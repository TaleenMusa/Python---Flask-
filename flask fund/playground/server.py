
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play/<x>/<color>')
def play(x , color):
    return render_template("index.html", num=int(x), col=color)


if __name__ == "__main__":   
    app.run(debug=True)    # Run the app in debug mode.
