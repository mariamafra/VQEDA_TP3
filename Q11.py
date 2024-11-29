import sys
import traceback

def fatorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n-1)

try:
    print(f"Limite de recursão: {sys.getrecursionlimit()}")
    print(fatorial_recursivo(1500))

except RecursionError as e:
    traceback.print_exc()

# def fatorial_iterativo(n):
#     resultado = 1
#     for i in range(1, n + 1):
#         resultado *= i
#     return resultado

# print(fatorial_iterativo(1500)) 