<?php
	if (isset($_GET['signOutSubmit'])) {
		session_start();
		session_unset();
		session_destroy();
		header('Location: ../index.php');
	}
