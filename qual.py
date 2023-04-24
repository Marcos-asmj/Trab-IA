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

def encontrar_nome(frase, cargo):
    nome = ''

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for dado in dados[cargo]:
            if dado["nome"].casefold() in frase.casefold():
                nome = dado["nome"]

    if nome == '':
        print(f"Não encontrei nenhum {cargo} com esse nome.")

    return nome

def iniciar_qual():
    return None

def atuar_qual(tokens, transcricao):
    cargo = encontrar_cargo(tokens)
    nome = encontrar_nome(transcricao, cargo)

    with open(DADOS, encoding='utf-8') as arquivo_de_dados:
        dados = json.load(arquivo_de_dados)
        for dado in dados[cargo]:
            if nome.casefold() == dado["nome"].casefold():
                print(f"{dado['nome']} foi {cargo} no(s) ano(s): {dado['periodo']}.")
        arquivo_de_dados.close()
