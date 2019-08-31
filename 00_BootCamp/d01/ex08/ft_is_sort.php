<?PHP

	function ft_is_sort($array0): bool {
		$return = true;
		$array1 = $array0;
		sort($array1, SORT_REGULAR);
		$index0 = 0;
		while ($i < count($array0))
		{
			if ($array1[$i] != $array0[$i])
				$return = false;
			$i++;
		}
		return $return;
	}

?>
