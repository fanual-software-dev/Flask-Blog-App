from flask import Flask,redirect,render_template,url_for,request,session,jsonify
from datetime import timedelta
from pymongo import MongoClient
from models import BlogSchema
import arrow

app = Flask(__name__)
client = MongoClient('mongodb+srv://asfawfanual2003:ur27imml69oBttLM@mernapp.f2gvrng.mongodb.net/?retryWrites=true&w=majority&appName=Mernapp')
db = client['test']
collection = db['blogs']
app.secret_key = 'FanBun'
# app.permanent_session_lifetime = timedelta(days=3)

@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/createBlog',methods=['POST'])
def createBlog():
    data = request.get_json()
    if data:
        blog = BlogSchema(
            data.get('title'),
            data.get('main'),
            data.get('image'),
            data.get('numberOfLikes'),
            data.get('createdAt')

        )
        blog.save()
        if blog.inserted_id:
            return redirect(url_for('blogs'))
        return f'<p>Opps somthing went wrong</p>'
    return f'<p>Opps somthing went wrong</p>'

@app.route('/blogs',methods = ['GET','POST'])
def blogs():

    resources = list(collection.find({}))
    formated_resource = []
    for blog in resources:
        created_at = arrow.get(blog['createdAt'])
        formatted_time = created_at.humanize()
        blog['createdAt'] = formatted_time
        formated_resource.append(blog)
    blogs = formated_resource[::-1]
    return render_template('blogs.html',blogs = blogs)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/user')
def users():
    if 'user' in session and 'password' in session:
        # user = session['user']
        # password = session['password']
        return render_template('user.html')

@app.route('/', methods = ["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # session.permanent = True
        session['user'] = user
        session['email'] = email
        session['password'] = password
        print(session)
        return redirect(url_for('home'))
    else:

        # if 'user' in session:
        #     return redirect(url_for('home'))

        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)