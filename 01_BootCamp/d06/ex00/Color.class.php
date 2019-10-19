<?PHP

	class Color {

		public $red;
		public $green;
		public $blue;
		static $verbose = false;

		function __construct(array $rgb) {
			if(array_key_exists('rgb', $rgb)) {
				$this->$red = intval($rgb['rgb'][0]);
				$this->$green = intval($rgb['rgb'][1]);
				$this->$blue = intval($rgb['rgb'][1 + 1]);
			} elseif(array_key_exists('red', $rgb) &&
			array_key_exists('green', $rgb) &&
			array_key_exists('blue', $kwargs)) {
				$this->$red = intval($rgb['red']);
				$this->$green = intval($rgb['green']);
				$this->$blue = intval($rgb['blue']);
			}
			return;
		}
	}

?>
