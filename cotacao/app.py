from flask import Flask, render_template
from cotacao import pegar_cotacao, pegar_cotacao_btc


app = Flask(__name__)


@app.route("/")
def index():

    usd = pegar_cotacao('usd')
    eur = pegar_cotacao('eur')
    gbp = pegar_cotacao('gbp')
    btc = pegar_cotacao_btc()

    return render_template('index.html', usd=usd, eur=eur, gbp=gbp, btc=btc)


if __name__ == '__main__':
    app.run(debug=False)
