from flask import Flask, render_template, redirect, url_for, request, flash, get_flashed_messages
from package.AccountForms import FormCreateAccount, FormLogin, FormUpdateAccount, FormDeleteAccount, PostsForm
from package import app
from package import bcrypt
from package import db
from package.database_model import User, Posts
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if current_user.is_authenticated:
        print("Authenticated")
        return redirect(url_for('home'))
    form = FormCreateAccount()
    #print("Test")
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
                    username=form.username.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=form.email.data).first()
        flash('Account Created Successfully!')
        login_user(user)
        return redirect(url_for('home'))

    return render_template("CreateAccount.html", form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    #print(str(form.remember_me.data) + " before authenticated if statement.")
    if current_user.is_authenticated:
        #print("Authenticated")
        flash('You are already logged in!')
        return redirect(url_for('home'))
    if form.validate_on_submit():
        #print("Login Successful!")
        user = User.query.filter_by(email=form.email.data).first()
        #print(user)
        #check_password = bcrypt.check_password_hash(user.password, form.password.data)

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Successful Login!')
            #print("After log in")
            login_user(user, remember=form.remember_me.data)
            #form.remember_me.data = True
            #print(form.remember_me.data)
            if form.remember_me.data is not None:
                form.remember_me.data = True
                print(str(form.remember_me.data) + " after not none if statement")
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful login!  Check Username and password!')
            #print("Unsuccessful login check email and password.")
            return redirect(url_for('login'))
    return render_template("LoginAccount.html", form=form)

@app.route('/logout')
def logout():
    form = FormLogin()
    form.remember_me.data = False;
    print(form.remember_me.data)
    logout_user()
    return redirect(url_for('login'))

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        select_options = request.form['select']
        select_language = request.form['language_select']
        if select_options == "Data Structures" and select_language == 'None':
            return redirect(url_for('data_structures'))
        elif select_options == "Databases" and select_language == 'None':
            return redirect(url_for('databases'))
        elif select_options == "Graphics" and select_language == 'None':
            return redirect(url_for('graphics'))
        elif select_options == "Data Structures" and select_language == "SQL":
            flash('SQL does not support Data Structures.  Select a different language!', 'success')
            return redirect(url_for('home'))#redirect home because no one does data structures in sql
        elif select_options == "Databases" and select_language == 'SQL':
            return redirect(url_for('sql_database'))
        elif select_options == "Graphics" and select_language == 'SQL':
            flash('SQL does not support graphics.  Select a different language!')
            return redirect(url_for('home'))#redirect home because no one does graphics in sql
        elif select_options == "Data Structures" and select_language == "Python":
            return redirect(url_for('python_ds'))
        elif select_options == "Data Structures" and select_language == "Java":
            return redirect(url_for('java_ds'))
        elif select_options == "Data Structures" and select_language == "C++":
            return redirect(url_for('c_plus_plus_ds'))
        elif select_options == "Databases" and select_language == "Python":
            return redirect(url_for('python_db'))
        elif select_options == "Databases" and select_language == "Java":
            return redirect(url_for('java_db'))
        elif select_options == "Databases" and select_language == "C++":
            return redirect(url_for('c_plus_plus_db'))
        elif select_options == "Graphics" and select_language == "Python":
            return redirect(url_for('python_graphics'))
        elif select_options == "Graphics" and select_language == "Java":
            return redirect(url_for('java_graphics'))
        elif select_options == "Graphics" and select_language == "C++":
            return redirect(url_for('c_plus_plus_graphics'))


    return render_template("Home.html", form=request.form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = FormUpdateAccount()
    delete_form = FormDeleteAccount()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    if delete_form.validate_on_submit():
        db.session.delete(current_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('Account.html', form=form, delete_form=delete_form)

@app.route('/community', methods=['GET', 'POST'])
@login_required
def community():
    for u in User.query.filter_by(email=current_user.email):
        postForm = PostsForm()
        user = User.query.filter_by(id=u.id).first()
        if postForm.validate_on_submit():
            new_user_post = Posts(post=postForm.post.data)
            new_user_post.user = user
            db.session.add(new_user_post)
            db.session.commit()
            return redirect(url_for('community', postForm=postForm))
    if request.method == 'POST':
        print("Post validated.")
        form = request.form['select_post']
        if form == 'newPost':
            for user1 in User.query.filter_by(email=current_user.email):
                return redirect(url_for('new_post', id=user1.id))
        elif form == 'myPosts':
            for user1 in User.query.filter_by(email=current_user.email):
                return redirect(url_for('my_posts', id=user1.id))
    posts_list = []
    user_list = []
    for posts in Posts.query.all():
        posts_list.append(posts)
    for users in User.query.all():
        user_list.append(users)
    return render_template("Community/Community.html", posts_list=posts_list, user_list=user_list, postForm=postForm)
@app.route('/new_post<id>', methods=['GET', 'POST'])
@login_required
def new_post(id):
    form = PostsForm()
    user = User.query.filter_by(id=id).first()
    if form.validate_on_submit():
        new_user_post = Posts(post=form.post.data)
        new_user_post.user = user
        db.session.add(new_user_post)
        db.session.commit()
        return redirect(url_for('community', form=form))
    return render_template("Community/NewPost.html", form=form)
@app.route('/my_posts<id>', methods=['GET', 'POST'])
@login_required
def my_posts(id):
    post_list = []
    user = User.query.filter_by(id=id).first()
    print(user)#successfully printing correct user!
    for posts in user.posts:
        post_list.append(posts)
        print(posts)
    return render_template("Community/MyPosts.html", post_list=post_list)

@app.route('/delete/<id>')
@login_required
def delete_post(id):
    deletePost = Posts.query.filter_by(id=id).first()
    print(deletePost)
    db.session.delete(deletePost)
    db.session.commit()
    return redirect(url_for("community"))