from pymongo import MongoClient

connection = MongoClient()
database = connection['database']

def getAllUsers():
    ans = database.logins.find()
    return ans

def newUser(username,password):
    d = {'username': username, 'password': password}
    check = database.logins.find({'username': username}).count()
    if check != 0:
        return False
    else:        
        database.logins.insert(d)
        return True

def authenticate(username, password):
    check = database.logins.find({'username':username,'password':password}).count()
    if check != 0:
        return True
    else:
        return False

#def set_firewood(username,num_fire):
#    db.users.update(
#        {'username':username},
#        { $set:
#          { 'fire': num_fire}
#      }
#    )

#def essays_edited(num_essays):
 
def add_essay(title,author,length,essay_description,essay_content):
    if (database.essays.find({'title':title,'author':author}).count()>0):
        return False
    new_essay = {'title':title,'author':author,'length':length,'essay_description':essay_description,'essay_content':essay_content}
    database.essays.insert(newEntry)
    return True

def get_essay(title,author):
    if (database.users.find({'title':title,'author':author}).count()==1):
        return database.users.find({'title':title,'author':author})
    else:
        return False
    
