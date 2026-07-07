<?php

function iterative_binary_search($arr, $target) {
	// assign start and end an index position
	$start = 0;
	$end = count($arr) - 1;

	while ($start <= $end) {
		// code...
		$midpoint = $start + ( floor($end - $start)/ 2);

		if ($arr[$midpoint] === $target) {
			// code...
			return $midpoint;
		}
		elseif ($arr[$midpoint] < $target) {
			// code...
			$start = $midpoint + 1;
		}
		else {
			$end = $midpoint - 1;
		}
	}
	return -1;
}