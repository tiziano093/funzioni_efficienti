# Utilizza un'immagine base di Python 3.8
FROM python:3.8-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il tuo script Python nella directory di lavoro
COPY python.py /app/

# Installa le dipendenze
RUN python -m pip install --upgrade pip && \
    pip install numpy psutil memory_profiler

# Comando per eseguire lo script e reindirizzare l'output in un file log
CMD python python.py > output.log 2>&1 && cat output.log
