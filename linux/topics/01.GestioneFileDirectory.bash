#!/bin/bash

# Gestione dei File e delle Directory

# Copia di un File o una Directory:
cp -r source_directory destination_directory

# Rinominare File in Batch:
for file in *.txt; do
    mv "$file" "${file%.txt}_new.txt"
done

# Elimina File Vecchi:
find /path/to/files -type f -mtime +7 -exec rm {} \;

# Conteggio delle Linee di un File:
if [ -f "$1" ]; then
    lines=$(wc -l < "$1")
    echo "Il file $1 ha $lines linee."
else
    echo "Il file $1 non esiste."
fi

# Ricerca di File per Nome:
find /path/to/search -name "filename"

# Estrai Contenuto di un Archivio:
tar -xvf archive.tar.gz -C /path/to/extract

# Trova i File di una Certa Estensione in una Directory:
find /path/to/directory -type f -name "*.txt"
echo "File con estensione .txt trovati nella directory."

# Calcola la Dimensione Totale di una Directory:
total_size=$(du -sh /path/to/directory | cut -f1)
echo "La dimensione totale della directory è $total_size."

# Concatena Contenuto di File in un Nuovo File:
cat file1.txt file2.txt > merged_file.txt
echo "File1.txt e file2.txt sono stati concatenati in merged_file.txt."

# Trova e Sostituisci Testo in Tutti i File di una Directory:
find /path/to/directory -type f -exec sed -i 's/vecchio/nuovo/g' {} +
echo "Testo 'vecchio' sostituito con 'nuovo' in tutti i file."

# Archivia una Directory in un File Tar:
tar -czvf archive.tar.gz /path/to/directory
echo "Directory archiviata in archive.tar.gz."

# Elimina File con Estensione Specifica più Vecchi di una Settimana:
find /path/to/files -type f -name "*.log" -mtime +7 -exec rm {} \;
echo "File con estensione .log più vecchi di una settimana eliminati."

# Copia Solo i File Nuovi o Modificati in un'altra Directory:
rsync -a --update /source/directory/ /destination/directory/
echo "File nuovi o modificati copiati nella directory di destinazione."

# Crea una Struttura di Directory Basata su un File di Configurazione:
while IFS= read -r line; do
    mkdir -p "$line"
done < directories_config.txt
echo "Struttura di directory creata in base al file di configurazione."

# Trova File Duplicati in una Directory:
find /path/to/directory -type f -exec md5sum {} + | sort | uniq -w32 -d
echo "File duplicati trovati nella directory."

# Rinomina Ricorsivamente i File con un Nuovo Prefisso:
find /path/to/directory -type f -name "*.jpg" -exec rename 's/^/nuovo_prefisso_/' {} \;
echo "File con estensione .jpg rinominati con un nuovo prefisso."
