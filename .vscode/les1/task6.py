from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/students/')
def students():
    _students = [
        {"name": "jon",
         "surname": "doe",
         "age": 22,
         "average": 34},
        {"name": "jon",
         "surname": "doe",
         "age": 22,
         "average": 92},

    ]
    context = {'students': _students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run()
