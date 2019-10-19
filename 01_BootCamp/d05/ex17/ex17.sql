SELECT count(name) AS nb_susc, ROUND(AVG(price), -1) AS av_susc, SUM(duration_sub) AS ft FROM db_saburadi.subscription
	;
