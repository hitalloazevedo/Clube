from flask import Flask, render_template
import requests

url = ' https://economia.awesomeapi.com.br/last/{}-BRL'


def pegar_cotacao(moeda:str):
    moeda = moeda.upper().strip()

    response = requests.get(url.format(moeda))
    response_json = response.json()

    preco = str(response_json[f'{moeda}BRL']['bid'])
    preco = f'{preco:.4}'.replace('.', ',')

    
    return preco


def pegar_cotacao_btc():
    response = requests.get(url.format('btc'))
    response_json = response.json()
    preco = str(response_json[f'BTCBRL']['bid'])
    preco = preco.replace('.', ',')
    
    return preco


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
