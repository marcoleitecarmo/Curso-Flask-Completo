from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def principal():
    return render_template("index.html")


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
