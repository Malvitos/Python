import random

#cria uma lista de palavras que serao sorteadas
palavras = ['python','programacao','computador','internet','disciplina','motherboard','mouse']

#escolher uma das palavras
palavra_sorteada = random.choice(palavras)

#string com as lacunas das letras
palavra_escondida = '*' * len(palavra_sorteada)

#lista vazia para armazenar as letras que ja foram faladas
letras_adivinhadas = []

max_tentativas = 7

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

    #verificar se letra esta na palavra sorteada
    if letra in palavra_sorteada:
        lista = []
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista) #exemplo da letra o digitada = *o***
    
    else: #letra nao esta na palavra sorteada
        max_tentativas -= 1
        print(f'Letra não encontrada! Você tem mais {max_tentativas} tentativas.')

    #verificar se o jogador ganhou ou perdeu
    if palavra_escondida == palavra_sorteada:
        print('Parabens, Você Acertou!!!')
        break
    elif max_tentativas == 0:
        print(f'Você Perdeu. A palavra era {palavra_sorteada}!')
        break
