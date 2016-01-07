from flask import Flask, render_template, request, session, redirect, url_for, Markup
import module

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if 'logged' not in session:
        session['logged']=False
    if request.method=="GET":
        return render_template("home.html",s=session)
    if request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        if (request.form['button']=="login"):
            if (module.authenticate(username,password)):
                session['logged']=username
                session['username'] = request.form['username']
                return render_template("home.html",s=session)
            else:
                return render_template('home.html',s=session,error='incorrect username or password')
        if (request.form['button']=="signup"):
            if module.newUser(username,password):
                return "You have signed up!"
            else:
                return render_template('home.html',s=session,error='Invalid username or password')

#When a user clicks a button to logout, direct them here, log them out and redirect them
@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect('/')

#Testing page to see all user accounts
@app.route('/allusers')
def allusers():
    users = module.getAllUsers()
    return users

if __name__=="__main__":
    app.debug = True
    app.secret_key="Don't tell anyone!"
    app.run('0.0.0.0', port=8000)
