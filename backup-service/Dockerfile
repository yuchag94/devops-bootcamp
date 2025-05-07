FROM ubuntu:22.04

# Instalar cron y mysql-client
RUN apt-get update && apt-get install -y cron mysql-client

# Crear carpeta para scripts
RUN mkdir -p /scripts

# Copiar el script de respaldo y dar permisos
COPY respaldo-diario.sh /scripts/respaldo-diario.sh
RUN chmod +x /scripts/respaldo-diario.sh

# Copiar el archivo de tareas de cron
COPY crontab.txt /etc/cron.d/respaldo-cron

# Dar permisos y aplicar crontab
RUN chmod 0644 /etc/cron.d/respaldo-cron && \
    crontab /etc/cron.d/respaldo-cron

# Crear log de cron
RUN touch /var/log/cron.log

# Iniciar cron al arrancar el contenedor
CMD cron && tail -f /var/log/cron.log
