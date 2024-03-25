import random

numero_minimo = int(input('Qual o número mínimo do intervalo?\n'))
numero_maximo = int(input('Qual o número máximo do intervalo?\n'))

tentativas = int(input('Quantas tentativas para acertar?\n'))

numero_sorteado = random.randint(numero_minimo, numero_maximo)

while True:
    tentativa = int(input(f'Digite um número entre {numero_minimo} e {numero_maximo}.\n'))

    if tentativa == numero_sorteado:
        print('Parabéns Você Acertou!')
        break
    else: tentativas -= 1
    if tentativas == 0:
        print(f'Você Perdeu! O número correto era {numero_sorteado}')
        break
    else: 
        print(f'Numero Errado! Tente Novamente. Você ainda tem {tentativas} tentativas.')