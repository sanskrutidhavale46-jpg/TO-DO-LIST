from flask import Flask,render_template

app = Flask(__name__)

todos = [
    {"sno":1,"title":"HomeWork","desc":"Complete All Assignments","date_created":"08-08-2026","status":"pending"}
]

@app.route("/")
def home():
    return render_template("index.html",allTodos = todos)


if __name__ == "__main__":
    app.run(debug=True,port=8000)