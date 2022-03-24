<?php
    require __DIR__ . '/../vendor/autoload.php';
    $redis = new Predis\Client('tcp://redis:6379');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Kamu anime yah banh?</title>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12 text-center">
                <h1>Kamu anime yah banh?</h1>
                <iframe width="560" height="315" src="https://www.youtube.com/embed/sH8DCvsCyb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                <p>Submit nama anda untuk mendapatkan anime point secara random.</p>
                <p>Anda akan menjadi riil anime jika mendapatkan 999999 anime point</p>
                <form class="row justify-content-md-center" action="" method="POST">
                    <div class="col-6">
                        <label for="nama" class="form-label">Nama</label>
                        <input type="text" class="form-control" id="nama" name="nama" aria-describedby="namaHelp">
                        <div id="namaHelp" class="form-text">Masukkan nama anda.</div>
                    </div>
                    <div class="col-12">
                        <button type="submit" name="get_anime_point" class="btn btn-primary">Get Anime Point</button>
                    </div>
                </form>
            </div>
            <div class="col-12 text-center">
            <?php
                if (isset($_POST['get_anime_point'])) {
                    $nama = $_POST['nama'];
                    if (!ctype_alpha($nama)) {
                        echo '<h3 class="text-danger">Nama hanya berupa karakter [a-zA-Z]</h3>';
                        die();
                    }
                    if ($redis->exists("nama_".$nama)) {
                        $scredit = intval($redis->get("nama_".$nama));
                        echo "<h3 class=\"text-success\">Hi $nama, kamu mendapatkan Anime Point $scredit</h3>";
                    } else {
                        $scredit = rand(1, 1000);
                        $redis->set("nama_".$nama, $scredit);
                        echo "<h3 class=\"text-success\">Hi $nama, kamu mendapatkan Anime Point $scredit</h3>";
                    }

                    if ($scredit == 999999) {
                        $flag = $redis->get("flag_gwej_anime");
                        echo "<h3 class=\"text-primary\">Hi $nama, kamu mendapatkan flag $flag dan menjadi anime</h3>";
                    }
                }
            ?>
            </div>
        </div>
    </div>
</body>
</html>