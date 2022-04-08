# marketing

# imports
from database import *
from openpyxl import load_workbook
import yagmail


# marketing main
def marketing():
    print("\n\n")
    print("Welcome to Marketing")

    while True:
        print("1: Email Blast")
        print("2: Single Email")

        # get user input
        marketing_mode = input("Select a mode: ")

        # print help info
        if marketing_mode == 'help':
            input_help()

        # return to mode select
        elif marketing_mode == 'return':
            print("\n\n")
            break

        # send a category based email blast
        elif marketing_mode == '1':
            email_blast()

        # send a custom email blast
        elif marketing_mode == '2':
            single_email()

        # if anything besides 1, 2, help, or return is entered
        else:
            print("Invalid input, please select again")
            print("\n")


# for category specific blast
def email_blast():
    print("WARNING: THIS PROCESS CAN TAKE UPWARDS OF 15 MINUTES, PROCEED WITH CAUTION")

    # get all the information that is going in the email blast
    subject = write_subject()
    body = write_body()
    filename = add_attachment()

    # confirm that the user wants to send this email blast
    print("This is the subject of the email: {}".format(subject))
    print("This is the body of the email: {}".format(body))
    if filename is not None:
        print("This is the name of the file being attached: {}".format(filename))

    while True:
        choice = input("Are you sure you want to send this email to every customer in the database? (Y/N): ")

        # if choice is yes
        if choice.lower() == 'y':
            # notify user that the emails are being sent
            print("Sending emails now...")
            print("Status: [ INCOMPLETE ]")

            # increment through each person in the database
            for person in database.db:
                # get the email for each person
                recipient = database.db[person]["email"]

                # send the email
                send_email(recipient, subject, body, filename)

            # notify user that all the emails are finished being sent
            print("Status: [ COMPLETE ]")

            # return to marketing home
            return

        # if choice is no
        elif choice.lower() == 'n':
            print("Ok, cancelling this email blast")
            return
        # catching inputs that are not Y or N
        else:
            print("Invalid input, please enter Y or N")


# send a single email
def single_email():
    while True:
        print("\n")
        print("1: Search for Customer")
        print("2: Enter email manually")
        print("Or type 'return' to go back to the marketing menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                name, email, phone_number = search_customer()
                break
            except TypeError:
                print("That phone number couldn't be found in the database")
        elif choice == '2':
            email = input("Enter the email: ")
            break
        elif choice == 'return':
            print("\n\n")
            return
        else:
            print("Invalid input, please enter a valid choice")

    # set recipient of the email
    recipient = email
    # get the subject
    subject = write_subject()
    # get the body
    body = write_body()
    # add an attachment?
    filename = add_attachment()
    # send the email
    send_email(recipient, subject, body, filename)


# send the email
def send_email(recipient, subject, body, filename):
    # log into the account
    yag = yagmail.SMTP("tronix.advertising.services@gmail.com", "tronixAdverts!")

    # update user of email send status
    print("\n")
    print("Sending the emails now, please wait...")

    # send the email
    yag.send(
        to=recipient,
        subject=subject,
        contents=body,
        attachments=filename
    )

    # confirm that the emails have been sent
    print("The email(s) have been successfully sent")
    print("\n\n")


# write body
def write_body():
    # loop to confirm the body of the email
    while True:
        print("\n")
        print("Type 'cancel' at anytime to cancel the email")
        body = input("Enter the body of the email (only press enter when you're finished writing the body!): ")

        # cancel checkpoint
        if body == 'cancel':
            break

        print("\n")
        print("You entered: \n{}\n".format(body))
        confirm = input("Is that what you want the body of the email to be? (Y/N): ")
        if confirm.lower() == 'y':
            print("Ok great")
            # add some spacing between the logo and the body of the email
            body = body + "\n\n\n\n"
            # add the tronix logo into the email
            logo = yagmail.inline("tronix_logo.png")
            # add the automated email message no reply comment at the bottom
            auto_message = "\nThis is an automated email, please do not reply"
            body = [body, logo, auto_message]
            return body

        elif confirm.lower() == 'n':
            print("Ok, you can re-write it now")
        elif confirm.lower() == 'cancel':
            break
        else:
            print("Invalid input, please enter 'Y' or 'N'")


# write subject
def write_subject():
    # loop to confirm the subject of the email
    while True:
        print("\n")
        subject = input("Enter the subject of the email (only press enter when you're finished writing the subject!): ")

        # cancel email checkpoint
        if subject == 'cancel':
            break

        print("\n")
        print("You entered: \n{}\n".format(subject))
        confirm = input("Is that what you want the subject of the email to be? (Y/N): ")
        if confirm.lower() == 'y':
            print("Ok great")
            return subject
        elif confirm.lower() == 'n':
            print("Ok, you can re-write it now")
        elif confirm.lower() == 'cancel':
            break
        else:
            print("Invalid input, please enter 'Y' or 'N'")


# add attachment
def add_attachment():
    while True:
        print("\n")
        choice = input("Would you like to add any attachments to this email? (Y/N): ")

        # if yes to an attachment in the email
        if choice.lower() == 'y':
            while True:
                print("Remember, the file must be in the same folder as these files!")
                filename = input("Enter the filename exactly as is, including the file extension name: ")
                is_correct = input("Is this filename correct (Y/N or NA for no attachment): {}".format(filename))

                # confirmation logic
                if is_correct.lower() == 'y':
                    print("Ok great")
                    return filename
                elif is_correct.lower() == 'n':
                    print("Ok, please re-enter the filename now")
                elif is_correct == 'NA':
                    print("Ok, no attachments were added to the email")
                    return None
                else:
                    print("Invalid input, please enter Y or N")

        # if no to attaching a file to the email
        elif choice.lower() == 'n':
            print("No attachments were added to the email")
            return None
        elif choice.lower() == 'cancel':
            break
        else:
            print("Invalid input, please enter Y or N")


# targeted advertising weekly email sender
def targeted_advert():
    # increment through each person in the database
    for person in database.db:
        # get name
        name = database.db[person]["name"]
        # get email address
        email_address = database.db[person]["email"]
        # get phone number
        phone_number = database.db[person]["phone_number"]

        comparator = 0
        most_frequent = ''

        for i in database.db[phone_number].keys():

            value = database.db[phone_number][i]

            # to skip the bio attributes
            if isinstance(value, int):
                if value >= comparator:
                    comparator = value
                    most_frequent = i

        # add the information gathered into the email
        recipient = email_address
        subject = "Hello From Tronix!"
        body = "Hello {}!\nWe are offering a discount to you on {}! " \
               "Visit the store to learn more!\n" \
               "Thanks, and have a great day!".format(name, str(most_frequent))
        filename = None

        # send the email!
        send_email(recipient, subject, body, filename)


# check for any special marketing days
def special_day(today):
    # set the marketing dates file as the active file
    wb = load_workbook(filename='marketing_dates.xlsx')
    sheet = wb.active

    # do some wacky formatting cause types are weird sometimes
    today = "({})".format(today)
    if sheet['Z2'].value == today:
        return True

    # set the week based interval of sending the targeted emails
    week_delay = sheet['Z3'].value
    delay = 2

    # week delay logic
    if week_delay != delay:
        week_delay += 1
        sheet['Z3'] = week_delay
        wb.save(filename='marketing_dates.xlsx')
        return True

    # set the date comparison cell
    sheet['Z2'] = today
    wb.save(filename='marketing_dates.xlsx')

    # add all the dates to a list so we can loop through them
    dates = []
    for i in range(0, 366):
        cell = 'A' + str(i+1)
        date = sheet[cell].value
        dates.append(date)

    # set subject and body as empty so we know if this returns anything
    subject = ''
    body = ''

    # loop through all the dates cells to see if any of them match the current date
    for i in range(0, len(dates)):
        if dates[i] == today:
            index = dates.index(today)
            subject_cell = 'B' + str(index+1)
            body_cell = 'C' + str(index+1)
            # get the pre-set subject and body
            subject = sheet[subject_cell].value
            print(subject)
            body = sheet[body_cell].value
            # add some spacing between the logo and the body of the email
            body = body + "\n\n\n\n"
            # add the tronix logo into the email
            logo = yagmail.inline("tronix_logo.png")
            # add the automated email message no reply comment at the bottom
            auto_message = "\nThis is an automated email, please do not reply"
            body = [body, logo, auto_message]

    if subject == '' and body == '':
        return False
    # send the email cause it's a special marketing day
    else:
        # increment through the entire database of customer to send each one the special email
        for customer in database.db:
            # get customer email
            recipient = database.db[customer]['email']
            # set filename to none for now
            filename = None
            # send the email!
            send_email(recipient, subject, body, filename)

        # return True so the weekly email doesn't send as well if the days are the same
        return True


# search customer
def search_customer():
    # get search type
    search_type = input("Would you like to search via phone numbers or names (type 'phone' or 'name'): ")

    # if search type is the customer's name
    if search_type == 'name':
        # get name of customer
        customer_name = input("Enter the customer's name: ")

        # first see if the name is an exact match in the system
        for i in database.db:
            # set temp phone number
            temp_phone = database.db[i]["phone_number"]
            # set temp name
            temp_name = database.db[i]['name']

            # do the perfect match comparison
            if customer_name == temp_name:
                name, email, phone_number = database.get(temp_phone)
                # display customer information
                print("Name: {} | Email: {} | Phone #: {}".format(name, email, phone_number))
                return name, email, phone_number

        # if the exact match search fails, fall back to accuracy match
        import difflib

        # set accuracy
        accuracy = 75

        # iterate through each phone number in the database
        for i in database.db:
            # set temp phone number
            temp_phone = database.db[i]['phone_number']
            # set temp name
            possible_name = database.db[i]['name']

            # get the input and possible name match percentage
            match_percent = int(difflib.SequenceMatcher(None, customer_name, possible_name).ratio()*100)

            # if the match percent is greater than or equal to my predetermined accuracy
            if match_percent >= accuracy:
                # set all the customer info
                name, email, phone_number = database.get(temp_phone)
                # display customer information
                print("Name: {} | Email: {} | Phone #: {}".format(name, email, phone_number))
                return name, email, phone_number

            # this message only shows if no results were found
            print("There was no match to the entered name in the database")

    # if search type is a phone number
    elif search_type == 'phone':
        # get phone number
        phone_number = input("Enter the customer's phone number: ")

        try:
            # get customer info
            name, email, phone_number = database.get(phone_number)

            # display customer information
            print("Name: {} | Email: {} | Phone #: {}".format(name, email, phone_number))
            return name, email, phone_number

        except TypeError:
            print("invalid input, returning to the command line")


# help page
def input_help():
    print("\n")
    print("Help Page:")

    # category description
    print("Choose category blast to send an email blast to all customers "
          "who's most popular purchases fall in a certain category")

    # custom description
    print("Choose custom blast to send an email blast to either specific or all customers with custom parameters, like "
          "information about a holiday special or approaching sale")

    # return instructions
    print("Type: 'return' to go back to the main menu")
    print("\n")
