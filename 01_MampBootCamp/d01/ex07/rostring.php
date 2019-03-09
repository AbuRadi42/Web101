#!/usr/bin/php
<?PHP

	if($argc > 1)
	{
		$epured = preg_split("/[\s]+/", trim($argv[1]));
		echo implode(" ", array_slice($epured, 1));
		echo " ".$epured[0];
		echo "\n";
	}

?>
