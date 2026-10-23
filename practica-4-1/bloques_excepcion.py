# Ejercicio: Practica el uso de bloques de excepción.
try:
    numero = int(input("Número: "))
except ValueError:
    print("Entrada no numérica.")
else:
    print("Número aceptado:", numero)
finally:
    print("Finalizó el intento de lectura.")
