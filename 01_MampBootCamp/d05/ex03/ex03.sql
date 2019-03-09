INSERT INTO db_saburadi.ft_table (login, `group`, creation_date)
	SELECT last_name AS login, 'other' AS `group`, birthdate AS creation_date FROM db_saburadi.user_card
	WHERE LENGTH(last_name) < 9 AND last_name LIKE '%a%'
	ORDER BY last_name
	LIMIT 10
	;
