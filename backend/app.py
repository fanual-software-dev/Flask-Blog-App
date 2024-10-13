from flask import Flask,redirect,render_template,url_for,request,session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'FanBun'
# app.permanent_session_lifetime = timedelta(days=3)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/users')
def users():
    if 'user' in session and 'password' in session:
        user = session['user']
        password = session['password']
        return f'<p>User Name : {user}</p> <p>Password : {password}</p>'

@app.route('/', methods = ["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form['email']
        password = request.form['password']
        # session.permanent = True
        session['user'] = user
        session['password'] = password
        print(session)
        return redirect(url_for('home'))
    else:

        # if 'user' in session:
        #     return redirect(url_for('home'))

        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)