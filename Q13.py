def is_palindromo_recursivo(palavra):
    palavra = palavra.lower()  
    if not palavra:
        return False
    if len(palavra) <= 1:
        return True  
    elif palavra[0] == palavra[-1]:
        return is_palindromo_recursivo(palavra[1:-1]) 
    else:
        return False  

print(is_palindromo_recursivo("reviver")) 
print(is_palindromo_recursivo("bola"))  
print(is_palindromo_recursivo("ovo"))

