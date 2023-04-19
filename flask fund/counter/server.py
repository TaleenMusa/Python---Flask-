from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it safe !'


@app.route('/')
def counter():

    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('counter.html', x=session['count'])


@app.route('/destroy_session')
def destroySession():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
