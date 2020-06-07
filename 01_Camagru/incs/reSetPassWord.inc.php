<?php
	ini_set("display_errors", "On");
	include_once '../cnfg/dbh.php';
	include_once './auxfns.inc.php';

	if (isset($_POST['forgotpwdSubmit'])) {
		$HashKey = $_GET['HashKey'];
		$newPassWord = $_POST['newPassWord'];
		$newRepeat = $_POST['newRepeat'];
		if (!empty($newPassWord)) {
			if (!passWordMaches($newPassWord, $newRepeat)) {
				header('Location: ../index.php?input=passwords_dont_match&HashKey='.$HashKey);
				return ;
			}
			if (!passWordisValid($newPassWord)) {
				header('Location: ../index.php?input=password_is_invalid&HashKey='.$HashKey);
				return ;
			}
			$newPassWord = hash('whirlpool', $newPassWord);
			$newRepeat = hash('whirlpool', $newRepeat);
			$obj = new db_handle();
			$row = $obj->findKeyMatch($HashKey);
			$obj->resetPassWord($HashKey, $newPassWord);
			header('Location: ../index.php?pwdReSet=success');
		}
		else
			header('Location: ../index.php?input=empty_feild(s)');
	}
	else
		header('Location: ../index.php?input=forgotpwdSubmit_unset');
