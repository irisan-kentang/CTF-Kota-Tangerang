<?php

require __DIR__ . '/vendor/autoload.php';

$client = new MongoDB\Client("mongodb://kijang-satu-mongo:27017");
$db = $client->ctftangerang;
