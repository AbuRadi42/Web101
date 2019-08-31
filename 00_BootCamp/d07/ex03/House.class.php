<?PHP

	class House {

		public function getHouseName() {
			return;
		}

		public function getHouseMotto() {
			return;
		}

		public function getHouseSeat() {
			return;
		}

		public function introduce() {

			echo 'House '.static::getHouseName().' of '.static::getHouseSeat().' : "'.static::getHouseMotto().'"'."\n";

		}

	}

?>
