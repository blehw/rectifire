from flask import Flask, render_template, request, session, redirect, url_for, Markup
import module

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if 'logged' not in session:
        session['logged']=False
    if request.method=="GET":

    else:

@app.route('/login')
def login():
    if request.method=="GET":
        return render_template('login.html',s=session)
    if request.method=="POST":
        #We need to add a verification system
        if request.form['username']=="henry" and request.form['password']=='12345':
            session['logged']=True
            return redirect('/')
        else:
            return render_template('login.html',s=session,error='incorrect username or password")

#When a user clicks a button to logout, direct them here, log them out and redirect them
@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect('/')

if __name__=="__main__":
    app.debug = True
    app.secret_key="Don't tell anyone!"
    app.run('0.0.0.0', port=8000)
