import unittest
from assistente_virtual import *

CHAMANDO_ERRADO = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_nome_errado.wav"
CHAMANDO_MARIA = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_quem_presidente.wav"
QUAL_PRESIDENTE = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_quem_presidente.wav"
QUAL_GOVERNADOR = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_quem_governador.wav"
QUAL_PREFEITO = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_quem_prefeito.wav"
QUEM_PRESIDENTE = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_qual_presidente.wav"
QUEM_GOVERNADOR = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_qual_governador.wav"
QUEM_PREFEITO = "C:/Users/Marcos/Documents/labs/TrabIA/audios/teste_qual_prefeito.wav"

class TesteNomeAssistente(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, _, self.nome_do_assistente, _ = iniciar()

    def testar_01_reconhecer_nome(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CHAMANDO_MARIA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)
        self.assertEqual(tokens[0], self.nome_do_assistente)

    def testar_02_nao_reconhecer_outro_nome(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CHAMANDO_ERRADO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)
        self.assertNotEqual(tokens[0], self.nome_do_assistente)

class TesteQuem(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.perguntas = iniciar()

    def testar_quem_presidente(self):
        tem_transcricao, transcricao = processar_audio_de_teste(QUEM_PRESIDENTE, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, = validar_comando(tokens, self.nome_do_assistente, self.perguntas)
        self.assertTrue(valido)

    def testar_quem_governador(self):
        tem_transcricao, transcricao = processar_audio_de_teste(QUEM_GOVERNADOR, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, = validar_comando(tokens, self.nome_do_assistente, self.perguntas)
        self.assertTrue(valido)
    
    def testar_quem_prefeito(self):
        tem_transcricao, transcricao = processar_audio_de_teste(QUEM_PREFEITO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, = validar_comando(tokens, self.nome_do_assistente, self.perguntas)
        self.assertTrue(valido)

class TesteQual(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.perguntas = iniciar()

    def testar_qual_presidente(self):
        tem_transcricao, transcricao = processar_audio_de_teste(QUAL_PRESIDENTE, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, = validar_comando(tokens, self.nome_do_assistente, self.perguntas)
        self.assertTrue(valido)

    def testar_qual_governador(self):
        tem_transcricao, transcricao = processar_audio_de_teste(QUAL_GOVERNADOR, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, = validar_comando(tokens, self.nome_do_assistente, self.perguntas)
        self.assertTrue(valido)
    
    def testar_qual_prefeito(self):
        tem_transcricao, transcricao = processar_audio_de_teste(QUAL_PREFEITO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, = validar_comando(tokens, self.nome_do_assistente, self.perguntas)
        self.assertTrue(valido)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteQuem))
    testes.addTest(carregador.loadTestsFromTestCase(TesteQual))

    executor = unittest.TextTestRunner()
    executor.run(testes)
