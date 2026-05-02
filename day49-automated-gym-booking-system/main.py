from web_driver import Driver
from menu import Menu
TEST_EMAIL = "asmalldev@test.com"
TEST_PASSWORD = "Thisisatest123!"

def main():
    while True:
        menu.greet()
        menu_choice = menu.get_main_menu_choice()

        if menu_choice == '1':
            menu.choose_table_data()
            menu.get_table()

            booking_choice = menu.book_or_choose_again()
            if booking_choice == 'RETURN_TO_MAIN_MENU':
                continue
        else:
            booking_menu_choice = driver.show_bookings()
            if booking_menu_choice == "CANCEL_BOOKING_MENU":
                cancel_menu_choice = driver.cancel_bookings()
                if cancel_menu_choice == "RETURN_TO_MAIN_MENU":
                    continue
                else:
                    menu.quit_program()
                    break
            elif booking_menu_choice == "RETURN_TO_MAIN_MENU":
                continue
            else:
                menu.quit_program()
                break

if __name__ == "__main__":
    driver = Driver(TEST_EMAIL, TEST_PASSWORD)
    menu = Menu(driver)
    driver.log_in()
    main()