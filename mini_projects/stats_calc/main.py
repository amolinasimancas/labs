if __name__ == '__main__':
    import statistics

    print('Bienvenido a calculadora estadística!')
    datos = input('Ingrese los valores a procesar separados por un espacio, al finalizar presione Enter: ')
    lista_texto = datos.split()
    lista_numero = [float(elemento) for elemento in lista_texto]
    media = statistics.mean(lista_numero)
    mediana = statistics.median(lista_numero)
    desviacion = statistics.stdev(lista_numero)
    
    print('Los estadísticos descriptivos de los valores ingresados son:')
    print('Media: ', media)
    print('Mediana: ', mediana)
    print('Desviación Estándar: ', round(desviacion,2))