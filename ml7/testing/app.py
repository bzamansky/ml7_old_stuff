from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "birthdays"

session = {}

@app.route("/")
def home():
    if 'user' in session:
        return render_template("home.html")

    else:
        return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if 'user' in session:
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "swartz" and password == "transformations":
            session['user'] = username

        return redirect("/")


@app.route("/logout")
def logout():
    if 'user' in session:
        print "logging out"
        session.pop('user',None)
        user = None
    return redirect("/login")


@app.route("/<bdaypage>")
def bdaypage(bdaypage=''):
    pages = ['early.html','music.html','pirate.html','space.html',
             'wizard.html','indian.html','halloween.html','taekwondo.html',
             'sports.html','davebusters.html','tech.html','cake.html',
             'casino.html','surfing.html','catan.html']

    if 'user' in session and bdaypage in pages:
            return render_template(bdaypage)

    return redirect("/")

if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0", port = 1995)
