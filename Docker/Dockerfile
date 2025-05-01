FROM ubuntu:latest
LABEL maintainer="yuliet@devops.com"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y cowsay bash
ENTRYPOINT ["/usr/games/cowsay"]
