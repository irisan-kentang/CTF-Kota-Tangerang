FROM debian:bookworm
RUN apt update
RUN apt install php7.4-cli php7.4-curl -y
ADD apache2_2.4.49-4_amd64.deb apache2-bin_2.4.49-4_amd64.deb apache2-data_2.4.49-4_all.deb apache2-utils_2.4.49-4_amd64.deb /
RUN apt install -y perl libxml2 libaprutil1-dbd-sqlite3 libnghttp2-14 libaprutil1-ldap libbrotli1 libcurl4 libjansson4 liblua5.3-0 procps mime-support
RUN dpkg -i /apache2-utils_2.4.49-4_amd64.deb /apache2-data_2.4.49-4_all.deb /apache2-bin_2.4.49-4_amd64.deb /apache2_2.4.49-4_amd64.deb
RUN apt install libapache2-mod-php7.4
RUN a2enmod php7.4
RUN a2enmod rewrite
ADD entry.sh /entry.sh
ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf
ADD apps /var/www/anime
RUN chmod 755 /entry.sh && mkdir -p /var/run/apache2 && a2enmod cgi

ENTRYPOINT ["/entry.sh"]
