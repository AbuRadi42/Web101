CREATE TABLE db_saburadi.ft_table (
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
login VARCHAR(8) NOT NULL DEFAULT 'toto',
`group` ENUM('staff', 'student', 'other') NOT NULL,
creation_date date NOT NULL)
;
