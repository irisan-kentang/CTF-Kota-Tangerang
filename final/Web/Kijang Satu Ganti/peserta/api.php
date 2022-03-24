<?php

require_once 'config.php';

if (isset($_GET['agent'])) {
    $agent = $_GET['agent'];

    // filter anti heker karena jadi heker tidaklah baik :)
    $agent = str_replace(';', '', $agent);
    $agent = str_replace('/', '', $agent);
    $agent = str_replace('eval', '', $agent);
    $agent = str_replace('require', '', $agent);
    $agent = str_replace('`', '', $agent);

    $agentsCollection = $db->agents;
    $result = $agentsCollection->findOne([
        '$where' => "this.name == '$agent'"
    ]);

    header('Content-Type: application/json');

    if ($result == null) {
        $response = [
            'success' => false,
            'message' => "Agen tidak ditemukan dalam database"
        ];
    } else {
        $response = [
            'success' => true,
            'message' => "Agen ditemukan, data valid"
        ];
    }
    echo json_encode($response);
    exit;
}
?>