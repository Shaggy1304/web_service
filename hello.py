from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('hi')
    return '<h1> Hello, my very Friend is working!!!!! <h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    username = int(username) * int(username)
    return 'User %s' % username

@app.route('/avg/<nums>')
def avg(nums):
    nums = nums.split(',')
    print(nums)
    return str(nums)