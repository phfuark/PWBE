import random

# Lista com 5 valores
valores = [10, 20, 30, 40, 50]

# Sorteando 5 posições únicas dentro do intervalo de 0 a 30
posicoes = random.sample(range(31), len(valores))

# Criando o dicionário que associa os valores às posições sorteadas
resultado = dict(zip(posicoes, valores))

print("Valores sorteados:")
for posicao, valor in resultado.items():
    print(f"Posição: {posicao}, Valor: {valor}")
    