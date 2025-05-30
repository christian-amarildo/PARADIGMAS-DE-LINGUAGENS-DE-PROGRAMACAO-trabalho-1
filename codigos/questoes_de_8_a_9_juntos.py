"""
Comparação entre Solução Recursiva (Q8) e Programação Dinâmica (Q9)
Este código executa ambas as soluções e mostra as diferenças de performance
"""

import time
import sys

# Aumenta o limite de recursão para matrizes maiores
sys.setrecursionlimit(10000)

class MetricasRecursiva:
    def __init__(self):
        self.chamadas = 0
        self.tempo_por_posicao = {}
    
    def incrementar(self):
        self.chamadas += 1

class MetricasDinamica:
    def __init__(self):
        self.chamadas = 0
        self.cache_hits = 0
        self.calculos_reais = 0

# Instâncias globais para métricas
metricas_recursiva = MetricasRecursiva()
metricas_dinamica = MetricasDinamica()

def menor_custo_recursiva(matriz, i=0, j=0):
    """Solução recursiva pura (Questão 8)"""
    metricas_recursiva.incrementar()
    
    N, M = len(matriz), len(matriz[0])
    
    if i == N - 1 and j == M - 1:
        return matriz[i][j]
    
    if i == N - 1:
        return matriz[i][j] + menor_custo_recursiva(matriz, i, j + 1)
    
    if j == M - 1:
        return matriz[i][j] + menor_custo_recursiva(matriz, i + 1, j)
    
    custo_baixo = menor_custo_recursiva(matriz, i + 1, j)
    custo_direita = menor_custo_recursiva(matriz, i, j + 1)
    
    return matriz[i][j] + min(custo_baixo, custo_direita)

def menor_custo_dinamica(matriz, i=0, j=0, memo=None):
    """Solução com programação dinâmica (Questão 9)"""
    if memo is None:
        memo = {}
    
    metricas_dinamica.chamadas += 1
    
    if (i, j) in memo:
        metricas_dinamica.cache_hits += 1
        return memo[(i, j)]
    
    metricas_dinamica.calculos_reais += 1
    
    N, M = len(matriz), len(matriz[0])
    
    if i == N - 1 and j == M - 1:
        return matriz[i][j]
    
    if i == N - 1:
        resultado = matriz[i][j] + menor_custo_dinamica(matriz, i, j + 1, memo)
    elif j == M - 1:
        resultado = matriz[i][j] + menor_custo_dinamica(matriz, i + 1, j, memo)
    else:
        custo_baixo = menor_custo_dinamica(matriz, i + 1, j, memo)
        custo_direita = menor_custo_dinamica(matriz, i, j + 1, memo)
        resultado = matriz[i][j] + min(custo_baixo, custo_direita)
    
    memo[(i, j)] = resultado
    return resultado

def executar_comparacao():
    # Matriz do problema
    matriz = [
        [5, 8, 0, 7, 4, 9, 6],
        [3, 1, 3, 6, 1, 3, 4],
        [5, 2, 9, 2, 5, 0, 3],
        [8, 4, 0, 0, 6, 1, 5],
        [0, 9, 0, 8, 4, 9, 3]
    ]
    
    print("=" * 70)
    print("COMPARAÇÃO ENTRE SOLUÇÕES RECURSIVA E DINÂMICA")
    print("=" * 70)
    print(f"\nMatriz: {len(matriz)} linhas x {len(matriz[0])} colunas")
    
    # Executar solução recursiva
    print("\n" + "─" * 70)
    print("🔄 EXECUTANDO SOLUÇÃO RECURSIVA (Questão 8)...")
    metricas_recursiva.chamadas = 0
    inicio = time.time()
    resultado_recursivo = menor_custo_recursiva(matriz)
    tempo_recursivo = (time.time() - inicio) * 1000
    
    print(f"✓ Concluído!")
    print(f"  • Resultado: {resultado_recursivo}")
    print(f"  • Chamadas recursivas: {metricas_recursiva.chamadas:,}")
    print(f"  • Tempo de execução: {tempo_recursivo:.4f} ms")
    
    # Executar solução dinâmica
    print("\n" + "─" * 70)
    print("💾 EXECUTANDO SOLUÇÃO DINÂMICA (Questão 9)...")
    metricas_dinamica.chamadas = 0
    metricas_dinamica.cache_hits = 0
    metricas_dinamica.calculos_reais = 0
    memo = {}
    inicio = time.time()
    resultado_dinamico = menor_custo_dinamica(matriz, 0, 0, memo)
    tempo_dinamico = (time.time() - inicio) * 1000
    
    print(f"✓ Concluído!")
    print(f"  • Resultado: {resultado_dinamico}")
    print(f"  • Total de chamadas: {metricas_dinamica.chamadas:,}")
    print(f"  • Cálculos únicos: {metricas_dinamica.calculos_reais}")
    print(f"  • Cache hits: {metricas_dinamica.cache_hits}")
    print(f"  • Tempo de execução: {tempo_dinamico:.4f} ms")
    
    # Análise comparativa
    print("\n" + "═" * 70)
    print("📊 ANÁLISE COMPARATIVA")
    print("═" * 70)
    
    # Verificar se os resultados são iguais
    print(f"\n✅ Verificação de correção:")
    print(f"   Ambos algoritmos retornaram o mesmo resultado? {'SIM' if resultado_recursivo == resultado_dinamico else 'NÃO'}")
    print(f"   Valor: {resultado_recursivo}")
    
    # Métricas de performance
    print(f"\n📈 Métricas de Performance:")
    reducao_chamadas = ((metricas_recursiva.chamadas - metricas_dinamica.chamadas) / metricas_recursiva.chamadas) * 100
    print(f"   • Redução no número de chamadas: {reducao_chamadas:.1f}%")
    print(f"   • Fator de redução: {metricas_recursiva.chamadas / metricas_dinamica.chamadas:.1f}x")
    
    # Tempo
    if tempo_dinamico > 0:
        speedup = tempo_recursivo / tempo_dinamico
        print(f"\n⏱️  Tempo de Execução:")
        print(f"   • Speedup: {speedup:.1f}x mais rápido")
        print(f"   • Economia de tempo: {tempo_recursivo - tempo_dinamico:.4f} ms")
    
    # Eficiência do cache
    print(f"\n💾 Eficiência do Cache (Programação Dinâmica):")
    taxa_cache = (metricas_dinamica.cache_hits / metricas_dinamica.chamadas) * 100 if metricas_dinamica.chamadas > 0 else 0
    print(f"   • Taxa de cache hit: {taxa_cache:.1f}%")
    print(f"   • Posições únicas calculadas: {len(memo)}")
    print(f"   • Economia de cálculos: {metricas_recursiva.chamadas - metricas_dinamica.calculos_reais:,}")
    
    # Complexidade
    print(f"\n🔍 Análise de Complexidade:")
    print(f"   ┌─────────────────┬──────────────────────┬──────────────────────┐")
    print(f"   │     Aspecto     │   Recursiva (Q8)     │   Dinâmica (Q9)      │")
    print(f"   ├─────────────────┼──────────────────────┼──────────────────────┤")
    print(f"   │ Temporal        │ O(2^(n+m))           │ O(n×m)               │")
    print(f"   │ Espacial        │ O(n+m) - pilha       │ O(n×m) - memo        │")
    print(f"   │ Chamadas        │ {metricas_recursiva.chamadas:>20,} │ {metricas_dinamica.chamadas:>20,} │")
    print(f"   │ Recálculos      │ Muitos               │ Nenhum               │")
    print(f"   └─────────────────┴──────────────────────┴──────────────────────┘")
    
    # Conclusão
    print(f"\n💡 CONCLUSÃO:")
    print(f"   A programação dinâmica é {speedup:.0f}x mais rápida e faz {reducao_chamadas:.0f}% menos chamadas!")
    print(f"   Isso ocorre porque cada subproblema é calculado apenas uma vez e armazenado.")
    
    # Teste com matriz maior
    print(f"\n🔬 TESTE ADICIONAL - Matriz Maior (6x8):")
    matriz_maior = [
        [5, 8, 0, 7, 4, 9, 6, 2],
        [3, 1, 3, 6, 1, 3, 4, 5],
        [5, 2, 9, 2, 5, 0, 3, 1],
        [8, 4, 0, 0, 6, 1, 5, 7],
        [0, 9, 0, 8, 4, 9, 3, 2],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ]
    
    # Apenas solução dinâmica para matriz maior (recursiva seria muito lenta)
    metricas_dinamica.chamadas = 0
    metricas_dinamica.calculos_reais = 0
    memo_maior = {}
    inicio = time.time()
    resultado_maior = menor_custo_dinamica(matriz_maior, 0, 0, memo_maior)
    tempo_maior = (time.time() - inicio) * 1000
    
    print(f"   • Resultado: {resultado_maior}")
    print(f"   • Chamadas (dinâmica): {metricas_dinamica.chamadas}")
    print(f"   • Tempo: {tempo_maior:.4f} ms")
    print(f"   • Estimativa recursiva: ~{2**(6+8):,} chamadas (impraticável!)")

if __name__ == "__main__":
    executar_comparacao()