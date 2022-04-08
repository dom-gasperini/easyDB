# all the database stuff

# imports
import json
import os


# database class
class DataBase(object):
    def __init__(self, location):
        self.db = {}
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            pass
        return True

    # used to load the file for access
    def _load(self):
        self.db = json.load(open(self.location, "r"))

    # save information to the database
    def dump(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except FileNotFoundError:
            return False

    # to add user to the database
    def set(self, phone_number, value):
        try:
            self.db[str(phone_number)] = value
            self.dump()
        except Exception as e:
            print("[ ERROR ] Error Saving Values to Database : " + str(e))
            return False

    # search the data base using a phone number for admin
    def search(self, phone_number):
        try:
            return self.db[phone_number]
        except KeyError:
            print("No Value Can Be Found for " + str(phone_number))
            return False

    # search the data base using the phone number for sales
    def get(self, phone_number):
        try:
            name = self.db[str(phone_number)]['name']
            email = self.db[str(phone_number)]['email']
            phone_number = self.db[str(phone_number)]['phone_number']
            return name, email, phone_number
        except KeyError:
            return False

    # retrieve the excel file name
    def retrieve(self):
        try:
            length = len(self.db)
            for i in range(0, length):
                file_name = [key for key in self.db.keys()][i]
                using = self.db[str(file_name)]['status']
                if using == 'active':
                    return file_name

        except KeyError:
            return False

    # delete a user from the database
    def delete(self, phone_number):
        if phone_number not in self.db:
            return False
        del self.db[phone_number]
        self.dump()
        return True

    # used to wipe the database
    def reset(self):
        self.db = {}
        self.dump()
        return True


# init the database and set the database load file location
database = DataBase('database.txt')
