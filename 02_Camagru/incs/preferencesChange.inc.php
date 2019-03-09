<?php
	ini_set("display_errors", "On");
	include_once '../cnfg/dbh.php';
	include_once './auxfns.inc.php';

	if (isset($_POST['Change'])) {
		session_start();
		$crntName = $_SESSION['userName'];
		$newName = $_POST['newName'];
		$passWord = hash('whirlpool', $_POST['newPassWord']);
		if (!empty($newName) && !empty($passWord)) {
			$obj = new db_handle();
			$crntUserRow = $obj->findNameMatch($crntName);
			if ($passWord == $crntUserRow['passWord']) {
				$rowCheck = $obj->findNameMatch($newName);
				if (empty($rowCheck)) {
					$obj->updateUserName($crntName, $newName);
					$_SESSION['userName'] = $newName;
					header('Location: ../settings.php?userName_successfully_changed');
				}
				else
					header('Location: ../settings.php?input=Name_already_used');
			}
			else
				header('Location: ../settings.php?input=passWord_incorrect');
		}
		else
			header('Location: ../settings.php?input=Empty_fields');
	}
	else
		header('Location: ../settings.php?input=Submit_unset');
