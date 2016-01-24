from pymongo import MongoClient

connection = MongoClient()
database = connection['database']

def newUser(username,password):
    d = {'username': username, 'password': password, 'firewood': 20, 'essaysEdited': 0,'toEdit':''}
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
    cursor = database.logins.find({'username':username})
    newlist = list(cursor)
    for r in newlist:
        password = r.get('password')
        essaysEdited = r.get('essaysEdited')
        toEdit = r.get('toEdit')
        database.logins.update({'username':username}, {'username':username,'password':password,'firewood':num,'essaysEdited':essaysEdited,'toEdit':toEdit})
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
    newEntry = {'username':username,'link':link,'timesEdited':0,'newEdits':0}
    #check = database.essays.find({'link':link}).count()
    #if check != 0:
    #    return False
    #else:        
    database.essays.insert(newEntry)
    return True

def getEssayLinks(username):
    rawEssays = database.essays.find({'username':username})
    newlist = list(rawEssays)
    contents = []
    for r in newlist:
        contents.append(r.get('link'))
    return contents

def getAllEssayLinks(username):
    rawEssays = database.essays.find( { 'username': { '$ne': username } })
    newlist = list(rawEssays)
    contents = []
    editedAlready = getEditedBy(username)
    for r in newlist:
        for essay in editedAlready:
            if (r != essay):
                contents.append(r.get('link'))
    return contents

def getAllEssayEdits(username):
    rawEssays = database.essays.find( { 'username': { '$ne': username } })
    newlist = list(rawEssays)
    contents = []
    editedAlready = getEditedBy(username)
    for r in newlist:
        for essay in editedAlready:
            if (r != essay):
                contents.append(r.get('timesEdited'))
    return contents

def getRandomEssay(username):
    essays = getAllEssayLinks(username)
    nums = getAllEssayEdits(username)
    if nums == []:
        return 'No essay to edit'
    else:
        champ = nums[0]
        for n in nums:
            if n > champ:
                champ = n
        return essays[n]

def setToEdit(username,link):
    cursor = database.logins.find({'username':username})
    newlist = list(cursor)
    for r in newlist:
        password = r.get('password')
        firewood = r.get('firewood')
        essaysEdited = r.get('essaysEdited')
        database.logins.update({'username':username}, {'username':username,'password':password,'firewood':firewood,'essaysEdited':essaysEdited,'toEdit':link})

def getEditor(link):
    editor = database.logins.find({'toEdit':link})
    newlist = list(editor)
    for r in newlist:
        return r.get('username')

def getToEdit(username):
    toEdit = database.logins.find({'username':username})
    newlist = list(toEdit)
    for r in newlist:
        return r.get('toEdit')

def getTimesEdited(link):
    raw = database.essays.find({'link':link})
    newlist = list(raw)
    for r in newlist:
        return r.get('timesEdited')

def setTimesEdited(link,num):
    cursor = database.essays.find({'link':link})
    newlist = list(cursor)
    for r in newlist:
        username = r.get('username')
        link = r.get('link')
        newEdits = r.get('newEdits')
        database.essays.update({'link':link}, {'username':username,'link':link,'timesEdited':num,'newEdits':newEdits})
    return True

def getNewEdits(link):
    raw = database.essays.find({'link':link})
    newlist = list(raw)
    for r in newlist:
        return r.get('newEdits')

def setNewEdits(link,num):
    cursor = database.essays.find({'link':link})
    newlist = list(cursor)
    for r in newlist:
        username = r.get('username')
        link = r.get('link')
        timesEdited = r.get('timesEdited')
        database.essays.update({'link':link}, {'username':username,'link':link,'timesEdited':timesEdited,'newEdits':num})
    return True

def addEditor(username,essay):
    newEntry = {'username':username,'essay':essay}
    database.editors.insert(newEntry)
    return True

def getEditedBy(username):
    raw = database.editors.find({'username':username})
    newlist = list(raw)
    contents = []
    for r in newlist:
        contents.append(r.get('essay'))
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
