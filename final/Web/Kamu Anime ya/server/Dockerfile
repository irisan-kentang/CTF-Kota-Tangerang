FROM httpd:2.4.49-buster
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
RUN apt update -y
RUN apt install php7.3-cli php7.3-curl -y
RUN apt install libapache2-mod-php7.3 -y
RUN a2enmod php7.3
RUN a2enmod rewrite

ADD entry.sh /entry.sh
ADD 000-default.conf /usr/local/apache2/sites-enabled/000-default.conf
ADD apps /var/www/anime
RUN chmod 755 /entry.sh && mkdir -p /var/run/apache2 && a2enmod cgi

ENTRYPOINT ["/entry.sh"]
