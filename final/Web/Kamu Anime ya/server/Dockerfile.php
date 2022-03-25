FROM php:7.4-fpm

ADD apps /var/www/html
ADD entry.sh /entry.sh
ADD apps /var/www/html
RUN chmod 755 /entry.sh

RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

# Change current user to www
USER www
