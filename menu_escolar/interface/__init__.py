import os

def menu(*opcoes):
    c = 1
    for o in opcoes:
        print(f'0{c} - {o}')
        c += 1
    
    print('99 - SAIR')
    
    opcao = leiaint('Informe sua opção: ')
    return opcao


def cabecalho(msg:str, tam=60, simb='='):
    print(simb * tam)
    print(msg.center(tam))
    print(simb * tam)


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor insira um valor inteiro!') 
        else:
            return valor


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor insira um valor válido!') 
        else:
            return valor


def inteiro(n : float):
    if n.is_integer():
        n = int(n)
        return n
   
    else:
        n = f'{n:.2f}'
        return n


def resposta():
    res = str(input('Deseja realizar calcular novamente? [S/N]: ')).lower().strip()
    if res != '':
        res = res[0]
    
    while res == '':
        print('Opção inválida!')
        res = str(input('Deseja realizar calcular novamente? [S/N]: ')).lower().strip()
        while res not in 'sn':
            print('Opção inválida!')
            res = str(input('Deseja realizar calcular novamente? [S/N]: ')).lower().strip()
            if res != '':
                res = res[0]

    return res


def limpar():
    nome_so = os.name
    if nome_so == 'nt':
        os.system('cls')
    else:
        os.system('clear')
