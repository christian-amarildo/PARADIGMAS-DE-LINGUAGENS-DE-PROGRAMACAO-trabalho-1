"""
Questão 9 - Acrescente no programa anterior a técnica de programação dinâmica,
guardando os resultados parciais calculados, a fim de evitar recálculo.
"""

def menor_custo_dinamico(matriz, i=0, j=0, memo=None):
    """
    Encontra o menor custo para percorrer a matriz usando programação dinâmica
    
    Parâmetros:
    - matriz: matriz de custos
    - i: linha atual (começa em 0)
    - j: coluna atual (começa em 0)
    - memo: dicionário para armazenar resultados já calculados
    
    A técnica de programação dinâmica:
    - Antes de calcular, verifica se o resultado já está no memo
    - Após calcular, armazena o resultado no memo
    - Evita recalcular subproblemas já resolvidos
    """
    # Inicializa o dicionário de memoização na primeira chamada
    if memo is None:
        memo = {}
    
    N = len(matriz)      # número de linhas
    M = len(matriz[0])   # número de colunas
    
    # Verifica se já calculamos o resultado para esta posição
    if (i, j) in memo:
        return memo[(i, j)]
    
    # Condição de parada: chegamos ao destino final
    if i == N - 1 and j == M - 1:
        resultado = matriz[i][j]
    
    # Caso especial: última linha (só pode ir para direita)
    elif i == N - 1:
        resultado = matriz[i][j] + menor_custo_dinamico(matriz, i, j + 1, memo)
    
    # Caso especial: última coluna (só pode ir para baixo)
    elif j == M - 1:
        resultado = matriz[i][j] + menor_custo_dinamico(matriz, i + 1, j, memo)
    
    # Caso geral: pode ir para baixo ou direita
    else:
        # Calcula o custo de ir para baixo
        custo_baixo = menor_custo_dinamico(matriz, i + 1, j, memo)
        
        # Calcula o custo de ir para direita
        custo_direita = menor_custo_dinamico(matriz, i, j + 1, memo)
        
        # O resultado é o custo atual mais o menor entre os dois caminhos
        resultado = matriz[i][j] + min(custo_baixo, custo_direita)
    
    # Guarda o resultado calculado no memo antes de retornar
    memo[(i, j)] = resultado
    
    return resultado


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
    
    # Cria o dicionário para armazenar resultados
    memo = {}
    
    print(f"\nMenor custo para percorrer de [0][0] até [{len(matriz)-1}][{len(matriz[0])-1}]:")
    resultado = menor_custo_dinamico(matriz, 0, 0, memo)
    print(f"Custo mínimo: {resultado}")
    
    # Mostra quantas posições únicas foram calculadas
    print(f"\nProgramação Dinâmica - Estatísticas:")
    print(f"Total de posições únicas calculadas: {len(memo)}")
    print(f"Cada posição foi calculada apenas uma vez!")