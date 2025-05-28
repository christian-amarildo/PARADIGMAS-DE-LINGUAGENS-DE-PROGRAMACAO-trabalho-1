def soma_lista(lst):
    if not lst:
        return 0
    return lst[0] + soma_lista(lst[1:])

def contar_elementos(lst):
    if not lst:
        return 0
    return 1 + contar_elementos(lst[1:])

def verificar_presenca(lst, elemento):
    if not lst:
        return False
    if lst[0] == elemento:
        return True
    return verificar_presenca(lst[1:], elemento)

def verificar_posicao(lst, elemento, pos=0):
    if not lst:
        return -1
    if lst[0] == elemento:
        return pos
    return verificar_posicao(lst[1:], elemento, pos + 1)

def maximo_elemento(lst):
    if len(lst) == 1:
        return lst[0]
    resto_maximo = maximo_elemento(lst[1:])
    return lst[0] if lst[0] > resto_maximo else resto_maximo

def inverter_lista(lst):
    if not lst:
        return []
    return inverter_lista(lst[1:]) + [lst[0]]

def soma_pares(lst):
    if not lst:
        return 0
    if lst[0] % 2 == 0:
        return lst[0] + soma_pares(lst[1:])
    return soma_pares(lst[1:])

# Testes
lista = [5, 8, 0, 7, 4, 9, 6]

print("Soma dos elementos:", soma_lista(lista))  # Saída esperada: 39
print("Número de elementos:", contar_elementos(lista))  # Saída esperada: 7
print("Elemento 7 presente?", verificar_presenca(lista, 7))  # Saída esperada: True
print("Elemento 10 presente?", verificar_presenca(lista, 10))  # Saída esperada: False
print("Posição do elemento 7:", verificar_posicao(lista, 7))  # Saída esperada: 3
print("Posição do elemento 10:", verificar_posicao(lista, 10))  # Saída esperada: -1
print("Maior elemento:", maximo_elemento(lista))  # Saída esperada: 9
print("Lista invertida:", inverter_lista(lista))  # Saída esperada: [6, 9, 4, 7, 0, 8, 5]
print("Soma dos números pares:", soma_pares(lista))  # Saída esperada: 18 (8 + 0 + 4 + 6)
