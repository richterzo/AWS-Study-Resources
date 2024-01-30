#!/bin/bash

# Networking

# Test di Connettività con Ping:
ping -c 4 example.com
echo "Test di connettività con example.com."

# Scansione delle Porte su un Host:
nmap -p- target_ip
echo "Scansione delle porte aperte su target_ip."

# Visualizza le Informazioni sull'Interfaccia di Rete:
ifconfig
echo "Informazioni sull'interfaccia di rete."

# Visualizza le Connessioni di Rete:
netstat -an
echo "Connessioni di rete attive."

# Analisi del Traffico di Rete:
tcpdump -i eth0
echo "Monitoraggio del traffico di rete in corso su eth0."


# Mostra gli indirizzi IP delle interfacce di rete:
ip addr show
echo "Indirizzi IP delle interfacce di rete."

# Trova l'indirizzo IP pubblico dell'host:
curl ifconfig.me
echo "Indirizzo IP pubblico dell'host."

# Visualizza le route di rete:
ip route show
echo "Route di rete."

# Configura un server DNS personalizzato:
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "Server DNS configurato su 8.8.8.8."

# Monitora il traffico di rete in tempo reale:
tcpdump -i eth0
echo "Monitoraggio del traffico di rete in corso su eth0."

# Mostra le informazioni dell'interfaccia di rete:
ifconfig
echo "Informazioni sull'interfaccia di rete."

# Cambia l'indirizzo MAC di un'interfaccia di rete:
sudo ifconfig eth0 hw ether 00:11:22:33:44:55
echo "Indirizzo MAC di eth0 cambiato."
