# command prompt style admin controls of the database
import time
from product_index import *
from database import *
import yagmail
import webbrowser


# admin main
def admin():

    """
    # required special key input to unlock the admin section
    password = input("")
    if password != '~':
        exit()
    """

    print("\n")
    print("welcome to the admin area")

    while True:
        command = input("--> ")

        # for returning to home menu
        if command == 'return':
            print("\n")
            break

        elif command == 'help':
            help_page()

        elif command == 'add':
            add_customer()

        elif command == 'add product':
            add_product()

        elif command == 'delete product':
            delete_product()

        elif command == 'set excel file':
            set_excel_file()

        elif command == 'delete':
            delete_customer()

        elif command == 'search':
            search_customer()

        elif command == 'nuke':
            password = input("please enter the super admin password: ")
            if password == '~':
                nuke_database()
            else:
                print("you shouldn't be trying to wipe the database anyway idiot...")
                yag = yagmail.SMTP("tronix.advertising.services@gmail.com", "tronixAdverts!")
                yag.send(
                    to='dominicgasperini@gmail.com',
                    subject='attempted nuke on the tronix database',
                    contents='hey future me, hope you never get this email but you saw the subject',
                    attachments='database.txt'
                )
                print("your attempted actions have not gone un-noticed btw, just emailed the dev about this lol :)")

        elif command == 'exit':
            print("\n")
            print("later skater")
            exit()

        else:
            print("invalid input")


# add customer
def add_customer():
    # get all the required customer information
    print("this will also update a customer's information if they also exist")
    name = input("enter the name of the new customer: ")
    email = input("enter the email of the new customer: ")
    phone_number = input("enter the phone number of the new customer: ")

    # add information to customer information template
    info['name'] = name
    info['email'] = email
    info['phone_number'] = phone_number

    # add the new customer to the database
    database.set(phone_number, info)

    # display customer information
    print("Name: {} | Email: {} | Phone #: {}".format(name, email, phone_number))
    return


# delete customer
def delete_customer():
    # get phone number
    phone_number = input("enter the customer's phone number to delete their information: ")

    # get customer info
    name, email, phone_number = database.get(phone_number)

    # display customer information
    print("Name: {} | Email: {} | Phone #: {}".format(name, email, phone_number))

    # confirm deletion of customer
    confirm = input("are you sure you want to delete {} from the database (y/n): ".format(name))

    # confirm delete logic
    if confirm.lower() == 'y':
        print('the customers information has been deleted')
        # actually delete customer information
        database.delete(phone_number)
    elif confirm.lower() == 'n':
        print("cancelling the deletion of the customer's information")
        return
    else:
        print("invalid input, returning to command line")
        return


# search customer
def search_customer():
    # get search type
    search_type = input("search phone numbers or names (phone/name): ")

    # if search type is the customer's name
    if search_type == 'name':
        # get name of customer
        customer_name = input("enter the customer's name: ")

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

                # also show top purchase
                comparator = 0
                most_frequent = ''
                for j in database.db[phone_number].keys():

                    value = database.db[phone_number][j]

                    # to skip the bio attributes
                    if isinstance(value, int):
                        if value >= comparator:
                            comparator = value
                            most_frequent = j
                print("top purchased product: {} | {} purchases".format(most_frequent, comparator))
                return

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

                # also show top purchase
                comparator = 0
                most_frequent = ''

                for j in database.db[phone_number].keys():

                    value = database.db[phone_number][j]

                    # to skip the bio attributes
                    if isinstance(value, int):
                        if value >= comparator:
                            comparator = value
                            most_frequent = j
                print("top purchased product: {} | {} purchases".format(most_frequent, comparator))
                return

        # this only prints if there was no match
        print("there was no match to the entered name in the database")

    # if search type is a phone number
    elif search_type == 'phone':
        # get phone number
        phone_number = input("enter the customer's phone number: ")

        try:
            # get customer info
            name, email, phone_number = database.get(phone_number)

            # display customer information
            print("Name: {} | Email: {} | Phone #: {}".format(name, email, phone_number))

            # also show top purchase
            comparator = 0
            most_frequent = ''

            for j in database.db[phone_number].keys():

                value = database.db[phone_number][j]

                # to skip the bio attributes
                if isinstance(value, int):
                    if value >= comparator:
                        comparator = value
                        most_frequent = j
            print("top purchased product: {} | {} purchases".format(most_frequent, comparator))
            return

        except TypeError:
            print("invalid input, returning to the command line")

    # catch any input that isn't name or phone
    else:
        print("invalid input")
        return


# add product
def add_product():
    # get the name of the new product
    new_product_name = input("enter the name of the new product category: ")

    # check to see if that name already exists
    for name in range(2, 1001):
        product_name = sheet['B' + str(name)].value
        taken_product_id = sheet['A' + str(name)].value
        if product_name == new_product_name:
            print("that product name already is already populated at id: {}".format(taken_product_id))
            return

    # get the product id to assign the name to
    new_id_number = input("enter the id number (xxx) you want to assign to the new product: ")
    new_id_number = int(new_id_number)
    empty_product_name = None
    lookup_product_name = sheet['B' + str(new_id_number)].value

    # if the entered number has no name assigned
    if lookup_product_name == empty_product_name:
        sheet.cell(column=2, row=(int(new_id_number) + 2), value="{}".format(new_product_name))
        wb.save(filename=file)
        print("new product: {} | product id: {}".format(new_product_name, new_id_number))
        return
    # if the new product id is not already being used
    else:
        print("this id is already in use: {}".format(lookup_product_name))
        return


# delete product
def delete_product():
    # get product id to delete
    product_id = input("enter the product id you would like to clear (xxx): ")
    # get product name
    row_num = int(product_id) + 2
    product_name = sheet['B' + str(row_num)].value
    # display product information
    print("product name: {} | product id: {}".format(product_name, product_id))

    # confirm delete
    confirm = input("are you sure you want to clear this product id of the assigned product (Y/N): ")
    if confirm.lower() == 'y':
        # clear cell by setting it to an empty string
        sheet.cell(column=2, row=(int(product_id) + 2), value="")
        wb.save(filename=file)
        print("product id: {} was cleared".format(product_id))
    elif confirm.lower() == 'n':
        print("ok, cancelling")
    else:
        print("invalid input, please try again")


# set the active product index excel file
def set_excel_file():
    # display current excel file
    old_file_name = excel_file_storage.retrieve()
    print("old active file name: {}".format(old_file_name))

    # get the name of the new file
    new_file_name = input("enter the exact filename of the excel file (with '.xlsx') or cancel to cancel: ")

    # if cancel
    if new_file_name == 'cancel':
        print("{} will remain the current active file".format(old_file_name))
        return

    # delete the old file
    excel_file_storage.delete(old_file_name)

    # set new file as active and save
    files.update(file_name=new_file_name, status='active')
    excel_file_storage.set(new_file_name, files)

    # done message
    print("{} is now the active file | {} has been de-activated".format(new_file_name, old_file_name))


# nuke the database
def nuke_database():
    confirm = input("are you sure you want to delete all data from the database (y/n): ")
    if confirm.lower() == 'y':

        # double confirm the nuke
        double_confirm = input("are positive you want to wipe the database clean (y/n): ")
        if double_confirm.lower() == 'y':
            # send myself an emergency backup of the database
            yag = yagmail.SMTP("tronix.advertising.services@gmail.com", "tronixAdverts!")
            yag.send(
                to='dominicgasperini@gmail.com',
                subject='the tronix database was just nuked',
                contents='hey future me, an emergency backup of the database is attached to this email since there '
                         'is no reason to ever delete the entire database',
                attachments='database.txt'
            )
            # actually wipe the database
            database.reset()
            print("the database has been wiped")
        # if no
        elif double_confirm == 'n':
            print("the nuke was disarmed, make up your mind next time and don't do it")
            return
        # catches all the other non y/n inputs
        else:
            print("invalid input, returning to command line")
    # initial no for nuke request
    elif confirm.lower() == 'n':
        print("good you should never do that idiot")
        return
    else:
        print("invalid input, returning to command line")
        return


# rick roll
def rick_roll():
    # lol get rick rolled idiot
    print("\n\n")
    print("oh???")
    time.sleep(1.5)
    print("a hidden feature??")
    time.sleep(1.5)
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ", new=1)
    print("hahahahah get rick rolled")
    print("\n\n")
    return


# help stuff
def help_page():
    print("\n")
    print("\n")
    print("list of commands:")

    # search
    print("search: find a user and display all of their info and spending habits in the database")

    # add customer
    print("add: manually add a new customer without actively making a sale")
    print("this will also update a customer's information if they also exist")

    # delete customer
    print("delete: permanently delete a user and all of their information from the database")

    # add product group
    print("add product: add a new product group to track more types customer purchase habits")

    # set active excel file
    print("set excel file: sets the active file of the product index, must be entered as '.xlsx'")

    # delete product group
    print("delete product: delete a product group")

    # database reset
    print("nuke: completely and permanently deletes the entire database")

    # return to main menu
    print("\n")
    print("return: return to the home menu")
    print("\n")
    print("\n")
    return
