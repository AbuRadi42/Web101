<?php
    require "header.php";
?>

<div class="page">
  <div class="container10">
    <div class="forgotpwdbox">
      <form class="form10" action="incs/forgotPassWord.inc.php" method="POST">
        <label for="email">Email or userName</label>
        <input type="userName" id="email" name="forgotpwdUserName">
        <input type="submit" class="submit" value="Submit" name="forgotpwdSubmit">
      </form>
      <br>
    </div>
  </div>
</div>

<?php
    require "footer.php";
?>