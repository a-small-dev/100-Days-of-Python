import os, time
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.chrome_options = None
        self.schedule = {}
        self.numbered_schedule = {}
        self.bookings = []
        self.waitlists = []
        self.gym_url = "https://appbrewery.github.io/gym/"
        self.schedule_url = "https://appbrewery.github.io/gym/schedule/"
        self.bookings_url = "https://appbrewery.github.io/gym/my-bookings/"
        self.tables = []
        self.bookings_table = []
        self.day_groups = None
        self.current_table = None
        self.logged_in = False
        self.set_options()
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def set_options(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        self.chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        return

    def log_in(self):
        print("Logging in....")
        self.driver.get(url=self.gym_url)

        sign_in_page = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "Home_heroButton__3eeI3")))
        sign_in_page.click()

        email_entry = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, "email-input")))
        email_entry.send_keys(self.email)

        password_entry = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, "password-input")))
        password_entry.send_keys(self.password)

        submit_button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, "submit-button")))
        submit_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Schedule_dayGroup__y79__")))

        if self.driver.current_url == self.schedule_url:
            self.logged_in = True
            return print("Successfully logged in")
        else:
            return print("Login Failed")

    def retrieve_data(self):
        if self.logged_in:
            while True:
                if self.driver.current_url != self.schedule_url:
                    schedule_link = self.driver.find_element(By.ID, "schedule-link")
                    schedule_link.click()
                else:
                    break
            self.day_groups = None
            self.schedule = {}
            self.numbered_schedule = {}
            self.tables = []
            print("\nRetrieving Data....")
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Schedule_dayGroup__y79__")))

            self.day_groups = self.driver.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")
            i = 0

            for group in self.day_groups:
                date = group.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs")
                class_block = group.find_elements(By.CLASS_NAME, "ClassCard_card__KpCx5")
                j = 1
                class_info = {}

                for class_ in class_block:
                    paragraphs = class_.find_elements(By.TAG_NAME, "p")
                    class_name = class_.find_element(By.TAG_NAME, "h3")
                    class_time = paragraphs[0]
                    class_instructor = paragraphs[1]
                    class_duration = paragraphs[2]
                    class_availability = paragraphs[3]
                    class_info[f"Class {j}"] = {"Class:": class_name.text,
                                                class_time.text.split()[0]: \
                                                    f"{class_time.text.split()[1]} {class_time.text.split()[2]}",
                                                class_instructor.text.split()[0]: \
                                                    f"{class_instructor.text.split()[1]} {class_instructor.text.split()[2]}",
                                                class_duration.text.split()[0]: \
                                                    f"{class_duration.text.split()[1]} {class_duration.text.split()[2]}",
                                                class_availability.text.split()[0]: \
                                                    f"{class_availability.text.split()[1]} {class_availability.text.split()[2]} "
                                                    f"{class_availability.text.split()[3]} {class_availability.text.split()[4]}",
                                                'Full': class_.get_attribute("data-is-fully-booked")}
                    j += 1
                self.schedule[date.text] = class_info
                self.numbered_schedule[i] = class_info
                i += 1

            for day in self.schedule:
                table = PrettyTable()
                table.field_names = ["Date", "Class", "Time", "Instructor", "Duration", "Availability"]
                for classes in self.schedule[day]:
                    class__ = self.schedule[day][classes]
                    table.add_row(
                        [day, class__['Class:'], class__['Time:'], class__['Instructor:'], class__['Duration:'],
                         class__['Available:']])
                self.tables.append(table)
            return print("Data retrieved")
        else:
            return print("You are not logged in.")

    def generate_booking_options(self):
        table = PrettyTable()
        i = 1
        table.field_names = ["#", "Class", "Book / Waitlist"]
        for gym_class in self.numbered_schedule[self.current_table]:
            if self.numbered_schedule[self.current_table][gym_class]['Full'] == 'true':
                table.add_row([i, self.numbered_schedule[self.current_table][gym_class]['Class:'], "Waitlist"])
            else:
                table.add_row([i, self.numbered_schedule[self.current_table][gym_class]['Class:'], "Book"])
            i += 1
        print(f"\n{table}")
        return i - 1

    def confirm_class(self, class_number):
        print(f"\nConfirming {self.numbered_schedule[self.current_table][f'Class {class_number}']['Class:']}...")
        for group in self.day_groups:
            date = group.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs")
            class_block = group.find_elements(By.CLASS_NAME, "ClassCard_card__KpCx5")
            for class_ in class_block:
                total_matched = 0
                paragraphs = class_.find_elements(By.TAG_NAME, "p")
                if list(self.schedule)[self.current_table] == date.text:
                    total_matched += 1
                if (class_.find_element(By.TAG_NAME, "h3").text ==
                        self.numbered_schedule[self.current_table][f'Class {class_number}']['Class:']):
                    total_matched += 1
                if (self.numbered_schedule[self.current_table][f'Class {class_number}']['Time:'] ==
                        f"{paragraphs[0].text.split()[1]} {paragraphs[0].text.split()[2]}"):
                    total_matched += 1
                if (self.numbered_schedule[self.current_table][f'Class {class_number}']['Instructor:'] ==
                        f"{paragraphs[1].text.split()[1]} {paragraphs[1].text.split()[2]}"):
                    total_matched += 1
                if (self.numbered_schedule[self.current_table][f'Class {class_number}']['Duration:'] ==
                        f"{paragraphs[2].text.split()[1]} {paragraphs[2].text.split()[2]}"):
                    total_matched += 1
                if (self.numbered_schedule[self.current_table][f'Class {class_number}']['Available:'] ==
                        f"{paragraphs[3].text.split()[1]} {paragraphs[3].text.split()[2]} "
                        f"{paragraphs[3].text.split()[3]} {paragraphs[3].text.split()[4]}"):
                    total_matched += 1
                if total_matched == 6:
                    print("Found class")
                    schedule_button = class_.find_element(By.CSS_SELECTOR, ".ClassCard_cardActions__tVZBm button")
                    if schedule_button.get_attribute("disabled"):
                        print("Looks like you already booked/waitlisted that class")
                    else:
                        print(f"Successfully {schedule_button.text.split()[0]}ed the {schedule_button.text.split()[1]}!")
                        schedule_button.click()

    def show_bookings(self):
            self.bookings = []
            self.waitlists = []

            bookings_button = self.driver.find_element(By.ID, "my-bookings-link")
            bookings_button.click()

            if self.driver.current_url == self.bookings_url:
                all_bookings = self.driver.find_elements(By.CLASS_NAME, "MyBookings_cancelButton__7jZTU")
                if len(all_bookings) < 1:
                    print("Looks like you have no bookings at this time.")
                    return "RETURN_TO_MAIN_MENU"
                else:
                    bookings = self.driver.find_elements(By.CSS_SELECTOR, "[id*='booking-card-booking']")
                    waitlists = self.driver.find_elements(By.CLASS_NAME, "MyBookings_bookingCard__VRdrR.MyBookings_waitlist__rD_tl")

                    for booking in bookings:
                        self.format_bookings(booking.text)

                    for waitlist in waitlists:
                        self.format_waitlists(waitlist.text)

                    self.build_bookings_table()
                    print(f"\n{self.bookings_table}")
                    choice = input("What would you like to do:\n1. Cancel a booking / waitlist\n2. Return to the main menu\n"
                                   "3. Quit program\nChoose 1-3: ").strip()
                    while True:
                        if choice == '1':
                            return "CANCEL_BOOKING_MENU"
                        elif choice == '2':
                            return "RETURN_TO_MAIN_MENU"
                        elif choice == '3':
                            return "QUIT_PROGRAM"
                        else:
                            print("WARNING: Invalid Input")
            return None

    def cancel_bookings(self):
        all_bookings = self.driver.find_elements(By.CLASS_NAME, "MyBookings_cancelButton__7jZTU")
        if len(all_bookings) < 1:
            print("\nLooks like you have no bookings at this time.")
            return "RETURN_TO_MAIN_MENU"
        else:
            cancel_bookings_choice = input(f"\nWhich booking would you like to cancel?\nChoose "
                                           f"1-{len(self.bookings) + len(self.waitlists)}, 'all', 'main menu', or 'quit': ")
            while True:
                if cancel_bookings_choice == 'all':
                    self.cancel_all_bookings()
                    return "RETURN_TO_MAIN_MENU"
                elif cancel_bookings_choice == 'main menu':
                    return "RETURN_TO_MAIN_MENU"
                elif cancel_bookings_choice == 'quit':
                    return "QUIT_PROGRAM"
                else:
                    try:
                        cancel_bookings_choice = int(cancel_bookings_choice)
                    except ValueError:
                        print("WARNING: Invalid Input")
                    else:
                        if cancel_bookings_choice in range(len(self.bookings) + len(self.waitlists) + 1):
                            self.cancel_specific_booking(cancel_bookings_choice)
                            return "RETURN_TO_MAIN_MENU"
                        else:
                            print("WARNING: Invalid Input2")


    def format_bookings(self, unf_booking):
        formatted = ''
        sentences = unf_booking.splitlines()
        for i in range(4):
            formatted += sentences[i] + "\n"
        self.bookings.append(formatted)
        return

    def format_waitlists(self, unf_waitlist):
        formatted = ''
        sentences = unf_waitlist.splitlines()
        for i in range(3):
            formatted += sentences[i] + "\n"
        self.waitlists.append(formatted)
        return

    def build_bookings_table(self):
        i = 1
        self.bookings_table = []
        table = PrettyTable()
        table.field_names = ['#', 'Booking / Waitinglist', 'Class Info']
        for booking in self.bookings:
            table.add_row([i, 'Booking', booking], divider=True)
            i += 1
        for waitlist in self.waitlists:
            table.add_row([i, "Waitlist", waitlist], divider=True)
            i += 1
        table.align = "c"
        self.bookings_table = table
        return

    def cancel_all_bookings(self):
        all_bookings = self.driver.find_elements(By.CLASS_NAME, "MyBookings_cancelButton__7jZTU")
        for booking in all_bookings:
            booking.click()
        time.sleep(1)
        all_bookings = self.driver.find_elements(By.CLASS_NAME, "MyBookings_cancelButton__7jZTU")
        if len(all_bookings) == 0:
            print("\nSuccessfully canceled all bookings")
            return
        else:
            print("\nSomething went wrong, couldn't cancel all bookings")
            return

    def cancel_specific_booking(self, booking_number):
        all_bookings = self.driver.find_elements(By.CLASS_NAME, "MyBookings_cancelButton__7jZTU")
        total_bookings_before = len(all_bookings)

        all_bookings[booking_number - 1].click()

        all_bookings = self.driver.find_elements(By.CLASS_NAME, "MyBookings_cancelButton__7jZTU")
        total_bookings_after = len(all_bookings)

        if total_bookings_after < total_bookings_before:
            print("\nSuccessfully deleted booking!")
            return
        else:
            print("\nSomething went wrong, couldn't cancel the booking")
            return