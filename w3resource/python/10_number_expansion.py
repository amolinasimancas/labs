n = input("Inserte el número a expandir: ")
e = int(input ("Inserte los niveles a expandir: "))

resultado = sum([int(i * n) for i in range(1, e+1)])

print(resultado)

# OTRA SOLUCIÓN

# Prompt the user to input an integer and store it in the variable 'a'
a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer

# Calculate the sum of 'n1', 'n2', and 'n3' and print the result
print(n1 + n2 + n3)