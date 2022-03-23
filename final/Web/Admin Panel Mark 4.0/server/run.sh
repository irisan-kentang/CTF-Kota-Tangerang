#!/bin/sh

export DB_DATABASE=admin_panel_4 \
    DB_PASSWORD=4dm1n_p4n3l_4 \
    DB_USERNAME=root \
    DB_HOST=mysql \
    APP_NAME=Laravel \
    APP_ENV=local \
    APP_KEY=base64:CnxC/nYwKMFmB4ht2+StTw3Z/xo6ATK2LDiOk9GBRo4= \
    APP_DEBUG=false

cd /var/www && php artisan migrate:fresh
php-fpm