<?PHP

	function isregistered ($username, $usrstack)
	{
		foreach ($usrstack as $tmpstack)
			if ($tmpstack == $username || (is_array($tmpstack) && isregistered($username, $tmpstack)))
				return true;
		return false;
	}

	//Checking if any of the form's inputs wasn't set (thus was NULL) to detect errors in case if any were there:

	if (!$_POST || !isset($_POST['submit']) || $_POST['submit'] !== "OK")
	{
		echo "ERROR\n";
		exit();
	}
	if (!isset($_POST['login']) || empty($_POST['login']) || !isset($_POST['passwd']) || empty($_POST['passwd']))
	{
		echo "ERROR\n";
		exit();
	}

	//Initialising the users' list of credentials or unserilizing users' input(s) according to the current state:

	$userslist = @file_get_contents('../private/passwd');
	if (!$userslist)
	{
		$userslist = [];
		mkdir('../private');
	}
	else
		$userslist = unserialize($userslist);

	//Checking if the UserName does already exit in the UsersList and returning an error massage in case it does:

	if (isregistered($_POST['login'], $userslist))
	{
		echo "ERROR\n";
		exit();
	}

	//In case the UserName isn't already in the UsersList, it's to be added to it (w/ user's encrypted PassWord):

	$userslist[] = [
		'login' => $_POST['login'],
		'passwd' => hash('sha256', $_POST['passwd'])
	];

	//After sorting the new data in the UsersList, it's to be saved in a storable format, after being serialized:

	file_put_contents('../private/passwd', serialize($userslist));
	echo "OK\n";

?>
