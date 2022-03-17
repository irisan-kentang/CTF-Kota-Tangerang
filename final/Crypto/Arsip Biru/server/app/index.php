<?php
    if (!isset($_COOKIE['token'])) {
        $authenticated = false;
    } else {
        
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
    <title>SCHALE - Login</title>
</head>

<body>
    <div class="container">
        <form class="myForm p-3 rounded" method="post">
            <div class="form-group">
                <h1>SCHALE</h1>
                <h2>Student Management System</h2>
            </div>
            <div class="form-group mt-3">
                <label class="mb-2" for="email">Masukan Nama Anda</label>
                <input class="form-control input-lg" placeholder="Nama" />
            </div>
            <div class="form-group mt-3">
                <input type="submit" name="submit" class="btn btn-success btn-lg" value="Masuk" />
            </div>
        </form>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>