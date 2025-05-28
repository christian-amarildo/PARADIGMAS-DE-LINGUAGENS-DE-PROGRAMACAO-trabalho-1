def menor_custo(matriz, i=0, j=0):
    # Condição de parada: chegamos na célula final
    if i == len(matriz) - 1 and j == len(matriz[0]) - 1:
        return matriz[i][j]
    
    # Condição de parada: se chegamos no final da linha (somente movimento para baixo)
    if i == len(matriz) - 1:
        return matriz[i][j] + menor_custo(matriz, i, j + 1)
    
    # Condição de parada: se chegamos no final da coluna (somente movimento para a direita)
    if j == len(matriz[0]) - 1:
        return matriz[i][j] + menor_custo(matriz, i + 1, j)

    # Caso geral: calcular o custo para baixo e para a direita
    custo_baixo = matriz[i][j] + menor_custo(matriz, i + 1, j)
    custo_direita = matriz[i][j] + menor_custo(matriz, i, j + 1)
    
    # Retorna o menor custo entre os dois movimentos possíveis
    return min(custo_baixo, custo_direita)

# Exemplo de uso com a matriz fornecida
matriz = [
    [5, 8, 0, 7, 4, 9, 6],
    [3, 1, 3, 1, 6, 1, 4],
    [5, 2, 9, 2, 5, 0, 3],
    [4, 0, 0, 6, 1, 5],
    [0, 9, 0, 8, 4, 9, 3]
]

print(menor_custo(matriz))  # Saída: menor custo para percorrer a matriz
