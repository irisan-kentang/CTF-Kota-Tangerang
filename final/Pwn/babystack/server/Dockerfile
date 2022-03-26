FROM i386/ubuntu:18.04

RUN apt update && apt install socat -y

EXPOSE 5000
WORKDIR /challs
COPY files /challs/

# Securing files
RUN chown -R root:root /challs/

# Securing environ
RUN chmod 700 /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/sh /bin/dash /bin/bash /bin/cat /usr/bin/groups /usr/bin/id /bin/ls
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./babystack2,su=nobody
