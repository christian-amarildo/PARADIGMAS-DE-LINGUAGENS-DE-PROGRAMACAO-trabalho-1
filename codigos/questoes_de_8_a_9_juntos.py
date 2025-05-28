# Função Recursiva Simples
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

# Função com Programação Dinâmica (Memoização)
def menor_custo_dyn(matriz, i=0, j=0, memo=None):
    if memo is None:
        memo = {}
    
    # Condição de parada: chegamos na célula final
    if i == len(matriz) - 1 and j == len(matriz[0]) - 1:
        return matriz[i][j]
    
    # Verifica se o custo para essa posição já foi calculado
    if (i, j) in memo:
        return memo[(i, j)]
    
    # Condição de parada: se chegamos no final da linha (somente movimento para baixo)
    if i == len(matriz) - 1:
        resultado = matriz[i][j] + menor_custo_dyn(matriz, i, j + 1, memo)
    
    # Condição de parada: se chegamos no final da coluna (somente movimento para a direita)
    elif j == len(matriz[0]) - 1:
        resultado = matriz[i][j] + menor_custo_dyn(matriz, i + 1, j, memo)
    
    # Caso geral: calcular o custo para baixo e para a direita
    else:
        custo_baixo = matriz[i][j] + menor_custo_dyn(matriz, i + 1, j, memo)
        custo_direita = matriz[i][j] + menor_custo_dyn(matriz, i, j + 1, memo)
        resultado = min(custo_baixo, custo_direita)
    
    # Armazena o resultado calculado
    memo[(i, j)] = resultado
    return resultado

# Exemplo de matriz
matriz = [
    [5, 8, 0, 7, 4, 9, 6],
    [3, 1, 3, 1, 6, 1, 4],
    [5, 2, 9, 2, 5, 0, 3],
    [4, 0, 0, 6, 1, 5],
    [0, 9, 0, 8, 4, 9, 3]
]

# Teste de uso para as duas abordagens
print("Resultado com recursão simples:")
print(menor_custo(matriz))  # Saída: Menor custo para percorrer a matriz

print("\nResultado com programação dinâmica (memoização):")
print(menor_custo_dyn(matriz))  # Saída: Menor custo para percorrer a matriz
