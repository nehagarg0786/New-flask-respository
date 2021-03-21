from app import app 
from flask import Flask, render_template, request, jsonify,flash, redirect , session, make_response 
from app import login_manager
from flask_login import  login_user, logout_user, login_required
from .models import User , Blog,db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/main') #blank URL
def main():
    return render_template("main.html")


@app.route('/') #blank URL
def index():
#print(f'ENV is set to: {app.config["ENV"]}')
#    app.config["SECRET_KEY"] = "iuhto743yto34iuho287gh78"
#    print(app.config["SECRET_KEY"])
    #data = Blog.query.all()
    #print(data)
        
    # if current_user.is_anonymous:
    #    return render_template("index.html")
    # else:
    #     currentUser=current_user.username
    #     print(currentUser)
    #     results=db.session.query(Blog).join(User).filter(User.username == currentUser).all()
        # return render_template("index.html", results=results)
    return render_template("index.html")#,data=data)

@app.route('/login', methods=['GET','POST']) #error-__init__() got an unexpected keyword argument 'method'(s is missing)
def login():
    if request.method=='POST':
        req = request.get_json()
        uname= req.get('uname')
        password= req.get('password')
        user = User.query.filter_by(username=uname).first()
        if user and password ==user.password:
            login_user(user)
            res = make_response(jsonify(req), 200)
            return res
        # print(uname)
        # print(password)
        #user = User.query.filter_by(username=uname).first()
        #blog = Blog.query.filter(blog.user==User.id).first()
        # if user and password ==user.password:
        #     login_user(user)
        
        # uname= request.form.get('uname')
        # password= request.form.get('password')
        # user = User.query.filter_by(username=uname).first()
     
        #blog = Blog.query.filter(blog.user==User.id).first()
        # if user and password ==user.password:
        #     #print(blog)
        #     login_user(user)
        #     return redirect('/')
        # else:
        #     flash('Invalid Credentials', 'danger')
        #     return redirect('/login')


    return render_template("login.html")

@app.route('/register', methods=['GET','POST']) 
def register():
    if request.method=='POST':
        req = request.get_json()
        email= req.get('email')
        password= req.get('password')
        fname= req.get('fname')
        lname= req.get('lname')
        uname= req.get('uname')
        user = User(username=uname, email=email, fname=fname, lname=lname, password=password)
        db.session.add(user)
        db.session.commit()
        res = make_response(jsonify(req), 200)
        return res
        # user = User.query.filter_by(username=uname).first()
        
        # if user and password ==user.password:
        #     flash('User already exist')
        #     return redirect('/login')
        # else:
        #     user = User(username=uname, email=email, fname=fname, lname=lname, password=password)
        #     db.session.add(user)
        #     db.session.commit()
        #     flash('user has been registered successfully', 'success')
        #     return redirect('/login')


    return render_template("register.html") 
     #error- "GET /register HTTP/1.1" 200 -
    #resolved- try different browser

@app.route('/logout') #blank URL
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/blogpost', methods=['GET','POST']) #blank URL
@login_required
def blogpost():
    if request.method=='POST':
        req = request.get_json()
        title = req.get('title')
        content= req.get('content')
        #uname= req.get('uname')
        # title = request.form.get('title')
        # content= request.form.get('content')
        #currentUser=current_user.username
        #user = User.query.filter_by(username=currentUser).first()
        #print(user)
        blog = Blog(title=title,content=content)
        db.session.add(blog)
        db.session.commit()
        res = make_response(jsonify(req), 200)
        return res
        
        #flash("Your post has been submitted successfully", 'success')
        # return redirect ('/')

    return render_template('blog.html')
@app.route("/blog_detail/<int:id>", methods=['GET','POST']) #blank URL
def blogdetail(id):
    blog = Blog.query.get(id)
    return render_template('blog_detail.html', blog=blog)

@app.route("/delete/<int:id>", methods=['GET','POST']) #blank URL
def delete_post(id):
    blog = Blog.query.get(id)
    req = request.get_json()
    db.session.delete(blog)
    db.session.commit()
    res = make_response(jsonify(req), 200)
    return res
    #return req
    #flash("Post has been deleted, Success")
    #return redirect('/')


@app.route("/edit/<int:id>", methods=['GET','PUT']) #blank URL
def edit_post(id):
    blog = Blog.query.get(id)
    if request.method=='PUT':
        blog = Blog.query.get(id)
        print(blog)
        req = request.get_json()
        blog.title = req.get('title')
        blog.content= req.get('content')
        db.session.commit()
        res = make_response(jsonify(req), 200)
        return res
        #db.session.commit()
        # flash("Post has been updated, Success")
        # return redirect('/')
    return render_template('edit.html',blog=blog)

   