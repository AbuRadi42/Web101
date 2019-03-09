SELECT REVERSE(RIGHT(phone_number, LENGTH(phone_number) - 1)) AS rebmunenohp FROM db_saburadi.distrib
	WHERE LEFT(phone_number, 2) = '05'
	;
