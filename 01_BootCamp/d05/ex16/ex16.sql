SELECT count(*) AS movies FROM db_saburadi.member_history
	WHERE (DATE(date) < '2007-07-28' AND DATE(date) > '2006-10-29')
	;
