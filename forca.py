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

while True:
    #mostrar palavra escondida
    print(palavra_escondida)

    #pedir ao jogador uma letra
    letra = input('Digite uma leta: ')

    #verificar se a letra ja foi digitada
    if letra in letras_adivinhadas:
    print('Você já digitou essa letra. Tente outra!')
    continue

    #adicionar letra a lista de letras digitadas
    letras_adivinhadas.append(letra)
    
 
