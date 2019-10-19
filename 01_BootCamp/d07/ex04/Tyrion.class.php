<?PHP

	class Tyrion extends Lannister {

		function sleepWith($person) {

			if(get_class($person) == "Sansa")
				echo "Let's do this.\n";
			elseif(get_class($person) == "Cersei")
				echo "Not even if I'm drunk !\n";
			elseif(get_class($person) == "Jaime")
				echo "Not even if I'm drunk !\n";

		}

	}

?>
