from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://c.tenor.com/gIaioChTOloAAAAC/cat-cute.gif",
    "https://c.tenor.com/GTcT7HODLRgAAAAC/smiling-cat-creepy-cat.gif",
    "https://c.tenor.com/M9xqrmAzMzIAAAAC/smile-cat.gif",
    "https://c.tenor.com/_kqZQY5wX2sAAAAd/orange-cat-smile-cat-smile.gif",
    "https://c.tenor.com/h5wYby96KJsAAAAd/cat-love-ahzix.gif",
    "https://c.tenor.com/dur8_lWhH2cAAAAC/crazy-cat-dancing-crazy-cat.gif",
    "https://c.tenor.com/ZhfMGWrmCTcAAAAC/cute-kitty-best-kitty.gif",
    "https://c.tenor.com/ujI068l1JL4AAAAC/sassy-cats.gif",
    "https://c.tenor.com/YjeDKHDpa6gAAAAd/cool-cat.gif",
    "https://c.tenor.com/4VY0Ykn4lN4AAAAd/cat-broken-cat.gif",
    "https://c.tenor.com/2T506UHvonMAAAAC/pirate-cat.gif",
    "https://c.tenor.com/oTeBa4EVepMAAAAC/business-cat-working.gif",
    "https://c.tenor.com/tMRY35MWfYYAAAAd/funny-silly.gif",
    "https://c.tenor.com/QAN9RxLUSxUAAAAC/cat-cute.gif",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
