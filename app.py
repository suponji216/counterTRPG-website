from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('mainpage.html', title='test', main='aa', footer='aaa')


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
