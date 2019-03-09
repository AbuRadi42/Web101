<?php
	ini_set("display_errors", "On");
	include_once '../cnfg/dbh.php';
	include_once './auxfns.inc.php';

	$userName = $_POST['forgotpwdUserName'];
	$obj = new db_handle();
	$row = $obj->findNameMatch($userName);
	if ($row) {
		reSetEmailSend($userName, $row['eMail'], $row['HashKey']);
		echo '<h5 style="text-align: center">Please check your eMail to reset your password.</h5>';
		sleep(5);
		header('Location: ../index.php');
	}
	else
		header('Location: ../index.php?input=userName_not_found');
