SELECT name FROM db_saburadi.distrib
	WHERE id_distrib IN (42, 62, 63, 64, 65, 66, 67, 68, 69, 71, 88, 89, 90) OR name LIKE '%y%y%Y%Y%'
	LIMIT 2, 5
	;
	/*another way: ORDER BY -> OFFSET -> FETCH*/
