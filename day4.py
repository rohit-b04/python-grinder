import csv
import json

class MyError(Exception):
    pass

try:
    raise MyError("Somethig went wrong")
except MyError as e:
    print("Caught error: ", e)

def check_positive(num):
    if num < 0:
        raise MyError("Number must be positive")
    return num

try:
    print(check_positive(-3))
except Exception as e:
    print(e)


import re
class InvalidEmailError(Exception):
    pass

def check_email_pattern(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email address")

try:
    mail = 'abcc@gmail.com'
    check_email_pattern(mail)
    print("valid email")
except InvalidEmailError as e:
    print(e)
'''
with open("students.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    file.seek(0)
    reader = csv.reader(file)
    for row in reader:
    print(row)
'''
with open('people.json',"r" ) as fi:
    loaded = json.load(fi)
    print(loaded)