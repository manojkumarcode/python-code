from flask.templating import render_template
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    course = request.args["course"]
    rating = request.args.get("rating")
    return {"message": f"{course} with rating {rating}"}

@app.route("/json")
def home2():
    return {"message": "Hello World"}

@app.route("/sample")
def get_sample_html():
    return render_template('sample.html')


if __name__ == "__main__":
    app.run(debug=True)
