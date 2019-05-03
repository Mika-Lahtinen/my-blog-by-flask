from flask import Flask, render_template
app = Flask(__name__)

'''
initialized page
'''
@app.route('/')
def say_Hello():
    return render_template('say_Hello.html')

'''
Initialized page for specified user
'''
@app.route('/user/<name>')
def say_Hello_to_User(name):
    return render_template('say_Hello_to_User.html', user_name=name)
