FROM php:7.3-fpm

# Set working directory
WORKDIR /var/www

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    locales \
    zip \
    vim \
    unzip \
    git \
    zlib1g-dev \
    libzip-dev \
    libsqlite3-dev \
    curl

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install extensions
RUN docker-php-ext-install pdo_sqlite mbstring zip exif pcntl

COPY ./app /var/www

RUN rm adm00ndata1337.db
RUN php init.php
RUN rm init.php

# Add user for application
RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

# Change current user to www
USER www

# Expose port 9000 and start php-fpm server
EXPOSE 9000
CMD ["php-fpm"]
