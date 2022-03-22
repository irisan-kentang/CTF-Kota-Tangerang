#!/bin/bash

php /var/www/social_credit/init.php
rm /var/www/social_credit/init.php

source /etc/apache2/envvars
exec apache2 -D FOREGROUND