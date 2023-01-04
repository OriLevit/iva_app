import pprint

from pymongo import MongoClient

mongo_path = "mongodb+srv://orilevit:Orielle2504@volleyapp.ec5jmns.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_path)
print("Connected to server...")


def add_user(username, password, user_type="guest"):
    users_db = client.Users
    collection = users_db.users
    user = {
        "username": username,
        "password": password,
        "type": user_type
    }
    collection.insert_one(user)


def does_username_exist(username):
    user = client.Users.users.find_one({"username": username})
    if user is not None:
        return True
    else:
        return False


def print_all_users():
    printer = pprint.PrettyPrinter()
    users = client.Users.users.find({})
    if users is not None:
        for user in users:
            printer.pprint(user)


def check_login(usr, psw):
    user = client.Users.users.find_one({"username": usr})
    if user is not None:
        return psw == user["password"]
    else:
        return False
