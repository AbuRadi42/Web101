#!/usr/bin/php
<?PHP

	if($argc > 1)
	{
		$epured = preg_split("/[\s]+/", trim($argv[1]));
		echo implode(" ", $epured);
		echo "\n";
	}

?>
