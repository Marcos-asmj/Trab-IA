import json

DADOS = "C:/Users/Marcos/Documents/labs/TrabIA/dados.json"

def encontrar_cargo(tokens):
    cargo = ''

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for token in tokens:
            for dado in dados:
                if token == dado:
                    cargo = token

    return cargo

def iniciar_quem():
    return None

def atuar_quem(tokens, _):
    cargo = encontrar_cargo(tokens)
    pessoas = []

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for dado in dados[cargo]:
            for ano in dado["periodo"]:
                if ano in tokens:
                    pessoas.append(dado["nome"])
        if cargo.lower != "governador":
            print(f"O(s) {cargo}(s) nesse ano foram: ")
            for i in pessoas:
                print(i)
        else: 
            print(f"O(s) {cargo}(es) nesse ano foram: ")
            for i in pessoas:
                print(i)
        
        arquivo_de_dados.close()
