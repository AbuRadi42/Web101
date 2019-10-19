#!/usr/bin/php
<?PHP

	while (1)
	{
		echo "Enter a number: ";
		$input = trim(fgets(STDIN));
		if(feof(STDIN))
		{
			echo "^D\n";
			exit;
		}
		elseif(!is_numeric($input))
			echo "'$input' is not a number\n";
		else
			if(intval($input) % 2 == 1)
				echo "the number $input is odd\n";
			else
				echo "the number $input is even\n";
	}

?>
