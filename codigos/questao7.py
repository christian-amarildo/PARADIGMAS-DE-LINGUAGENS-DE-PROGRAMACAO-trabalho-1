def soma_pares(lst):
    # Condição de parada: lista vazia
    if not lst:
        return 0
    # Se o primeiro elemento for par, soma com a chamada recursiva
    if lst[0] % 2 == 0:
        return lst[0] + soma_pares(lst[1:])
    # Caso contrário, apenas chama a recursão para o resto da lista
    return soma_pares(lst[1:])

# Teste de uso
lista = [5, 8, 0, 7, 4, 9, 6]
print("Soma dos números pares:", soma_pares(lista))  # Saída esperada: 18 (8 + 0 + 4 + 6)