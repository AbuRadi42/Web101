<?php
    require "header.php";
?>

<div class="page">
  <div class="container1">
    <div class="rightform1">
      <form method="POST" action="incs/preferencesChange.inc.php" class="form1">
        <label for="username">Username</label>
        <input type="username" class="textholder" name="newName">
        <label for="email">Email</label>
        <input type="email" class="textholder" name="newEmail">
        <label for="password">Password</label>
        <input type="password" class="textholder" name="newPassWord">
        <label for="password">Repeat Password</label>
        <input type="password" class="textholder" name="newRepeat">
        <br>
        <input type="submit" class="submit" value="Save Change" name="Change">
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