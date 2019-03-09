<?php
	ini_set("display_errors", "On");
	include_once '../cnfg/dbh.php';

	if ($_POST['signInSubmit'] && $_POST['signInEmail'] && $_POST['signInToHashPW']) {
		$userName = htmlspecialchars($_POST['signInEmail']);
		$toHashPW = hash('whirlpool', $_POST['signInToHashPW']);
		$obj = new db_handle();
		$row = $obj->findNameMatch($userName);
		if ($row) {
			if ($row['passWord'] == $toHashPW) {
				if ($row['Activity']) {
					session_start();
					$_SESSION['userName'] = ['userName'=>$row['userName'], 'Id'=>$row['Id']];
					
					header('Location: ../index.php?login=success');
				}
				else
					header('Location: ../index.php?login=account_not_activated_yet');
			}
			else
				header('Location: ../index.php?login=passWords_didnt_match');
		}
		else
			header('Location: ../index.php?login=userName_wasnt_found');
	}
	else
		header('Location: ../index.php?login=incompleteForm');
