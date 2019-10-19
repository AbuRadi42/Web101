#!/usr/bin/php
<?PHP

	$i = 1;
	while ($i <= $argc)
	{
		$array = preg_split("/[\s]+/", trim($argv[$i]));
		sort($array, SORT_REGULAR);
		echo implode("\n", $array);
		if($i != $argc)
			echo "\n";
		$i++;
	}

?>
