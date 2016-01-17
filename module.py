from pymongo import MongoClient

connection = MongoClient()
database = connection['database']

def newUser(username,password):
    d = {'username': username, 'password': password, 'firewood': 20, 'essaysEdited': 0}
    check = database.logins.find({'username': username}).count()
    if check != 0:
        return False
    else:        
        database.logins.insert(d)
        return True

def getAllUsers():
    ans = database.logins.find()
    return ans

def authenticate(username, password):
    check = database.logins.find({'username':username,'password':password}).count()
    if check != 0:
        return True
    else:
        return False

def wordCounter(essay):
    count = 0
    words = essay.split()
    for num in words:
        count += 1
    return count
 
def getFirewood(username):
    user = database.logins.find({'username':username})
    newlist = list(user)
    for r in newlist:
        return r.get('firewood')

def setFirewood(username,num):
    database.logins.update({'username':username}, {'firewood':num})
    return True

def getEssaysEdited(username):
    user = database.logins.find({'username':username})
    return user.get('essaysEdited')

def addEssaysEdited(username,num):
    prevEssaysEdited = getEssaysEdited(username)
    newEssaysEdited = prevEssaysEdited + num
    database.logins.update({'username':username}, {'essaysEdited':newEssaysEdited})
    return True

def addEssay(username,link):
    newEntry = {'username':username,'link':link}
    check = database.essays.find({'link':link}).count()
    if check != 0:
        return False
    else:        
        database.essays.insert(newEntry)
        return True

def getEssayLinks(username):
    rawEssays = database.essays.find({'username':username})
    newlist = list(rawEssays)
    contents = []
    for r in newlist:
        contents.append(r.get('link'))
    return contents

'''
def addEssay(title,author,length,essay_description,essay_content):
    newEntry = {'title':title,'author':author,'length':length,'essay_description':essay_description,'essay_content':essay_content}
    check = database.essays.find({'title':title}).count()
    if check != 0:
        return False
    else:        
        database.essays.insert(newEntry)
        return True

def getEssay(title,author):
    if (database.essays.find({'title':title,'author':author}).count()==1):
        return database.users.find({'title':title,'author':author})
    else:
        return "No essay found"

def getEssayTitles(username):
    rawEssays = database.essays.find({'author':username})
    newlist = list(rawEssays)
    contents = []
    for r in newlist:
        essays.append(r.get('essay_content'))
    return contents

def getEssayLengths(username):
    rawEssays = database.essays.find({'author':username})
    newlist = list(rawEssays)
    contents = []
    for r in newlist:
        essays.append(r.get('essay_content'))
    return contents

def getEssayDescriptions(username):
    rawEssays = database.essays.find({'author':username})
    newlist = list(rawEssays)
    contents = []
    for r in newlist:
        essays.append(r.get('essay_content'))
    return contents
    
def getEssayContents(username):
    rawEssays = database.essays.find({'author':username})
    newlist = list(rawEssays)
    contents = []
    for r in newlist:
        contents.append(r.get('essay_content'))
    return contents
'''
