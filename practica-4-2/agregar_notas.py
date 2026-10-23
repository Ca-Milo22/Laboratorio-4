# Ejercicio: Permite agregar notas a un archivo.
with open("notas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Una observación adicional\n")
