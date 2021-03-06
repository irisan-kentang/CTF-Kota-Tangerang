<?php
    include 'config.php';
    $cipher = 'AES-128-CBC';
    $authenticated = false;

    if (isset($_POST['nama'])) {
        $name = $_POST['nama'];

        $token = "name=".$name."|"."sensei=0";
        $encryptedToken = openssl_encrypt($token, $cipher, $secret, 0, $iv);

        setcookie('token', $encryptedToken, time() + (86400 * 30), "/");
        $_COOKIE['token'] = $encryptedToken;
        $authenticated = true;
    }

    if (!isset($_COOKIE['token'])) {
        $authenticated = false;
    } else {
        $token = $_COOKIE['token'];
        $token = openssl_decrypt($token, $cipher, $secret, 0, $iv);

        $name = "";
        $sensei = "";
        $tokenDetails = explode('|', $token);
        foreach ($tokenDetails as $detail) {
            $keyValue = explode('=', $detail);
            if ($keyValue[0] == 'name') {
                $name = $keyValue[1];
            } else if ($keyValue[0] == 'sensei') {
                $sensei = $keyValue[1];
            }
        }

        $isSensei = false;
        if ($sensei == '1') {
            $isSensei = true;
        }
        $authenticated = true;
    }
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.4/css/fontawesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.0/font/bootstrap-icons.css">
    <link rel="stylesheet" href="/css/style.css">
    <?php if (!$authenticated): ?>
        <title>SCHALE - Login</title>
    <?php else: ?>
        <title>SCHALE - Dashboard</title>
    <?php endif; ?>
</head>

<body>
    <div class="container">
        <form class="myForm p-3 rounded" method="post">
            <div class="form-group">
                <h1>SCHALE</h1>
                <h2>Student Management System</h2>
            </div>
            <?php if (!$authenticated): ?>
            <div class="form-group mt-3">
                <label class="mb-2" for="email">Masukan Nama Anda</label>
                <input name="nama" class="form-control input-lg" placeholder="Nama" />
            </div>
            <div class="form-group mt-3">
                <input type="submit" name="submit" class="btn btn-success btn-lg" value="Masuk" />
            </div>
            <?php else: ?>
                <?php if ($isSensei): ?>
                    <p>Selamat datang sensei, flag anda <?php echo $flag; ?></p>
                <?php else: ?>
                    <p>Selamat datang murid <?php echo $name; ?></p>
                <?php endif; ?>
            <?php endif; ?>
        </form>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>