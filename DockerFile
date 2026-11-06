FROM python:3.12-slim
WORKDIR /app
COPY tiempos_respuesta.py .
CMD ["python", "tiempos_respuesta.py"]
