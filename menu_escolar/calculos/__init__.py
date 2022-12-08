from interface import cabecalho, leiafloat, leiaint, inteiro


def PG():
    cabecalho('PROGRESSÃO GEOMÉTRICA')

    a1 = leiafloat('Informe o primeiro termo: ')
    q = leiafloat('Informe a razão: ')
    qtd = leiaint('Até qual termo deseja visualizar?: ')

    soma = 0

    for n in range(1, qtd + 1):
        tg = a1*q**(n-1)
        print(inteiro(tg), end=' -> ')
        soma = soma + tg
    
    print('FIM!')
    print(f'A soma de todos os termos: {inteiro(soma)}')
    print('=' * 60)


def PA():
    cabecalho('PROGRESSÃO ARITIMÉTICA')

    a1 = leiafloat('Informe o primeiro termo: ')
    q = leiafloat('Informe a razão: ')
    qtd = leiaint('Até qual termo deseja visualizar?: ')

    soma = 0

    for n in range(1, qtd+1):
        tg = a1+(n-1)*q
        print(inteiro(tg), end=' -> ')
        soma = soma + tg
    
    print('FIM!')
    print(f'A soma de todos os termos: {inteiro(soma)}')
    print('=' * 60)


def funcao_segundo():
    from math import sqrt

    cabecalho('FUNÇÃO QUADRÁTICA')

    a = leiafloat('Informe o valor de (A): ')
    b = leiafloat('Informe o valor de (B): ')
    c = leiafloat('Informe o valor de (C): ')

    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b+(sqrt(delta)))/2*a
        x2 = (-b-(sqrt(delta)))/2*a

    Xv = -b/(2*a)
    Yv = -delta/(4*a)

    if a > 0:
        concavidade = 'para cima'
    elif a < 0:
        concavidade = 'para baixo'

    print(f'Δ = {inteiro(delta)}')
    if delta > 0:
        print(f'Xi = {inteiro(x1)}')
        print(f'Xii = {inteiro(x2)}')
    print(f'Xv = {inteiro(Xv)}')
    print(f'Yv = {inteiro(Yv)}')
    print(f'Concavidade {concavidade}')
    print('=' * 60)


def funcao_primeiro():
    cabecalho('FUNÇÃO PRIMEIRO GRAU')

    a = leiafloat('Insira um valor para (A): ')
    x = leiafloat('Insira um valor para (X): ')
    b = leiafloat('Insira um valor para (B): ')
    inteiro(a)
    inteiro(x)
    inteiro(b)

    y = (a*x)+b

    print(f'O resultado é {inteiro(y)}')
    print('=' * 60)


def fibonacci():
    cabecalho('FIBONACCI')

    qtd = leiaint('Quantos termos deseja ver?: ')
    t1, t2 = 0, 1
    if qtd == 0:
        print('FIM!')
    elif qtd == 1:
        print('0 -> FIM!')
    elif qtd == 2:
        print('0 -> 1 -> FIM!')
    else:
        print(f'{t1} -> {t2}', end=' -> ')
        for c in range(3, qtd+1):
            t3 = t1 + t2
            t1 = t2
            t2 = t3
            print(f'{t3}', end=' -> ')
        print('FIM!')
    print('=' * 60)


def logaritmo():
    from math import log
    cabecalho('LOGARITMO')

    loga = leiafloat('Informe o valor do Log: ')
    base = leiafloat('Informe o valor da base (B): ')

    print(f'O log de {inteiro(loga)} na base {inteiro(base)} é: {inteiro(log(loga, base))}')
    print('=' * 60)

