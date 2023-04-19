from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET"])
def form():
    return render_template("dojo.html")


@app.route('/result', methods=['POST'])
def result():
    name = request.form['your_name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template("result.html",  name=request.form['your_name'], location=request.form['location'],
                        language=request.form['language'], comment=request.form['comment'])


if __name__ == "__main__":
    app.run(debug=True)
