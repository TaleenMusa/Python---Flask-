from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checkboard():
    return render_template('check.html')


# @app.route('/4')
# def customrows():

#     return render_template('customrows.html')


@app.route('/<x>/<y>')
def customrows2(x, y):
    x = int(x)
    y = int(y)
    return render_template('customrows2.html', horizontal=x, vertical=y)


if __name__ == "__main__":
    app.run(debug=True)
