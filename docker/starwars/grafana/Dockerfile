# Use the official Grafana image as the base image
FROM grafana/grafana

# Copia il file JSON nella directory /etc/grafana/provisioning/dashboards/ della tua immagine
COPY dashboards/starwars.json /etc/grafana/provisioning/dashboards/

# Expose the Grafana port
EXPOSE 3000

# Start Grafana
CMD ["grafana-server"]
