# Import the flask class and create an instance of it
from flask import Flask, render_template

app = Flask(__name__)

# Define a route and view function
@app.route('/')
def index():
    return render_template('index.html', name='Flask Demos')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us', description='Template example with multiple strings passed to it.')

@app.route('/fruits')
def fruits():
    fruit_list  = ["apple", "banana", "cherry"]
    return render_template('fruits.html', title='List Example', fruits = fruit_list)

@app.route('/profile')
def show_profile():
    user = {"name": "Alice", "age": 30}
    return render_template("profile.html", title='Dictionary Example', user=user)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)