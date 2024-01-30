
# Monitoraggio del Sistema

# Visualizza l'Utilizzo della Memoria:
free -h

# Visualizza lo Spazio su Disco:
df -h

# Monitora l'Utilizzo della CPU:
top

# Visualizza Utenti Connessi:
who

# Controllo dello Stato del Servizio:
systemctl status servicename

# Aggiorna Pacchetti di Sistema:
sudo apt update && sudo apt upgrade -y

# Processi

# Elenco dei Processi:
ps aux

# Uccidi un Processo per Nome:
pkill processname

# Monitora l'Utilizzo delle Risorse del Processo:
pidstat 1