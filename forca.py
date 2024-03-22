import random

#cria uma lista de palavras que serao sorteadas
palavras = ['python','programacao','computador','internet','disciplina','motherboard','mouse']

#escolher uma das palavras
palavra_sorteada = random.choice(palavras)

#string com as lacunas das letras
palavra_escondida = '-' * len(palavra_sorteada)

#lista vazia para armazenar as letras que ja foram faladas
letras_adivinhadas = []

max_tentativas = 6

