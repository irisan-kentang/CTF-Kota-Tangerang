FROM php:7.4-fpm

ADD entry.sh /entry.sh
ADD apps /var/www/html
RUN chmod 755 /entry.sh
