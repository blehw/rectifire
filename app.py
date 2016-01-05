from flask import Flask, render_template, request, session, redirect, url_for, Markup
import module

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    #if 'logged' not in session:
    #    session['logged']=False
    if request.method=="GET":
        return render_template("home.html")
    else:
        if button == "Signup":
            button = request.form['button']

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template('login.html',s=session)
    if request.method=="POST":
<<<<<<< HEAD
        if (request.form['button']=="login"):
            if (authenticate(request.form['username'],request.form['password'])):
                session['logged']=True
                return redirect('/')
            else:
                return render_template('login.html',s=session,error='incorrect username or passwor')
=======
        if (authenticate(request.form['username'],request.form['password'])):
            session['logged']=True
            return redirect('/')
>>>>>>> 181e5fe4388600fdfd3195586860c87545c8c4df
        else:
            if (newUser(request.form['username'],request.form['password'])):
                session['logged']=True
                return redirect('/')
            else:
                 return render_template('login.html',s=session,error='Invalid username or passwor')
            

#When a user clicks a button to logout, direct them here, log them out and redirect them
@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect('/')

if __name__=="__main__":
    app.debug = True
    app.secret_key="Don't tell anyone!"
    app.run('0.0.0.0', port=8000)
