<?php
	ini_set("display_errors", "On");
	session_start();
	include_once '../cnfg/dbh.php';

	$obj = new db_handle();
	$obj->some1BlockedSome1($_SESSION['userName']['Id'], $_GET['BlockedId']);
	header('Location: ../index.php');