def sumar_pares(numeros):
    suma_pares = sum([numero for numero in numeros if numero % 2 == 0])
    return suma_pares

print(sumar_pares([1, 2, 3, 4, 5, 6]))  # debería devolver 12

# Solución:
'''
def sumar_pares(numeros):
    return sum(x for x in numeros if x % 2 == 0)
'''