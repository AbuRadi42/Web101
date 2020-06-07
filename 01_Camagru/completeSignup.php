<?php
    require "header.php";
?>

<div class="page">
  <div class="container1">
    <div class="rightform1">
      <form method="POST" action="incs/completeSignup.inc.php" class="form1">
        <label for="username">Username</label>
        <input type="username" class="textholder" name="userName">
        <label for="email">Email</label>
        <input type="email" class="textholder" name="eMail">
        <label for="password">Password</label>
        <input type="password" class="textholder" name="passWord">
        <label for="password">Repeat Password</label>
        <input type="password" class="textholder" name="Repeat">
        <label for="Notification">
          <input class="checkBox" type="checkbox" name="toNotify" value="notification" style="float: left; margin-top: 5px">
          <h5 class="notprmssn">I'd like to recieve notifications via email</h5>
        </label>
        <br>
        <input type="submit" class="submit" value="Continue" name="signUp">
        <br>
        <a href="./index.php"><input value="Cancel" class="submit"></a>
      </form>
      <div class="eula">By signing up you agree to our <a href="/#" title="Be Awesome!">terms & conditions</a>.</div>
    </div>
  </div>
</div>

<?php
    require "footer.php";
?>