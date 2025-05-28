def soma_lista(lst):
    # Condição de parada: lista vazia
    if not lst:
        return 0
    # Chamada recursiva: soma o primeiro elemento e chama a função para o resto da lista
    return lst[0] + soma_lista(lst[1:])

# Teste de uso
lista = [5, 8, 0, 7, 4, 9, 6]
print("Soma dos elementos:", soma_lista(lista))  # Saída esperada: 39