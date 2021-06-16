from flask import Flask
from post import Post
import os
app = Flask(__name__)

p = Post(os.getenv("TITLE"), os.getenv("CONTENT"))


@app.route("/")
def main():
    return p.json()


if __name__ == "__main__":
    app.run("0.0.0.0")
