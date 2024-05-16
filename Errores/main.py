# Errores en Python

try:
    print(10/"x")
except TypeError as e:
    print("ERROR EN EL SISTEMA - TIPO", e)
except ZeroDivisionError as ex:
    print("ERROR EN EL SISTEMA - DIVISION", ex)
finally:
    print("Sigue Intentando")