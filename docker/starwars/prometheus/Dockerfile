# Use the official Prometheus image as the base image
FROM prom/prometheus

# Copy the Prometheus configuration file into the container
COPY config.yml /etc/prometheus/

# Set the working directory
WORKDIR /etc/prometheus/

# Expose the Prometheus port
EXPOSE 9090

# Start Prometheus with the custom configuration
CMD ["--config.file=/etc/prometheus/config.yml"]