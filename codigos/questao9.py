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

# Exemplo de uso com a matriz fornecida
print(menor_custo_dyn(matriz))  # Saída: menor custo com memoização
