def verificar_presenca(lst, elemento):
    # Condição de parada: lista vazia
    if not lst:
        return False
    # Verifica se o primeiro elemento é o desejado
    if lst[0] == elemento:
        return True
    # Chamada recursiva para o resto da lista
    return verificar_presenca(lst[1:], elemento)

# Teste de uso
lista = [5, 8, 0, 7, 4, 9, 6]
elemento = 7
print("Elemento presente?", verificar_presenca(lista, elemento))  # Saída esperada: True

elemento = 10
print("Elemento presente?", verificar_presenca(lista, elemento))  # Saída esperada: False