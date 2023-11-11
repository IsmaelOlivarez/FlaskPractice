from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dynamic')
def dynamic():
    greeting = "Man I sure do love flask web development"
    friends = ['bob', 'john', 'kayla', 'jeremy']
    return render_template('dynamic.html', greeting=greeting, friends = friends)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')