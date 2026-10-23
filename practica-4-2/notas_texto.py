# Ejercicio: Gestiona notas de texto en archivos.
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera observación\n")
    archivo.write("Segunda observación\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
