import speech_recognition as sr
from nltk import word_tokenize, corpus
from qual import *
from quem import *
import json

IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-BR"
CAMINHO_CONFIGURACAO = "C:/Users/Marcos/Documents/labs/TrabIA/config.json"

ATUADORES = [
    {
        "nome": "quem",
        "iniciar": iniciar_quem,
        "parametro_de_atuacao": None,
        "atuar": atuar_quem
    },
    {
        "nome": "qual",
        "iniciar": iniciar_qual,
        "parametro_de_atuacao": None,
        "atuar": atuar_qual
    }
]

def iniciar():
    iniciado = False
    palavras_de_parada = []
    nome_do_assistente = ''
    perguntas = []
    reconhecedor = sr.Recognizer()

    try:    
        nao_parada = {'quem', 'qual'}
        palavras_de_parada = set([word for word in corpus.stopwords.words("portuguese") if word not in nao_parada]) 
        with open(CAMINHO_CONFIGURACAO, "r") as arquivo_de_configuracao:
            configuracao = json.load(arquivo_de_configuracao)

            nome_do_assistente = configuracao["nome"]
            perguntas = configuracao["perguntas"]

            arquivo_de_configuracao.close()

        iniciado = True
    except:
        ...
    
    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["iniciar"]()
        atuador["parametro_de_atuacao"] = parametro_de_atuacao

    return iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, perguntas

def escutar_fala(reconhecedor):
    tem_fala = False

    with sr.Microphone() as fonte_de_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_de_audio)

        print("fale alguma coisa")
        try:
            fala = reconhecedor.listen(fonte_de_audio, timeout = 4)
            tem_fala = True
        except:
            ...

    return tem_fala, fala

def processar_audio_de_teste(audio, reconhecedor):
    tem_transcricao = False

    with sr.AudioFile(audio) as fonte_de_audio:
        fala = reconhecedor.listen(fonte_de_audio)
        try:
            transcricao = reconhecedor.recognize_google(
                fala, language=IDIOMA_FALA)
            tem_transcricao = True
        except:
            ...

    return tem_transcricao, transcricao.lower()

def transcrever_fala(fala, reconhecedor):
    tem_transcricao = False
    
    try:
        transcricao = reconhecedor.recognize_google(fala, language=IDIOMA_FALA)
        tem_transcricao = True
    except:
        ...

    return tem_transcricao, transcricao.lower()

def tokenizar_transcricao(transcricao):
    return word_tokenize(transcricao)

def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_filtrados = []
    
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

def validar_comando(tokens, nome_do_assistente, perguntas):
    valido, pergunta = False, None

    if len(tokens) >= 3:
        if nome_do_assistente == tokens[0]:
            pergunta = tokens[1]

        for pergunta_cadastrada in perguntas:
            if pergunta == pergunta_cadastrada["nome"]:
                valido = True

                break

    return valido, pergunta

def executar_comando(tokens, transcricao):
    for atuador in ATUADORES:
        if tokens[1] == atuador["nome"]:
            atuou = atuador["atuar"](tokens, transcricao)

            if atuou:
                break

if __name__ == "__main__":
    iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, perguntas = iniciar()

    if iniciado:
        while True:
            tem_fala, fala = escutar_fala(reconhecedor)
            if tem_fala:
                tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
                if tem_transcricao:
                    tokens = tokenizar_transcricao(transcricao)
                    tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)

                    valido, pergunta = validar_comando(tokens, nome_do_assistente, perguntas)
                    if valido:
                        executar_comando(tokens, transcricao)
                    else:
                        print("comando inválido, por favor tente novamente")