<?php
	function passWordMaches($passWord, $Repeat) {
		if ($passWord !== $Repeat) {
			return FALSE;
		}
		return TRUE;
	}

	function passWordisValid($passWord) {
		if (strlen($passWord) < 9 || strlen($passWord) > 20) {
			return FALSE;
		}
		if (!(preg_match('/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,20}$/', $passWord))) {
			return FALSE;
		}
		return TRUE;
	}

	function confirmationEmailSend($userName, $eMail, $HashKey) {
		$link = "http://localhost:8080/Camagru/accountActivate.php?HashKey=".$HashKey;
		$headers = "MIME-Version: 1.0"."\r\n";
		$headers .= "Content-type:text/html;charset=UTF-8"."\r\n";
		$subject = "Camagru Account Verification";
		$headers .= "From: Saburadi@student.wethinkcode.co.za";
		$content =
		"
		<html>
		  <head>
		  	<title> HTML eMail </title>
		  </head>
		  <body>
		  	Hello ".$userName.",
		  	Click this <a href=".$link.">link</a> to activate your Camagru account
		  	Regards!
		  </body>
		 </html>
		";
		mail($eMail, $subject, $content, $headers);
	}

	function reSetEmailSend($userName, $eMail, $HashKey) {
		$link = "http://localhost:8080/Camagru/reSetPassWord.php?HashKey=".$HashKey;
		$headers = "MIME-Version: 1.0"."\r\n";
		$headers .= "Content-type:text/html;charset=UTF-8"."\r\n";
		$subject = "passWord reSet";
		$headers .= "From: Saburadi@student.wethinkcode.co.za";
		$content =
		"
		<html>
		  <head>
		  	<title> HTML eMail </title>
		  </head>
		  <body>
		  	Hello ".$userName.",
		  	Click this <a href=".$link.">link</a> to reset your Camagru password
		  	Regards!
		  </body>
		 </html>
		";
		mail($eMail, $subject, $content, $headers);
	}
