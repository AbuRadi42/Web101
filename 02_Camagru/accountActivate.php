<?php
	ini_set("display_errors", "On");
	include_once './cnfg/dbh.php';

	if (isset($_GET['HashKey'])) {
		$HashKey = $_GET['HashKey'];
		$obj = new db_handle();
		$row = $obj->findKeyMatch($HashKey);
		$obj->activateAccount($HashKey);
		echo '<h5 style="text-align: center">Your account has been activated.</h5>';
		sleep(5);
		header('Location: ./index.php');
	}
	else {
		echo '<h5 style="text-align: center">Your account has not been activated.</h5>';
	}
?>
