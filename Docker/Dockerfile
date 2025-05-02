FROM ubuntu:latest

LABEL maintainer="yuliet@devops.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y bash

COPY script-logica.sh /script-logica.sh

RUN chmod +x /script-logica.sh

CMD ["/script-logica.sh"]
