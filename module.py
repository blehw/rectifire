from pymongo import MongoClient

connection = MongoClient()
database = connection['database']

def newUser(username,password):
    ans = database.users.find({username:True})
    for r in ans:
        return False
    newEntry = {'username': username, 'password': password, 'fire':10}
    database.users.insert(newEntry)
    return True

def authenticate(username, password):
    if (database.users.find({'uname':name,'password':password}).count()==1):
        return True
    return "noUser"

def set_firewood(username,num_fire):
    db.users.update(
        {'username':username},
        { $set:
          { 'fire': num_fire}
      }
    )

def essays_edited(num_essays):
 
def add_essay(title,author,length,essay_description,essay_content):
    if (database.essays.find({'title':title,'author':author}).count()>0):
        return False
    new_essay = {'title':title,'author':author,'length':length,'essay_description':essay_description,'essay_content':essay_content}
    database.essays.insert(newEntry)
    return True

def get_essay(title,author):
    if (database.users.find({'title':title,'author':author}).count()==1):
        return database.users.find({'title':title,'author':author}
    return False
    
