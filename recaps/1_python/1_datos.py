texto = "texto"
entero = 1
decimal = 3.14
booleano = True

print(type(texto))
print(type(entero))
print(type(decimal))
print(type(booleano))

print(type(str(entero)))
print(type(int(decimal)))
print(type(str(booleano)))

lista = [1,2,3,4,5,6,7,8,9]
diccionario = {
    'nombre': 'Antonio',
    'apellido': 'Molina',
    'edad': 38,
    'casado': True,
    'estatura': 1.75
}
conjunto = {1,2,3,4,5}
tupla = (1,2,3,4,5)

print(type(lista))
print(type(diccionario))
print(type(conjunto))
print(type(tupla))

print(lista[2:])
print(diccionario['casado'])