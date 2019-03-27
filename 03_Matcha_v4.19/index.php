<?php
    require_once("cnfg/dbh.php");
    require "header.php";
    session_start();
?>

<?php
    include_once 'cnfg/dbh.php';
    $obj = new db_handle();
    $rows = $obj->usrsFromDBFetch();

    for ($i = 0; $i < sizeof($rows); $i++) {
        if (1) {
            echo
            '
              <div class="responsive">
                <div class="gallery" title="';
            if ($rows[$i]['Cnctvity'])
                echo 'Connected';
            else
                echo 'Last Seen on '.$rows[$i]['LastCnctTime'];
            echo
            '">
                  <a target="_blank" href="">
                    <div class="under gallery">
                      <img src="data:image/png;base64,'.$rows[$i]['Img1'].'" alt="'.$rows[$i]['Id'].'" width="600" height="400" class="over">
                    </div>
                  </a>
                <div class="desc" title="Interests: '.$rows[$i]['Interests'].'1&#013;Biography: '.$rows[$i]['Biography'].'">
                  <a href="./incs/toBlock.inc.php?BlockedId='.$rows[$i]['Id'].'">⨂</a>
            ';

            if ($rows[$i]['Gender'] == 1 && $rows[$i]['Sexuality'] == "hetero")
                echo ' ♂ ⚤ ';
            else if ($rows[$i]['Gender'] == 1 && $rows[$i]['Sexuality'] == "homo")
                echo ' ♂ ⚣ ';
            else if ($rows[$i]['Gender'] == 1 && $rows[$i]['Sexuality'] == "bi")
                echo ' ♂ ⚥ ';
            else if ($rows[$i]['Gender'] == 0 && $rows[$i]['Sexuality'] == "hetero")
                echo ' ♀ ⚤ ';
            else if ($rows[$i]['Gender'] == 0 && $rows[$i]['Sexuality'] == "homo")
                echo ' ♀ ⚢ ';
            else if ($rows[$i]['Gender'] == 0 && $rows[$i]['Sexuality'] == "bi")
                echo ' ♀ ⚥ ';
            echo
                $rows[$i]['fullName'].' ('.$rows[$i]['fameRate'].') ';
            if ($rows[$i]['Id'] !== $_SESSION['userName']['Id']) {
                if ($obj->isntSome1ILike($_SESSION['userName']['Id'], $rows[$i]['Id']) && $_SESSION['userName'])
                    echo '<br /> <a href="./incs/toLike.inc.php?LikedId='.$rows[$i]['Id'].'">like ❤️</a>';
                else if ($_SESSION['userName'])
                    echo '<br /> <a href="./incs/toUnlike.inc.php?UnlikedId='.$rows[$i]['Id'].'">unlike 💔</a>';
            }
            else
                echo '<br /> <a href="" style="color: white">.</a>';
            if ($obj->weBothLikeEachOther($_SESSION['userName']['Id'], $rows[$i]['Id'])) {
                echo ' <a href="./Chat.php?chattedTo='.$rows[$i]['Id'].'">CHAT! 💬</a>';
            }
             else
                echo ' <a href="" style="color: white">.</a>';
            echo
                  '</div>
                </div>
              </div>
            ';
        }
    }
?>

<div class="clearfix"></div>

<?php
    require "footer.php";
?>