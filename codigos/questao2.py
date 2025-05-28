def contar_elementos(lst):
    # Condição de parada: lista vazia
    if not lst:
        return 0
    # Chamada recursiva: conta o primeiro elemento e chama para o resto da lista
    return 1 + contar_elementos(lst[1:])

# Teste de uso
lista = [5, 8, 0, 7, 4, 9, 6]
print("Número de elementos:", contar_elementos(lista))  # Saída esperada: 7