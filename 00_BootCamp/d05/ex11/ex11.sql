SELECT UPPER(db_saburadi.user_card.last_name) AS NAME, db_saburadi.user_card.first_name, db_saburadi.subscription.price
	FROM db_saburadi.user_card
	INNER JOIN member ON db_saburadi.user_card.id_user = db_saburadi.member.id_user_card
	INNER JOIN subscription ON db_saburadi.member.id_sub = db_saburadi.subscription.id_sub
	WHERE db_saburadi.subscription.price > 42
	ORDER BY last_name ASC, first_name ASC
	;
