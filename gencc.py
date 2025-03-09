import random
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def gerar_numero():
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])

def gerar_data():
    mes = str(random.randint(1, 12)).zfill(2)
    ano = str(random.randint(2023, 2035))
    return f"{mes}/{ano}"

def gerar_cvc():
    return ''.join([str(random.randint(0, 9)) for _ in range(3)])

def gerar_nome_completo():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        nome = f"{dados['results'][0]['name']['first']} {dados['results'][0]['name']['last']}"
        return nome
    else:
        return "Nome Indisponível"

def gerar_numeros_com_dados(qtd):
    dados = []
    for _ in range(qtd):
        numero = gerar_numero()
        nome_completo = gerar_nome_completo()
        data = gerar_data()
        cvc = gerar_cvc()
        dados.append(f"{numero} | {nome_completo} | {data} | {cvc}")
    return '\n'.join(dados)

def painel():
    print(Fore.GREEN + Style.BRIGHT + "===============================")
    print(Fore.CYAN + "    GERADOR DE CARTÕES VIRTUAIS    ")
    print(Fore.GREEN + Style.BRIGHT + "===============================")
    print(Fore.YELLOW + "Por favor, insira a quantidade de cartões que deseja gerar:")
    qtd = int(input(Fore.MAGENTA + "Quantidade: "))
    
    print(Fore.GREEN + Style.BRIGHT + "\nGerando, aguarde...\n")
    
    numeros_com_dados = gerar_numeros_com_dados(qtd)
    
    print(Fore.GREEN + Style.BRIGHT + "===============================")
    print(Fore.CYAN + f" Cartões Gerados ({qtd}):")
    print(Fore.GREEN + Style.BRIGHT + "===============================")
    print(Fore.WHITE + numeros_com_dados)
    print(Fore.GREEN + Style.BRIGHT + "===============================")

if __name__ == "__main__":
    painel()
