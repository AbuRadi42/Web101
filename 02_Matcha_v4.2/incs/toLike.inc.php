<?php
	ini_set("display_errors", "On");
	session_start();
	include_once '../cnfg/dbh.php';

	$obj = new db_handle();
	$obj->some1likessome1($_SESSION['userName']['Id'], $_GET['LikedId']);
	$obj->incrementFameRate($_GET['LikedId']);
	header('Location: ../index.php');