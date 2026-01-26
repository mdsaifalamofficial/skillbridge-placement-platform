from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    marks = request.form["marks"]

    return f"Hello {name}, your marks are {marks}"

if __name__ == "__main__":
    app.run(debug=True)
# feature branch backend logic test
