# Condicionales
edad = 10
if edad >= 18 and edad < 21:
	print("Puedes conducir")
elif edad >= 21:
    print("Puedes tomar alcohol")
else:
	print("Eres menor de edad")

# Métodos de Strings
texto = "Lorem ipsum dolor sit Amem"
palabra = "lorem"

print(palabra in texto)

if palabra in texto:
    print("Palabra encontrada")

print(texto.upper())
print(texto.lower())
print(texto.count("o"))
print(texto.swapcase())
