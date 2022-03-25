#!/bin/bash

php /var/www/anime/init.php
rm /var/www/anime/init.php

source /etc/apache2/envvars
exec httpd
