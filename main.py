from flask import Flask, render_template



app = Flask(__name__)


@app.route("/")
def principal():
    frutas = ["Morango", "Uva", "Abacate", "Banana", "Pera", "Maça", "Abacaxi"]
    return render_template("index.html", frutas=frutas)


@app.route('/sobre')
def sobre():
    notas = {"Marco":9.0, "Paulo":7.5, "Claudia": 8.4, "Vilma":6.9}
    return render_template('sobre.html', notas=notas)


if __name__ == "__main__":
    app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

