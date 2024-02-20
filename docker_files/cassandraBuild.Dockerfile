# Use the official Cassandra image from Docker Hub
FROM cassandra:latest
# Expose the CQL port
EXPOSE 9042 7000 7001 7001 7199 9160 
# Install additional packages
RUN apt-get update \
    && apt-get install -y \
       tree \
       neovim \
       screen \
       iputils-ping \
       traceroute \
       net-tools \
       dnsutils \
       curl \
       telnet \
       nmap \
       tcpdump \
       iperf 


RUN apt-get update && \
    apt-get install -y     && \
    rm -rf /var/lib/apt/lists/*



# Set the working directory (optional)
WORKDIR /app

# Copy the CQL script to create the user
COPY config_scripts/create_user.cql /app/
COPY config_scripts/entrypoint.sh /app/
# Command to run when the container starts
CMD ["/bin/bash", "/app/entrypoint.sh"]
