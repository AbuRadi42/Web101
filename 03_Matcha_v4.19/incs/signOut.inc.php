<?php
	ini_set("display_errors", "On");
	session_start();
	include_once '../cnfg/dbh.php';

	$obj = new db_handle();
	$obj->LastCnctTime($_GET['signOutId']);
	$obj->getUnconnected($_GET['signOutId']);
	if (isset($_GET['signOutUserName'])) {
		session_start();
		session_unset();
		session_destroy();
		header('Location: ../index.php');
	}
