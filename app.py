from flask import Flask,render_template

app = Flask(__name__)

todos = [
    {"sno":1,"title":"sample task","desc":"this is a sample task for todo list","status":"pending"}
]

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=8000)