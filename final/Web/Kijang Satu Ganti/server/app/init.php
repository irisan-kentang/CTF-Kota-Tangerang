<?php

require_once '/var/www/config.php';

$agentsCollection = $db->agents;
$agentsCollection->insertOne([
	'name' => "kijang"
]);
$agentsCollection->insertOne([
	'name' => "tangerangkota{regex_satu_target_sedang_makan_nasgor_ganti}"
]);

unlink(__FILE__);