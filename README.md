# Trabajo Práctico Integrador — Virtualización con VirtualBox

**Materia:** Arquitectura y Sistemas Operativos  
**Carrera:** Tecnicatura Universitaria en Programación — UTN  
**Estudiante:** María Constanza Maetta

## Descripción

El trabajo consistió en crear una máquina virtual con Ubuntu Desktop 24.04.5 LTS en Oracle VirtualBox sobre Windows. Para comprobar el funcionamiento del entorno, se ejecutó un programa en Python que calcula el promedio de tres tiempos de respuesta simulados. El programa se ejecutó directamente en Ubuntu y dentro de un contenedor Docker, con los mismos datos de prueba en ambos entornos.

## Contenido

- `TPI_Virtualizacion_Maetta.pdf`: informe con la configuración de la máquina virtual, la instalación de Ubuntu y los resultados de la práctica.
- `tiempos_respuesta.py`: código fuente del programa.
- `Dockerfile`: instrucciones para construir la imagen Docker del programa.
- `documentacion - imagenes/`: evidencias del procedimiento y de la ejecución.

## Video explicativo

[Ver video en YouTube](https://youtu.be/m0Bc7JTn0iA)

## Ejecución del programa

Desde la terminal de Ubuntu, ubicarse en la carpeta que contiene el archivo y ejecutar:

```bash
python3 tiempos_respuesta.py
```

Para reproducir la prueba del informe, ingresar `120`, `150` y `180`, presionando Enter después de cada valor. El resultado esperado es `Tiempo promedio de respuesta: 150.00 ms`.

La prueba se realizó con Python 3.12.3.

## Ejecución con Docker

Desde la terminal de Ubuntu, con Docker instalado, ubicarse en la carpeta que contiene el `Dockerfile` y `tiempos_respuesta.py`. Construir la imagen y ejecutar el contenedor:

```bash
sudo docker build -t tiempos-respuesta:1.0 .
sudo docker run --rm -it tiempos-respuesta:1.0
```

Ingresar `120`, `150` y `180`, presionando Enter después de cada valor. El resultado esperado es `Tiempo promedio de respuesta: 150.00 ms`, igual que en la ejecución directa en Ubuntu.
