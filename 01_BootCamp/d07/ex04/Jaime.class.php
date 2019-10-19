<?PHP

	class Jaime extends Lannister {

		function sleepWith($person) {

			if(get_class($person) == "Sansa")
				echo "Let's do this.\n";
			elseif(get_class($person) == "Cersei")
				echo "With pleasure, but only in a tower in Winterfell, then.\n";
			elseif(get_class($person) == "Tyrion")
				echo "Not even if I'm drunk !\n";

		}

	}

?>
