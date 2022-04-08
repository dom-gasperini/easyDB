# test grounds for stuff im experimenting with

# from database import *
# from product_index import *
import datetime
import shutil
from database import *
import keyboard
import time

break_program = False


def on_press(key):
    global break_program
    print(key)
    if key == keyboard.Key.end:
        print('end pressed')
        break_program = True
        return False


with keyboard.lis(on_press=on_press) as listener:
    while not break_program:
        print('program running')
        time.sleep(5)
    listener.join()


"""
helpful copy and pastes:

print('got here')
"""

"""
phone_number = '9084614134'

comparator = 0
most_frequent = ''

for i in database.db[phone_number].keys():

    value = database.db[phone_number][i]

    # to skip the bio attributes
    if isinstance(value, int):
        if value >= comparator:
            comp = value
            most_frequent = i

print("most frequent purchase = {}".format(most_frequent))
"""

"""
date = datetime.datetime.now()
print(date)

receipt_name = 'Dominic Gasperini_2021-07-22'

shutil.move('{}'.format(receipt_name), 'Receipts')
"""


import cv2
print("GeeksForGeeks")
print("Your OpenCV version is: " + cv2.__version__)