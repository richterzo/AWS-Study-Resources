FROM python:3-alpine

### ATTENZIONE ###
# Aggiungere i file di requirements e del codice python

# Eseguire il pip install dei requirements ('pip install -r path/to/requirements.txt')

# Utilizzare come entry di esecuzione del container il seguente comando 'python path/to/ds1KyberCannon.py'

# Imposta il lavoro all'interno del container
WORKDIR /app

# Copia i file di requirements e il codice Python nella directory di lavoro
COPY requirements.txt /app/
COPY ds1KyberCannon.py /app/

# Esegui l'installazione dei requirements
RUN pip install --no-cache-dir -r requirements.txt

# Specifica il comando di avvio del container
CMD ["python", "ds1KyberCannon.py"]