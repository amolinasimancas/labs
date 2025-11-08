def media_movil(valores, ventana):
    if ventana > 1 and ventana <= len(valores):
        medias_moviles = []
        operaciones = len(valores) - ventana + 1
        for i in range(operaciones):
            medias_moviles.append(sum(valores[i:i+ventana])/ventana)
        return medias_moviles
    else:
        print("¡Fuera de rango!")

print(media_movil([10, 20, 30, 40, 50], 1))
print(media_movil([10, 20, 30, 40, 50], 2))
print(media_movil([10, 20, 30, 40, 50], 3)) # [20.0, 30.0, 40.0]
print(media_movil([10, 20, 30, 40, 50], 4))
print(media_movil([10, 20, 30, 40, 50], 5))
print(media_movil([10, 20, 30, 40, 50], 6))

# Solución
'''
def media_movil(valores, ventana):
    return [sum(valores[i:i+ventana]) / ventana for i in range(len(valores) - ventana + 1)]
'''