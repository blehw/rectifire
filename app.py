from flask import Flask, render_template, request, session, redirect, url_for, Markup
import module

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if 'logged' not in session:
        session['logged']=False
    if request.method=="GET":
        firewood = module.getFirewood(session['logged'])
        #essays = module.getEssayContents(session['logged'])
        return render_template("home.html",s=session,f=firewood)
    if request.method=="POST":
        button = request.form['button']
        if (button=="Login"):
            username = request.form['username']
            password = request.form['password']
            if (module.authenticate(username,password)):
                session['logged']=username
                session['username'] = request.form['username']
                firewood = module.getFirewood(session['logged'])
                return render_template("home.html",s=session,f=firewood)
            else:
                return render_template('home.html',s=session,error='Incorrect username or password')
        if (button=="Signup"):
            username = request.form['username']
            password = request.form['password']
            if module.newUser(username,password):
                return render_template('home.html',s=session,error='You have successfully created an account!')
            else:
                return render_template('home.html',s=session,error='Invalid username or password')
        if (button=="Submit"):
            link = request.form['link']
            '''
            title = request.form['title']
            description = request.form['description']
            essay = request.form['essay']
            wordCount = str(module.wordCounter(essay))
            
            if (module.addEssay(title,session['logged'],module.wordCounter(essay),description,essay)):
            '''
            if (module.addEssay(session['logged'],link)):
                return render_template('home.html',s=session,error='Essay successfully submitted!')
            else:
                return render_template('home.html',s=session,error='Error with submitting essay')
        if (button=="Logout"):
            session['logged'] = None
            session['username'] = None
            return render_template('home.html')

#When a user clicks a button to logout, direct them here, log them out and redirect them
@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect('/')

@app.route('/youressays')
def youressays():
    essays = module.getEssayLinks(session['logged'])
    return render_template('youressays.html',e=essays)

@app.route('/edit')
def edit():
    return render_template('editothers.html')

if __name__=="__main__":
    app.debug = True
    app.secret_key="Don't tell anyone!"
    app.run('0.0.0.0', port=8000)
