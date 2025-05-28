def verificar_posicao(lst, elemento, pos=0):
    # Condição de parada: lista vazia
    if not lst:
        return -1
    # Verifica se o primeiro elemento é o desejado
    if lst[0] == elemento:
        return pos
    # Chamada recursiva para o resto da lista, com a posição incrementada
    return verificar_posicao(lst[1:], elemento, pos + 1)

# Teste de uso
lista = [5, 8, 0, 7, 4, 9, 6]
elemento = 7
print("Posição do elemento:", verificar_posicao(lista, elemento))  # Saída esperada: 3

elemento = 10
print("Posição do elemento:", verificar_posicao(lista, elemento))  # Saída esperada: -1