def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[-1]

    menores = [x for x in lista[:-1] if x <= pivo]
    maiores = [x for x in lista[:-1] if x > pivo]

    return quicksort(menores) + [pivo] + quicksort(maiores)

lista = [3, 4, 100, 6, 8, 10, 32, 76, 1, 2, 68]
print(quicksort(lista))