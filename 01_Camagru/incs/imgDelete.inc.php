<?php
	ini_set("display_errors", "On");
	session_start();
	include_once '../cnfg/dbh.php';

	$obj = new db_handle();
	$obj->imgFromDBRemove($_GET['imgId']);
	header('Location: ../index.php?Removal=success');
