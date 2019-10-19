<?php
  session_start();
  require_once("cnfg/setup.php");
?>

<!DOCTYPE html>
<html>
<head>
  <title></title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="header">
  <a href="./index.php" class="logo">Camagru</a>
  <?php
      if (isset($_SESSION['userName'])) {
          echo '
              <div class="header-right">
                <a href="./imgUpload.php">Upload an Image</a>
                <a href="./settings.php">Settings</a>
                <a href="incs/signOut.inc.php?signOutSubmit='.$_SESSION['userName'].'">Sign Out</a>
              </div>
              ';
      }
      else {
          echo '             
              <div class="header-right">
                <a href="./References.php">About us</a>
                <a href="./signin.php">Sign in</a>
                <a href="./completeSignup.php">Sign up</a>
              </div>
              ';
      }
  ?>
</div>

<br>
