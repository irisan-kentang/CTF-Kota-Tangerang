#!/bin/bash

php /var/www/html/init.php
rm /var/www/html/init.php

exec httpd -D FOREGROUND
