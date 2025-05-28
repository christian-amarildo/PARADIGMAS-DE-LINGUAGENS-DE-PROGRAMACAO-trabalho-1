def inverter_lista(lst):
    # Condição de parada: lista vazia
    if not lst:
        return []
    # Chamada recursiva para inverter o resto da lista e adicionar o primeiro elemento no final
    return inverter_lista(lst[1:]) + [lst[0]]

# Teste de uso
lista = [5, 8, 0, 7, 4, 9, 6]
print("Lista invertida:", inverter_lista(lista))  # Saída esperada: [6, 9, 4, 7, 0, 8, 5]