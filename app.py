from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://c.tenor.com/gIaioChTOloAAAAC/cat-cute.gif",
    "https://c.tenor.com/GTcT7HODLRgAAAAC/smiling-cat-creepy-cat.gif",
    "https://c.tenor.com/M9xqrmAzMzIAAAAC/smile-cat.gif",
    "https://c.tenor.com/_kqZQY5wX2sAAAAd/orange-cat-smile-cat-smile.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
