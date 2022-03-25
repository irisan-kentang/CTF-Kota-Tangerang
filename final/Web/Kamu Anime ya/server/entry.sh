#!/bin/bash

php /var/www/html/init.php
rm /var/www/html/init.php

httpd-foreground
