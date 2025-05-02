FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y mysql-client bash && \
    rm -rf /var/lib/apt/lists/*

COPY script-logica.sh /script-logica.sh
RUN chmod +x /script-logica.sh

ENTRYPOINT ["/script-logica.sh"]
