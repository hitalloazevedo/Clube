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
    preco = float(preco)
    preco = f'{preco:.3f}'
    preco = preco.replace('.', ',')

    return preco


def date():
    req = requests.get('https://economia.awesomeapi.com.br/last/usd')

    date = req.json()['USDBRL']['create_date']
    
    return date

app = Flask(__name__)


@app.route("/")
def index():
    usd = pegar_cotacao('usd')
    eur = pegar_cotacao('eur')
    gbp = pegar_cotacao('gbp')
    btc = pegar_cotacao_btc()

    data = date()

    return render_template('index.html', usd=usd, eur=eur, gbp=gbp, btc=btc, date=data)


if __name__ == '__main__':
    app.run(debug=False)
