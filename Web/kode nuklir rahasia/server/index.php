<?php

if (isset($_GET['kode1']) && isset($_GET['kode2'])) {
    $kode1 = $_GET['kode1'];
    $kode2 = $_GET['kode2'];

    if ($kode1 !== $kode2) {
        if ($kode1 == $kode2) {
            die("tangerangkota{kode_peluncuran_nuklir_381731}");
        }
    }
    die("kode salah");
} else {
    die('/?kode1=&kode2=');
}