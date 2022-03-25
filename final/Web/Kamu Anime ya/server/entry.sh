#!/bin/bash

php /var/www/html/init.php
rm -f /var/www/html/init.php

httpd-foreground
