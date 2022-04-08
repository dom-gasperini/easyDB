# tronix database and interface

# imports
from sales import *
from marketing import *
from admin import *
import datetime


# automatic marketing stuff
def get_date_time():

    # get the un-formatted date and time
    date = datetime.datetime.now()
    # get just today's date
    today = date.date()

    # check to see if the current date is a special marketing day
    sent_emails = special_day(today)

    if not sent_emails:
        # send the weekly email (monday = 0 sunday = 6, Hour:Minute:Second)
        if date.weekday == 0:
            print("\n\n\n")
            print("I am preforming automated marketing, DO NOT interrupt me until the all clear is given!!")
            print("Status: [ INCOMPLETE ]")
            # send the targeted emails!!!!
            targeted_advert()
            print("\n")
            print("STATUS: [ COMPLETED ]")
            print("You may proceed with any operations to or within the program")
            print("\n\n\n")


# main!
def main():

    print("\n")
    print("Welcome to the tronix database")
    print("\n")

    while True:
        # get date and time for automated marketing features
        get_date_time()

        # user interface
        print("Mode Select:")
        print("1: Sales")
        print("2: Marketing")

        # get mode
        mode = input("Select a mode (1 or 2): ")

        # help page
        if mode == 'help':
            help_page()

        # take em to sales
        elif mode == '1':
            sales()

        # take em to marketing
        elif mode == '2':
            marketing()

        elif mode == '3':
            rick_roll()

        # enter admin mode
        elif mode == 'admin':
            admin()

        # exit program
        elif mode == 'exit':
            print("goodbye!")
            exit()

        # if the input isn't anything
        else:
            print("\n")
            print("Invalid input, please try again")


# help stuff
def help_page():
    print("\n")
    print("Help Page:")
    print("Enter 1 or 2 to enter either the sales or marketing menus")
    print("You can return to this menu by entering return in the sales and marketing sub-menus")
    print("Type 'exit' to quit the program")
    print("\n")


# run it!
if __name__ == '__main__':
    main()
