from flask import Flask, render_template, request, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/terms')
def terms():
    return render_template("terms.html")


@app.route('/policy')
def policy():
    return render_template("policy.html")


@app.route('/care')
def care():
    return render_template("care.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/flowerpot')
def flowerpot():
    return render_template("flowerpot.html")


@app.route('/ashtray')
def ashtray():
    return render_template("ashtray.html")


@app.route('/chess')
def chess():
    return render_template("chess.html")


@app.route('/lamp')
def lamp():
    return render_template("lamp.html")


@app.route('/sale')
def sale():
    return render_template("sale.html")


@app.route('/save_response', methods=["POST"])
def save_response():
    with open("mails.txt", "a") as write_email:
        print(request.form)
        write_email.write(request.form["email_data"] + "\n")

        return Response("successful")


if __name__ == '__main__':
    app.run(debug=True)
