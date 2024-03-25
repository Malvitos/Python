from math import pow

def compoosto(capital, juros, tempo):
    return capital*pow((1+juros),tempo)

capital = float('Qual o capital de investimento?\n')
juros = float('Qual o juros anual em porcentagem (%)?\n')
tempo = int('Quantos meses de investimento?\n')

juros = juros / 100 
tempo = tempo / 12

valor_final_composto = composto(capital, juros, tempo)
print(f'O montante final será de: {valor_final_composto}.')
print(f'O juros do rendimento foram de: {valor_final_composto - capital}.')


