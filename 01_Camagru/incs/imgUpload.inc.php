<?php
	ini_set("display_errors", "On");
	session_start();
	include_once '../cnfg/dbh.php';

	if (isset($_POST['img']) && isset($_SESSION['userName']['Id'])) {
		$uri = preg_replace('#^data:image/\w+;base64,#i', '',$_POST['img']);
		if ($uri !== "") {
			$obj = new db_handle();
			$obj->imgIntoDBInsert($uri, $_SESSION['userName']['Id']);
			header('Location: ../index.php?upload_succeed');
		}
		else
			header('Location: ../index.php?input=incomplete');
	}
	else
		header('Location: ../index.php?input=Submit_unset');
