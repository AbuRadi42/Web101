SELECT title AS Title, summary AS Summary, prod_year FROM db_saburadi.film
	WHERE id_genre LIKE '%erotic%'
	ORDER BY prod_year DESC
	;
