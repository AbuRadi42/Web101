<?php
    require "header.php";
?>

<div class="page">
  <div class="container10">
    <div class="forgotpwdbox">
      <form class="form10" action="incs/reSetPassWord.inc.php?HashKey=<?php echo $_GET['HashKey']; ?>" method="POST">
        <label for="email">New passWord</label>
        <input type="password" name="newPassWord">
         <label for="email">Repeat</label>
        <input type="password" name="newRepeat">
        <input type="submit" class="submit" value="Submit" name="forgotpwdSubmit">
      </form>
      <br>
    </div>
  </div>
</div>

<?php
    require "footer.php";
?>