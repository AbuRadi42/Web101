<?php
    require_once('./cnfg/dbh.php');
?>

<!DOCTYPE html>

<html>
<head>
  <title></title>
  <link rel="stylesheet" type="text/css" href="./style.css">
</head>
<body>

<div class="page">
  <div class="container">
    <div class="left">
      <div class="wlcmsg">Welcome to <a href="./index.php">Camagru</a>!</div>
      <div class="login">Sign in;</div>
      <div class="eula">By signing up you agree to our <a href="#" title="Be Awesome!">terms & conditions</a>.</div>
      <div class="eulu">Made with keyboard by Sameh M. AbuRadi</div>
    </div>
    <div class="right">
      <svg viewBox="0 0 320 300">
        <defs>
          <linearGradient
                          inkscape:collect="always"
                          id="linearGradient"
                          x1="12.5"
                          y1="193.4999"
                          x2="309"
                          y2="193.4999"
                          gradientUnits="userSpaceOnUse">
            <stop
                  style="stop-color:#ff00ff;"
                  offset="0"
                  id="stop876" />
            <stop
                  style="stop-color:#ff0000;"
                  offset="1"
                  id="stop878" />
          </linearGradient>
        </defs>
        <path d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,35 -25.00016,35 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143"/>
      </svg>
      <form class="form" action="incs/signin.inc.php" method="POST">
        <label for="email">Email or userName</label>
        <input type="userName" id="email" name="signInEmail">
        <label for="password">Password</label>
        <input type="password" id="password" name="signInToHashPW">
        <input type="submit" id="submit" class="submit" value="Sign In" name="signInSubmit">
        <br>
        <div class="eulo"><a href="forgotPassWord.php"><h5 style="text-align: center">I forgot my password.</h5></a></div>
      </form>
    </div>
  </div>
</div>

</body>
</html>
