def filtrar_diccionario(diccionario, umbral):
    return {clave:valor for(clave,valor) in diccionario.items() if valor > umbral}

print(filtrar_diccionario({'a': 3, 'b': 8, 'c': 1}, 4)) # {'b': 8}

# Respuesta
'''
def filtrar_diccionario(d, k):
    return {clave: valor for clave, valor in d.items() if valor > k}
'''