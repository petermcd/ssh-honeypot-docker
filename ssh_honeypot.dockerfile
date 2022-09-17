FROM ubuntu

RUN apt update; \
    apt upgrade; \
    apt -y install git; \
    git clone https://github.com/PeterMcD/honeypot-installer.git; \
    cd ./honeypot-installer; \
    chmod +x ./install.sh; \
    ./install.sh; \
    apt remove -y git gcc; \
    apt clean; \
    useradd sshd;

EXPOSE 22/tcp
EXPOSE 22/udp

ENTRYPOINT /usr/sbin/sshd && tail -f /dev/null
