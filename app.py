"""
CP1404 - Practical 10
Flask Test App
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"{celsius} C converts to {fahrenheit} F\n" \
           f"<h2>Now that's useful :D</h2>"


if __name__ == '__main__':
    app.run()
