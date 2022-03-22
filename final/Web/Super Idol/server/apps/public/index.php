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
    <title>Super Idol</title>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12 text-center">
                <h1>Super Idol</h1>
                <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/aCgP8BFjrw4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                <p>Daftarkan nama anda untuk mendapatkan social credit secara random.</p>
                <p>Anda akan menjadi SUPER IDOL jika mendapatkan +999999 social credit</p>
                <form class="row justify-content-md-center" action="" method="POST">
                    <div class="col-6">
                        <label for="nama" class="form-label">Nama</label>
                        <input type="text" class="form-control" id="nama" name="nama" aria-describedby="namaHelp">
                        <div id="namaHelp" class="form-text">Masukkan nama anda.</div>
                    </div>
                    <div class="col-12">
                        <button type="submit" name="get_social_credit" class="btn btn-primary">Get Social Credit</button>
                    </div>
                </form>
            </div>
            <div class="col-12 text-center">
            <?php
                if (isset($_POST['get_social_credit'])) {
                    $nama = $_POST['nama'];
                    if (!ctype_alpha($nama)) {
                        echo '<h3 class="text-danger">Nama hanya berupa karakter [a-zA-Z], Social Credit -9999</h3>';
                        die();
                    }
                    if ($redis->exists("nama_".$nama)) {
                        $scredit = intval($redis->get("nama_".$nama));
                        echo "<h3 class=\"text-success\">Hi $nama, kamu mendapatkan Social Credit +$scredit</h3>";
                    } else {
                        $scredit = rand(1, 1000);
                        $redis->set("nama_".$nama, $scredit);
                        echo "<h3 class=\"text-success\">Hi $nama, kamu mendapatkan Social Credit +$scredit</h3>";
                    }

                    if ($scredit == 999999) {
                        $flag = $redis->get("flag_super_idol");
                        echo "<h3 class=\"text-primary\">Hi $nama, kamu rakyat yang budiman, kamu mendapatkan flag $flag dan berbakat menjadi SUPER IDOL</h3>";
                    }
                }
            ?>
            </div>
            <div class="col-12 text-center">
                <br>
                <img width="200px" src="https://c.tenor.com/-NENNF2ptzkAAAAC/social-credit-social-credit-score.gif" alt="social credit">
            </div>
        </div>
    </div>
</body>
</html>