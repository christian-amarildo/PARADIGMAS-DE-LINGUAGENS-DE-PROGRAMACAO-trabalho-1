def maximo_elemento(lst):
    # Condição de parada: lista com um único elemento
    if len(lst) == 1:
        return lst[0]
    # Chamada recursiva para o resto da lista
    resto_maximo = maximo_elemento(lst[1:])
    # Retorna o maior entre o primeiro elemento e o máximo do resto
    return lst[0] if lst[0] > resto_maximo else resto_maximo

# Teste de uso
lista = [5, 8, 0, 7, 4, 9, 6]
print("Maior elemento:", maximo_elemento(lista))  # Saída esperada: 9