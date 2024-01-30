#!/bin/bash

# Esecuzione Periodica di uno Script:
while true; do
    # Tuo codice qui
    sleep 3600  # esegui ogni ora
done

# Automazione del Backup:
tar -czvf backup_$(date +%Y%m%d).tar.gz /path/to/data
echo "Backup eseguito."

# Esegui uno Script ogni Minuto (cron job):
# Aggiungi questa riga al tuo crontab (crontab -e)
# */1 * * * * /path/to/script.sh
echo "Esecuzione programmata ogni minuto."

# Ricerca e Rimuovi File Vecchi in una Directory:
find /path/to/files -type f -mtime +30 -exec rm {} \;
echo "File più vecchi di 30 giorni rimossi."

# Esegui uno Script in Background all'Avvio del Sistema:
# Aggiungi questa riga al tuo crontab o al file /etc/rc.local
# /path/to/script.sh &
echo "Script avviato in background all'avvio del sistema."

# Monitora le Modifiche in una Directory:
inotifywait -m /path/to/watched_directory -e create,delete,modify |
    while read path action file; do
        echo "File $file è stato $action in $path"
    done
echo "Monitoraggio delle modifiche nella directory."

# Esegui un Comando su una Lista di Host SSH:
hosts=("host1" "host2" "host3")
for host in "${hosts[@]}"; do
    ssh "$host" "comando_da_eseguire"
done
echo "Comando eseguito su tutti gli host."

# Genera Backup Incrementali:
backup_dir="/path/to/backup"
rsync -a --link-dest=$backup_dir/backup.$(date -d "yesterday" '+%Y%m%d') /source/ $backup_dir/backup.$(date '+%Y%m%d')
echo "Backup incrementale eseguito."

# Esegui uno Script su una Lista di File:
files=("file1.txt" "file2.txt" "file3.txt")
for file in "${files[@]}"; do
    /path/to/script.sh "$file"
done
echo "Script eseguito su tutti i file della lista."

# Rotazione dei Log Vecchi:
find /var/log -name "*.log" -mtime +7 -exec gzip {} \;
echo "Log più vecchi di una settimana compressi."

# Esegui un Comando con Parametri da un File:
while IFS= read -r line; do
    /path/to/script.sh "$line"
done < parameters.txt
echo "Comando eseguito con parametri da un file."
