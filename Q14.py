def soma_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_recursiva(lista[1:])
    
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(soma_recursiva(minha_lista))