<?php
	ini_set("display_errors", "On");
	include_once '../cnfg/dbh.php';
	include_once './auxfns.inc.php';
	require_once("../cnfg/setup.php");
	
	new db_handle();

	if ($_POST['signUp'] && $_POST['userName'] && $_POST['eMail'] && $_POST['passWord'] && $_POST['Repeat']
	&& $_POST['fullName'] && $_POST['Gender'] != NULL && $_POST['Sexuality']) {
		$userName = $_POST['userName'];
		$fullName = $_POST['fullName'];
		$eMail = $_POST['eMail'];
		$passWord = $_POST['passWord'];
		$Repeat = $_POST['Repeat'];
		$Gender = $_POST['Gender'];
		$Sexuality = $_POST['Sexuality'];
		$Biography = $_POST['Biography'];
		$Interests = $_POST['Interests'];
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
			$object->userDetailsInsertion($userName, $fullName, $eMail, $HashPwd, $HashKey, $Gender, $Sexuality, $Biography, $Interests);
			$object->userLocationUpdating($userName);
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
