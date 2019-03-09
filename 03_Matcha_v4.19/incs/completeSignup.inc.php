<?php
	ini_set("display_errors", "On");
	include_once '../cnfg/dbh.php';
	include_once './auxfns.inc.php';
	require_once("../cnfg/setup.php");
	
	new db_handle();

	if ($_POST['signUp'] && $_POST['userName'] && $_POST['eMail'] && $_POST['passWord'] && $_POST['Repeat']) {
		$userName = $_POST['userName'];
		$eMail = $_POST['eMail'];
		$passWord = $_POST['passWord'];
		$Repeat = $_POST['Repeat'];
		$toNotify = (isset($_POST['toNotify'])) ? 1 : 0;
		if (!passWordMaches($passWord, $Repeat)) {
			header('Location: ../completeSignup.php?input=passwords_dont_match');
			return ;
		}
		if (!passWordisValid($passWord)) {
			header('Location: ../completeSignup.php?input=password_is_invalid');
			return ;
		}
		$object = db_handle::$INSTANCE;
		
		if (!($object->userNameAlreadyExists($userName))) {
			$HashKey = hash('whirlpool', $passWord.$userName);
			$HashPwd = hash('whirlpool', $passWord);
			confirmationEmailSend($userName, $eMail, $HashKey);
			$object->userDetailsInsertion($userName, $eMail, $HashPwd, $HashKey, $toNotify);
			echo '<h5 style="text-align: center">Please check your eMail to activate your account.</h5>';
			sleep(5);
			header('Location: ../index.php');
		}
		else {
			header('Location: ../completeSignup.php?input=userName_OR_eMail_is_taken');
			return ;
		}
	}
	else {
		header('Location: ../completeSignup.php?input=incompleteForm');
		return ;
	}
