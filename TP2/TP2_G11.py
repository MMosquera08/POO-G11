lista = [9, 5, 7, 3, 4, 1, 6, 2, 8]
lista_ordenada = 0
posible_menor = 0
for k in range(len(lista)):
    for i in range(len(lista)):
        if list(i) > list(i+1):
            posible_menor = list(i+1)
        else:
            posible_menor = i
    lista_ordenada.append(posible_menor)
    lista.pop(posible_menor)
print(lista_ordenada)