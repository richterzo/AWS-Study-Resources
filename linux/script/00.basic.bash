#!/bin/bash
# Questo è uno script shell che illustra alcuni comandi utili su Linux

# Comando per visualizzare la directory corrente
pwd

# Comando per elencare i file e le directory nella directory corrente
ls

# Comando per elencare i file e le directory in formato dettagliato
ls -l

# Comando per navigare in una directory specifica
cd /path/to/directory

# Comando per creare una nuova directory
mkdir new_directory

# Comando per copiare un file o una directory
cp source_file destination_file

# Comando per spostare o rinominare un file o una directory
mv old_file new_file

# Comando per eliminare un file
rm file_to_delete

# Comando per eliminare una directory e tutto il suo contenuto
rm -r directory_to_delete

# Comando per visualizzare il contenuto di un file di testo
cat file_name

# Comando per visualizzare i primi 10 linee di un file di testo
head file_name

# Comando per visualizzare le ultime 10 linee di un file di testo
tail file_name

# Comando per cercare una stringa in un file di testo
grep "search_string" file_name

# Comando per visualizzare i processi in esecuzione sul sistema
ps aux

# Comando per visualizzare i dettagli del sistema
uname -a

# Comando per visualizzare lo spazio su disco utilizzato e disponibile
df -h

# Comando per visualizzare le informazioni sulla memoria
free -m

# Comando per elencare le interfacce di rete
ifconfig

# Comando per visualizzare la tabella di routing
route -n

# Comando per pingare un indirizzo IP per verificare la connettività di rete
ping -c 4 google.com

# Comando per controllare le connessioni di rete attive
netstat -tuln

# Comando per cambiare le autorizzazioni di un file o una directory
chmod permissions file_or_directory

# Comando per cambiare il proprietario di un file o una directory
chown owner:group file_or_directory

# Comando per comprimere un file o una directory
tar -czvf archive_name.tar.gz file_or_directory

# Comando per estrarre un file compresso
tar -xzvf archive_name.tar.gz

# Comando per visualizzare l'elenco dei processi in esecuzione
top

# Comando per terminare un processo
kill process_id
