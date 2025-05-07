FROM ubuntu

RUN apt-get update && \
    apt-get install -y mysql-client bash && \
    rm -rf /var/lib/apt/lists/*

COPY script-logica.sh /script-logica.sh
RUN chmod +x /script-logica.sh

CMD ["/script-logica.sh"]
