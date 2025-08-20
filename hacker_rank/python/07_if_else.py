import math
import os
import random
import re
import sys

n = int(input("Ingrese un número entero: ").strip())

if n >= 1 and n <= 100:
    print("El número ingresado es válido.")
    if n % 2 != 0:
        print("Weird")

    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")

    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")

    elif n % 2 == 0 and n > 20:
        print("Not Weird")
else:
    print("El número ingresado no es válido.")
