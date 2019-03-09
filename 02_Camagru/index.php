<?php
    require_once("cnfg/dbh.php");
    require "header.php";
    session_start();
?>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="Cinque_Terre.jpg">
      <img src="./imgs/Cinque_Terre.jpg" alt="Cinque Terre" width="600" height="400" class="othrimgs">
    </a>
    <div class="desc">Italy</div>
  </div>
</div>


<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="Autumn_Forest.jpg">
      <img src="./imgs/Autumn_Forest.jpg" alt="Forest" width="600" height="400" class="othrimgs">
    </a>
    <div class="desc">Canada</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="Northern_Lights.jpg">
      <img src="./imgs/Northern_Lights.jpg" alt="Northern Lights" width="600" height="400" class="othrimgs">
    </a>
    <div class="desc">Finland</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="Mountains.jpg">
      <img src="./imgs/Mountains.jpg" alt="Mountains" width="600" height="400" class="othrimgs">
    </a>
    <div class="desc">Austria</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="Cinque_Terre_Other.jpg">
      <img src="./imgs/Cinque_Terre_Other.jpg" alt="Cinque Terre" width="600" height="400" class="othrimgs">
    </a>
    <div class="desc">Italy</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="Summer_Forest.jpg">
      <img src="./imgs/Summer_Forest.jpg" alt="Forest" width="600" height="400" class="othrimgs">
    </a>
    <div class="desc">Indonesia</div>
  </div>
</div>

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
                  <img src="data:image/png;base64,'.$rows[$i]['Img'].'" alt="'.$rows[$i]['Id'].'" width="600" height="400" class="over">
                </div>
              </a>
            <div class="desc">Description';
        if ($rows[$i]['userId'] == $_SESSION['userName']['Id']) {
            echo ' <a href="imgEdit.php">edit</a>';
            echo ' <a href="./incs/imgDelete.inc.php?imgId='.$rows[$i]['Id'].'">X</a>';
        }
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