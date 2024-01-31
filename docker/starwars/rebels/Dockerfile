FROM python:3-alpine

### ATTENZIONE ###
# Aggiungere i file di requirements e del codice python

# Eseguire il pip install dei requirements ('pip install -r path/to/requirements.txt')

# Utilizzare come entry di esecuzione del container il seguente comando 'python path/to/bases.py'

# https://docs.docker.com/engine/reference/builder/

# Imposta il lavoro di lavoro all'interno del container
WORKDIR /app

# Aggiungi i file di requirements e del codice Python nella directory di lavoro
COPY requirements.txt /app/
COPY bases.py /app/

# Esegui l'installazione dei requirements
RUN pip install --no-cache-dir -r requirements.txt

# Utilizza come entry point del container il comando 'python path/to/bases.py'
CMD ["python", "bases.py"]