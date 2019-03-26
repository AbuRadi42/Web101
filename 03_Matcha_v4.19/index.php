<?php
    require_once("cnfg/dbh.php");
    require "header.php";
    session_start();
?>

<?php
    include_once 'cnfg/dbh.php';

    $obj = new db_handle();
    $rows = $obj->imgFromDBFetch();

    for ($i = 0; $i < sizeof($rows); $i++) {
        echo
        '
          <div class="responsive">
            <div class="gallery">
              <a target="_blank" href="">
                <div class="under gallery">
                  <img src="data:image/png;base64,'.$rows[$i]['Img1'].'" alt="'.$rows[$i]['Id'].'" width="600" height="400" class="over">
                </div>
              </a>
            <div class="desc">'.$rows[$i]['fullName'].'';
        if ($rows[$i]['Id'] !== $_SESSION['userName']['Id']) {
            if ("you didn't like him\\her")
                echo '<br /> <a href="">like 👍</a>';
            else
                echo '<br /> <a href="">unlike 👎</a>';
        }
        else
            echo '<br /> <a href="" style="color: white">.</a>';
        echo
              '</div>
            </div>
          </div>
        ';
    }
?>

<div class="clearfix"></div>

<?php
    require "footer.php";
?>