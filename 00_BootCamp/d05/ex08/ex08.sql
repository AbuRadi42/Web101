SELECT last_name, first_name, birthdate AS birthdate FROM db_saburadi.user_card
	WHERE year(birthdate) = 1989 ORDER BY last_name ASC
	;
