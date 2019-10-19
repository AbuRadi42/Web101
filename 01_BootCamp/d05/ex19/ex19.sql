SELECT ABS(DATEDIFF(MIN(`date`), MAX(`date`))) AS uptime FROM db_saburadi.member_history
	;
