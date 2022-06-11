from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'secretkey' # set a secret key for security purposes

@app.route("/")
def render_home():
    session['count'] += 1
    return render_template("index.html")

@app.route("/count", methods=['POST'])
def start_counting():
    session['count'] += 1
    return redirect("/count")

@app.route("/count_by_two", methods=['POST'])
def count_by_two():
    session['count'] += 2
    return redirect("/count_by_two")

@app.route("/count")
@app.route("/count_by_two")
def display_count():
    return render_template("index.html")

@app.route("/destroy_session", methods=['POST'])
def clear_count():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)