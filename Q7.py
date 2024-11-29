def quickselect(lista, k):
    if len(lista) == 1:
        return lista[0]

    pivo = lista[-1]

    menores = [x for x in lista[:-1] if x <= pivo]
    maiores = [x for x in lista[:-1] if x > pivo]

    i_pivo = len(menores)

    # Verificar onde está o k-ésimo elemento
    if k == i_pivo:
        return pivo
    elif k < i_pivo:
        return quickselect(menores, k)
    else:
        return quickselect(maiores, k - i_pivo - 1)
    
lista = [10, 4, 5, 8, 6, 11, 26, 7]
k = 0
print(f"O {k + 1}-ésimo menor elemento é: {quickselect(lista, k)}")