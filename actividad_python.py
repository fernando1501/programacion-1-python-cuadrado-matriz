# Programación I: datos del estudiante y cuadrado con una matriz.

nombres = "Fernando Alonso"
apellidos = "Núñez Famanía"
carrera = "Administración de Sistemas"
lado = 8

print("DATOS DEL ESTUDIANTE")
print("Nombres:", nombres)
print("Apellidos:", apellidos)
print("Carrera:", carrera)

# Crear una matriz de lado x lado con espacios en su interior.
matriz = [[" " for columna in range(lado)] for fila in range(lado)]

# Colocar asteriscos en la primera y última fila y columna.
for fila in range(lado):
    for columna in range(lado):
        if (fila == 0 or fila == lado - 1
                or columna == 0 or columna == lado - 1):
            matriz[fila][columna] = "*"

print()
print("CUADRADO CON ASTERISCOS")
for fila in matriz:
    print(" ".join(fila))
