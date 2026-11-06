# Lista para almacenar los tres tiempos de respuesta simulados.
tiempos = []

# Solicitar tres valores y convertir cada entrada a un número decimal.
for numero in range(1, 4):
    tiempo = float(input(f"Ingresá el tiempo {numero} en milisegundos: "))

    # Agregar el valor ingresado a la lista.
    tiempos.append(tiempo)

# Calcular el promedio de los tiempos almacenados.
promedio = sum(tiempos) / len(tiempos)

# Mostrar el promedio con dos decimales y su unidad.
print(f"Tiempo promedio de respuesta: {promedio:.2f} ms")
