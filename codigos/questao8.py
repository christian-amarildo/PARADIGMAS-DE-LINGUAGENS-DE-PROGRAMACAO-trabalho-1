"""
Questão 8 - Fazer um programa que resolva o problema do menor custo
para percorrer a matriz desde M[0][0] até M[N-1][N-1]
Movimentos possíveis: para baixo e para a direita (quando possível)
"""

def menor_custo(matriz, i=0, j=0):
    """
    Encontra o menor custo para percorrer a matriz de [0][0] até [N-1][M-1]
    
    Parâmetros:
    - matriz: matriz de custos
    - i: linha atual (começa em 0)
    - j: coluna atual (começa em 0)
    
    Condições de parada identificadas:
    1. Chegamos na célula final M[N-1][M-1]
    2. Estamos na última linha (só podemos ir para direita)
    3. Estamos na última coluna (só podemos ir para baixo)
    
    Casos especiais de chamada recursiva:
    - Posição intermediária: duas chamadas recursivas (baixo e direita)
    - Borda inferior: apenas uma chamada recursiva (direita)
    - Borda direita: apenas uma chamada recursiva (baixo)
    """
    N = len(matriz)      # número de linhas
    M = len(matriz[0])   # número de colunas
    
    # Condição de parada: chegamos ao destino final
    if i == N - 1 and j == M - 1:
        return matriz[i][j]
    
    # Caso especial: última linha (só pode ir para direita)
    if i == N - 1:
        return matriz[i][j] + menor_custo(matriz, i, j + 1)
    
    # Caso especial: última coluna (só pode ir para baixo)
    if j == M - 1:
        return matriz[i][j] + menor_custo(matriz, i + 1, j)
    
    # Caso geral: pode ir para baixo ou direita
    # Calcula o custo de ir para baixo
    custo_baixo = menor_custo(matriz, i + 1, j)
    
    # Calcula o custo de ir para direita
    custo_direita = menor_custo(matriz, i, j + 1)
    
    # Retorna o custo atual mais o menor entre os dois caminhos
    return matriz[i][j] + min(custo_baixo, custo_direita)


# Programa principal
if __name__ == "__main__":
    # Matriz do problema
    matriz = [
        [5, 8, 0, 7, 4, 9, 6],
        [3, 1, 3, 6, 1, 3, 4],
        [5, 2, 9, 2, 5, 0, 3],
        [8, 4, 0, 0, 6, 1, 5],
        [0, 9, 0, 8, 4, 9, 3]
    ]
    
    print("Matriz de custos:")
    for linha in matriz:
        print(linha)
    
    print(f"\nMenor custo para percorrer de [0][0] até [{len(matriz)-1}][{len(matriz[0])-1}]:")
    resultado = menor_custo(matriz)
    print(f"Custo mínimo: {resultado}")