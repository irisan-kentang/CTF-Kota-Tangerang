FROM ubuntu:18.04

RUN apt update && apt install socat -y

COPY files /challs/

RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/sh /bin/bash /bin/dash /bin/cat /usr/bin/groups /usr/bin/id /bin/ls
RUN chown root:root -R /challs

WORKDIR /challs

EXPOSE 5000
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./babyrop2,su=nobody
