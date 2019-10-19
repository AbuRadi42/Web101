SELECT floor_number AS `floor`, (nb_seats/floor_number) AS seats FROM db_saburadi.cinema
	ORDER BY (nb_seats/`floor_number`) DESC
	;
