from datetime import datetime, timedelta
class Menu:
    def __init__(self, driver):
        self.days = []
        self.driver = driver
        self.choice = ""
        self.greeting = ("\nWelcome to the Automated Gym Booking System\nWhat would you like to do today?\n\n"
                         "========Main Menu========)\n1. Show Classes\n2. View Bookings\n3. Logout")

    def get_main_menu_choice(self):
        while True:
            self.choice = input("Choose 1-3: ").strip()

            if self.choice == '1':
                self.driver.retrieve_data()
                self.get_datetime()
                return self.schedule_menu()

            elif self.choice == '2':
                return "SHOW_CLASSES"
            elif self.choice == '3':
                return self.quit_program()
            else:
                print("WARNING: Invalid Input, try again")

    def schedule_menu(self):
        print("\nWhat day do you want to see?")
        if len(self.driver.tables) == 6 and len(self.days) == 7:
            del self.days[0]
        for day in self.days:
            print(f"{day}")
        return "1"

    def choose_table_data(self):
        while True:
            try:
                self.choice = int(input(f"Choose 1-{len(self.days)}: "))
            except ValueError:
                print("WARNING: Invalid Input")
            else:
                if self.choice in range(len(self.days)):
                    self.choice = str(self.choice)
                    return None

    def get_table(self):
        match self.choice:
            case '1':
                self.driver.current_table = 0
                return print(f"\n{self.driver.tables[0]}")
            case '2':
                self.driver.current_table = 1
                return print(f"\n{self.driver.tables[1]}")
            case '3':
                self.driver.current_table = 2
                return print(f"\n{self.driver.tables[2]}")
            case '4':
                self.driver.current_table = 3
                return print(f"\n{self.driver.tables[3]}")
            case '5':
                self.driver.current_table = 4
                return print(f"\n{self.driver.tables[4]}")
            case '6':
                self.driver.current_table = 5
                return print(f"\n{self.driver.tables[5]}")
            case '7':
                self.driver.current_table = 6
                return print(f"\n{self.driver.tables[6]}")
        return None

    def greet(self):
        print(self.greeting)

    def quit_program(self):
        print("Thank you for using the Automated Gym Booking System\nShutting down...")
        self.driver.driver.close()

    def get_datetime(self):
        self.days = []
        if len(self.driver.tables) == 7:
            for i in range(7):
                date = datetime.today() + timedelta(days=i)
                formatted = f'{date.strftime("%A")}, {date.strftime("%B")} {date.day}{self.format_days(date.day)}'
                self.days.append(f"{i + 1}. {formatted}")
        else:
            for i in range(7):
                date = datetime.today() + timedelta(days=i)
                formatted = f'{date.strftime("%A")}, {date.strftime("%B")} {date.day}{self.format_days(date.day)}'
                self.days.append(f"{i}. {formatted}")
        return

    def book_or_choose_again(self):
        while True:
            user_choice = input("Do you want to book or join the waitlist for any of these classes? (y/n): ").lower().strip()
            if user_choice == 'y':
                number_of_classes = self.driver.generate_booking_options()
                while True:
                    if number_of_classes > 1:
                        user_choice = input(f"choose between 1-{number_of_classes} or type 'exit' to go back to the main menu: ").lower().strip()
                    else:
                        user_choice = input(f"choose between 1 or type 'exit' to go back to the main menu: ").lower().strip()
                    if user_choice == "exit":
                        return "RETURN_TO_MAIN_MENU"
                    else:
                        try:
                            user_choice = int(user_choice)
                        except ValueError:
                            print("WARNING: Invalid Input")
                        else:
                            if user_choice in range(number_of_classes):
                                self.driver.confirm_class(user_choice)
                                return "RETURN_TO_MAIN_MENU"
                            else:
                                print("WARNING: Invalid Input")

            elif user_choice == 'n':
                while True:
                    user_choice = input("\nYou have the following options:\n1. Look at a different day\n"
                                        "2. Return to the main menu\n3. Exit program\nChoose 1-3: ")
                    if user_choice == '1':
                        self.schedule_menu()
                        self.choose_table_data()
                        self.get_table()
                        self.book_or_choose_again()
                    elif user_choice == '2':
                        return "RETURN_TO_MAIN_MENU"
                    elif user_choice == '3':
                        return self.quit_program()
                    else:
                        print("WARNING: Invalid Input")
            else:
                print("WARNING: Invalid Input")

    @staticmethod
    def format_days(day):
        if day % 10 == 1:
            return "st"
        elif day % 10 == 2:
            return "nd"
        elif day % 10 == 3:
            return "rd"
        else:
            return "th"
