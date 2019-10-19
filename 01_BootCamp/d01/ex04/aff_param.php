#!/usr/bin/php
<?PHP

	$i = $argc - 1;
	$j = 1;
	while ($i > 0)
	{
		echo $argv[$j++]."\n";
		$i--;
	}

?>
