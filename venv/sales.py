# sales

# imports
import smtpd
import socket
from database import *
from product_index import *
from openpyxl import load_workbook
import datetime
import yagmail
import shutil


# sales main
def sales():
    # main loop
    while True:
        print("\n\n")
        print("Welcome to Sales")

        # init valid phone number
        valid_phone_number = False

        # get customer info
        phone_number = input("Enter the customers phone number: ")

        if phone_number == 'help':
            input_help()
            continue

        elif phone_number == 'return':
            print("\n\n")
            break

        try:
            # ensure the phone number entered was valid
            valid_phone_number, phone_number = filter_phone_number(phone_number)

        # if what was entered was not a phone number or valid command pass to the else statement
        except TypeError:
            pass

        # if the phone number entered is valid
        if valid_phone_number:
            # query database for the customer already existing
            exists = database.get(phone_number)
            if not exists:
                new_customer(phone_number)
                do_sale(phone_number)

            # the customer exists in the database
            else:
                existing_customer(phone_number)
                do_sale(phone_number)

        # if phone number is not valid
        else:
            print("the information entered was not valid, please try again")


# input filter
def filter_phone_number(phone_number):

    while True:
        # set default validity state
        valid_phone_number = False

        if len(phone_number) != 10:
            return valid_phone_number

        else:
            valid_phone_number = True

        print("\n")
        print("Phone Number Entered: {}".format(phone_number))
        confirm = input("Is this correct (Y/N): ")
        if confirm.lower() == 'y':
            break
        if confirm.lower() == 'n':
            print("Ok, you can re-enter the phone number now")
            phone_number = input("Enter the customers phone number: ")
        else:
            print("Invalid input, please enter Y or N")

    return valid_phone_number, phone_number


# new customer
def new_customer(phone_number):
    print("This customer is new!")

    # get more customer information
    name = input("Enter the customer's name: ")
    email = input("Enter the customer's email: ")

    # update the empty dictionary of customer info
    info.update(name=name, email=email, phone_number=phone_number)

    # add the new customer to the database
    database.set(phone_number, info)
    return


# existing customer
def existing_customer(phone_number):
    print('This is an existing customer')
    name, email, phone_number = database.get(phone_number)

    # print customer information
    print("\n")
    print("Name: {} | Email: {} | Phone #: {}".format(name, email, phone_number))
    return


# do sale
def do_sale(phone_number):
    # get some customer info
    name, email, phone_number = database.get(phone_number)

    while True:
        try:
            # get the number of products being purchased by the customer
            num_of_products = int(input("How many products are being sold: "))
            if num_of_products < 0:
                print("Invalid input, the number of products must be greater than zero")
            else:
                break
        except TypeError:
            print("A number must be entered")
        except ValueError:
            print("A number must be entered")

    # create purchased product list and cumulative price
    purchased_products = []
    price_list = []

    # get the product id numbers for each item being purchased
    for i in range(0, int(num_of_products)):
        product_name = ''
        try:
            # get product id
            purchased_product_id = input("Enter the product ID (xxx): ")

            if int(purchased_product_id) < 0:
                print("\n")
                print("Invalid input, the product ID must be greater than 000")
                continue
            # get the product name from the given id number
            product_id = int(purchased_product_id) + 2
            product_name = sheet['B' + str(product_id)].value

            # get the price of the product
            product_price = sheet['C' + str(product_id)].value

            # add the purchased product to the running list
            purchased_products.append(product_name)

            # add price
            price_list.append(product_price)

        # block a non integer input
        except ValueError:
            print("Invalid input, a number must be entered")

        # add 1 to the customer's product specific purchase frequency
        database.db[str(phone_number)][str(product_name)] += 1
        # save the changes made to customer's profile
        database.dump()

    # TODO: add more bezos features

    # get the name of the employee who made the sale
    employee_name = input("Enter your name to log the sale: ")

    # get total price
    total_price = 0
    for i in range(len(price_list)):
        total_price += price_list[i]

    # log information about the sale in sales_log.xlsx
    purchased_products_list = ''
    for i in range(len(purchased_products)):
        purchased_products_list += purchased_products[i] + ' '

    log_sale(name, purchased_products_list, total_price, employee_name)

    # create and save a receipt
    print_receipt(name, purchased_products, price_list, employee_name)
    print("Purchase receipt created")

    # send a purchase confirmation email to the customer
    purchase_email(name, email, purchased_products)

    # print the purchased product and the name of the customer who purchased it
    print("Completed Purchase for: {} | Product: {} | Total: ${}".format(name, purchased_products, total_price))

    return


# sales logger
def log_sale(name, purchased_products, total_price, employee_name):

    # set sales log as the active file
    excel_doc = load_workbook(filename='sales_log.xlsx')
    page = excel_doc.active

    # start the search for the next empty row at the second row since the row titles are in row 1
    row = 2

    # search until the next empty row is found
    while True:
        # get the value of the cell
        cell = page['A' + str(row)].value
        # if the cell is empty
        if cell is None:

            # log the date and time
            date_and_time = datetime.datetime.now()
            page['A' + str(row)] = date_and_time

            # log the products sold
            page['B' + str(row)] = purchased_products

            # log the name of the customer who purchased the product
            page['C' + str(row)] = name

            # log the total purchased price
            page['D' + str(row)] = total_price

            # log the name of the employee who made the sale
            page['E' + str(row)] = employee_name

            # save the excel file
            excel_doc.save(filename='sales_log.xlsx')

            return

        # increment to the next row if the the cell is not empty
        else:
            row += 1


# send purchase email
def purchase_email(name, email, purchased_products):
    # log into the account
    # removed the email and password obviously for security reasons
    email = ""
    password = ""
    yag = yagmail.SMTP(email, password)

    # email stuff
    recipient = email
    subject = 'Purchase Confirmation Email'
    body = 'Hello {}, this is an email confirming your purchase of: {}. ' \
           'We hope you enjoyed your shopping experience! Thanks for shopping at Tronix!'.format(name,
                                                                                                 purchased_products)
    # add some spacing between the logo and the body of the email
    body = body + "\n\n\n\n"
    # add the tronix logo into the email
    logo = yagmail.inline("tronix_logo.png")
    # add the automated email message no reply comment at the bottom
    auto_message = "\nContact us at: 609-607-8882 or tronixautosports@gmail.com" \
                   "\nVisit us at our Barnegat Location!" \
                   "\n\nThis is an automated email, please do not reply, thanks!"

    # condense the body into the list format that stackoverflow told me about
    body = [body, logo, auto_message]

    # update user of email send status
    print("\n")
    print("Sending the confirmation email now, please wait...")

    try:
        # send the email
        yag.send(
            to=recipient,
            subject=subject,
            contents=body,
        )

        # message to user
        print("Purchase confirmation email sent")
        print("\n")

    # perhaps the internet is no good or the "less secure apps" thing in the google account needs to be reset
    except socket.gaierror:
        print("The email failed to send the email right now, please try re-connecting to the internet")

    return


# print receipt
def print_receipt(name, purchased_products, price_list, employee_name):

    # create the name of the receipt
    date = datetime.datetime.now()
    receipt_name = str(name) + "_" + str(date)    # format: dominic gasperini _ 2021-01-01

    # create a new text file
    receipt = open("{}".format(receipt_name), "w+")

    # write to the text file
    receipt.write("Tronix Receipt: \n\nName: {}   |   Date of Purchase: {}  |   Sales Associate: {}".
                  format(name, date, employee_name))

    # column titles
    num_of_products = len(purchased_products)
    receipt.write("\n\n")
    receipt.write("No:  |  Product Name:  |  Price: ")

    # purchased product listing
    for i in range(num_of_products):
        receipt.write("\n")
        receipt.write("{}:   |  {}  |   {}".format(i+1, purchased_products[i], ('$' + str(price_list[i]))))

    # total price
    receipt.write("\n\n")
    total_price = sum(price_list)
    receipt.write("Total: ${}".format(total_price))

    # contact information and other stuff at the bottom
    receipt.write("\n\n\n")
    receipt.write("Thanks for shopping at Tronix!\nWe hope you enjoyed your shopping experience!")
    receipt.write("Contact us at: 609-607-8882 or tronixautosports@gmail.com\nVisit us at our Barnegat Location!")

    # close receipt file
    receipt.close()

    # move the receipt to the receipts folder
    shutil.move('{}'.format(receipt_name), 'Receipts')

    return


# helpful information
def input_help():
    print("\n")
    print("Help Page:")

    # phone number format
    print("Phone Number Format Example: 1234567890")

    # option to return to the main menu
    print("Enter 'return' to go back to mode select")
    print("\n")
    return
