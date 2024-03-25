from math import pow

def composto(capital, juros, tempo):
    return capital*pow((1+juros),tempo)

def simples(capital, juros, tempo):
    return capital*juros*tempo

capital = float('Qual o capital de investimento?\n')
juros = float('Qual o juros anual em porcentagem (%)?\n')
tempo = int('Quantos meses de investimento?\n')

juros = juros / 100 
tempo = tempo / 12

valor_final_composto = composto(capital, juros, tempo)
print(input(f'O montante final será de: {valor_final_composto:.02f}R$'))
print(input(f'O juros do rendimento foram de: {(valor_final_composto - capital):.02f}R$'))

valor_final_simples = simples(capital, juros, tempo)
print(f'O montante final será de {(valor_final_simples + capital):.02f}R$')