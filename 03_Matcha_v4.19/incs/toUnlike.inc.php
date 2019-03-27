<?php
	ini_set("display_errors", "On");
	session_start();
	include_once '../cnfg/dbh.php';

	$obj = new db_handle();
	$obj->some1unlikessome1($_SESSION['userName']['Id'], $_GET['UnlikedId']);
	$obj->decrementFameRate($_GET['UnlikedId']);
	header('Location: ../index.php');