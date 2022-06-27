from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '73e2bea5c8fb763ea86d0aecbcdd6fe7'

posts = [
    {
        'author': 'Avi Paul',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '19 June 2022'
    },
    {
        'author': 'Avi Paul',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': '20 June 2022'

    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Registration', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)