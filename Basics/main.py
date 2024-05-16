#print("Hello World")

# Variable

"""
texto = "Esto es un String"
year = 2020

print(f"{texto} {str(year)}")
print(texto + " " + str(year))
"""

# Entrada

"""
dato = input("Ingrese dato: ")
print(f"Este es el valor ingresado: {dato} ")
"""

# Condicional y Funcion

"""
var_altura = int(input("Ingrese Altura: "))
def mostrarAltura(altura):
    resultado = ""
    if altura >= 170:
        resultado = "Persona alta"
    else:
        resultado = "Persona Bajita"

    return resultado

print(mostrarAltura(var_altura))

"""

# Listas

"""
personas = ["Victor", "Paco", "Pepe"]
#print(personas[0])

for persona in personas:
    print("-" + persona)
"""

# Modulo

import modulo
var_altura = int(input("Ingrese Altura: "))
print(modulo.mostrarAltura(var_altura))


