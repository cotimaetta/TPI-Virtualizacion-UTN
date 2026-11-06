tiempos = []
for numero in range(1, 4):
    tiempo = float(input(f"Ingresá el tiempo {numero} en milisegundos: "))
    tiempos.append(tiempo)
promedio = sum(tiempos) / len(tiempos)
print(f"Tiempo promedio de respuesta: {promedio:.2f} ms")
