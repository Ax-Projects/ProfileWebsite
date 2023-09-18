from flask import Flask, redirect, render_template
# import os, signal

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return redirect(location="/index.html", code=301)


@app.route("/index.html", methods=["GET"])
def index():
    return render_template("index.html")

# @app.route("/stop_server")
# def stop_server():
#     os.kill(os.getpid(), signal.CTRL_C_EVENT)
#     return "Server stopped"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)