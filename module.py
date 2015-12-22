from pymongo import MongoClienimport re;

connection = MongoClient()
database = connection['database']

def newUser(username,password):
    ans = database.users.find({username:True})
    for r in ans:
        return False
    newEntry = {'username': username, 'password': password}
    database.users.insert(newEntry)
    return True
