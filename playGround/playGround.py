from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("playGround.html", boxCount = 3)

@app.route("/play/<boxCount>")
def play2(boxCount):
    boxCount = int(boxCount)
    return render_template("playGround.html", boxCount = boxCount)


@app.route("/play/<boxCount>/<color>")
def play3(boxCount, color):
    boxCount = int(boxCount)
    return render_template("playGround.html", boxCount = boxCount, color = color)


if __name__=="__main__":
    app.run(debug=True)