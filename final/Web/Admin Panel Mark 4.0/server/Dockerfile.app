FROM php:8.1.4-fpm

# Copy composer.lock and composer.json
COPY ./apps/composer.lock /var/www/
COPY ./apps/composer.json /var/www/

# Set working directory
WORKDIR /var/www

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    mariadb-client \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    zip \
    jpegoptim optipng pngquant gifsicle \
    vim \
    unzip \
    git \
    curl

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install extensions
RUN docker-php-ext-install pdo_mysql mbstring zip exif pcntl
RUN docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/
RUN docker-php-ext-install gd

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

ENV DB_DATABASE=admin_panel_4 \
    DB_PASSWORD=4dm1n_p4n3l_4 \
    DB_USERNAME=root \
    DB_HOST=mysql \
    APP_NAME=Laravel \
    APP_ENV=local \
    APP_KEY=base64:CnxC/nYwKMFmB4ht2+StTw3Z/xo6ATK2LDiOk9GBRo4= \
    APP_DEBUG=false

# Add user for laravel application
RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

# Copy existing application directory contents
COPY ./app /var/www

RUN cd /var/www && composer install && php artisan migrate:fresh

# Copy existing application directory permissions
COPY --chown=www:www . /var/www

# Change current user to www
USER www

# Expose port 9000 and start php-fpm server
EXPOSE 9000
CMD ["php-fpm"]
