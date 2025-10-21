def contar_palabras(texto):
    lista_palabras = texto.lower().split()
    palabras_unicas = list(set(lista_palabras))
    palabras_unicas.sort()
    repeticiones = []
    for palabra_unica in palabras_unicas:
        contador = 0
        for palabra in lista_palabras:
            if palabra == palabra_unica:
                contador += 1
        repeticiones.append(contador)
    return {palabra:repeticion for (palabra,repeticion) in zip(palabras_unicas,repeticiones)}

print(contar_palabras("Hola hola mundo mundo mundo")) # {'hola': 2, 'mundo': 3}

# Respuesta
'''
def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    return conteo
'''