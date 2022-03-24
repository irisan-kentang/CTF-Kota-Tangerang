<?php
    require __DIR__ . '/vendor/autoload.php';
    $redis = new Predis\Client('tcp://redis:6379');

    $redis->set('flag_gwej_anime', 'tangerangkota{ap4che_cve_2021_41773_n4isu}');
?>