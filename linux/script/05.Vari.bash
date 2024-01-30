#!/bin/bash

# Gestione Utenti da un File CSV:
while IFS=, read -r username password; do
    useradd -m -p $(openssl passwd -1 "$password") "$username"
    echo "Utente $username creato con successo."
done < users.csv

# Altro

# Genera una Password Casuale:
random_password=$(openssl rand -base64 12)
echo "Password casuale generata: $random_password"

# Esegui uno Script con Privilegi di Amministratore:
if [ "$EUID" -ne 0 ]; then
    echo "Eseguire come amministratore (root)."
    exit 1
fi

# Resto dello script

# Verifica la Presenza di un Comando:
command_to_check="git"
if command -v "$command_to_check" &> /dev/null; then
    echo "$command_to_check è installato."
else
    echo "$command_to_check non è installato."
fi

# Vari

# Genera un Numero Casuale:
random_number=$((RANDOM % 100))
echo "Numero casuale generato: $random_number"

# Conversione di Caratteri Maiuscoli/Minuscoli:
text="Testo in maiuscolo"
lowercase_text=$(echo "$text" | tr '[:upper:]' '[:lower:]')
echo "Convertito in minuscolo: $lowercase_text"

# Calcolatrice Bash:
echo "Inserisci l'espressione matematica:"
read expr
result=$(echo "scale=2; $expr" | bc)
echo "Risultato: $result"
