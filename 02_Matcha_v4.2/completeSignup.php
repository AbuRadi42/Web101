<?php
    require "header.php";
?>

<div class="page">
  <div class="container1">
    <div class="rightform1">
      <form method="POST" action="incs/completeSignup.inc.php" class="form1">
        <label for="username">Username</label>
        <input type="username" class="textholder" name="userName">
        <label for="fullname">Fullname</label>
        <input type="fullname" class="textholder" name="fullName">
        <label for="email">Email</label>
        <input type="email" class="textholder" name="eMail">
        <label for="password">Password</label>
        <input type="password" class="textholder" name="passWord">
        <label for="password">Repeat Password</label>
        <input type="password" class="textholder" name="Repeat">
        <select multiple style="width: 48.75%" name="Gender">
          <option value="1">male</option>
          <option value="0">female</option>
        </select>
        <select multiple style="width: 48.75%" name="Sexuality">
          <option value="hetero">heterosexual</option>
          <option value="homo">homosexual</option>
          <option value="bi">bisexual</option>
        </select>
        <label for="Biography">Biography</label>
        <input type="Biography" class="textholder" name="Biography">
        <label for="Interests">Interests</label>
        <input type="Interests" class="textholder" name="Interests">

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