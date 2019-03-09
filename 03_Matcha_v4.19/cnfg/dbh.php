<?php

	class db_handle {

		private $_pdo;

		public static	$INSTANCE;
		private			$db_username = "root";
		private			$db_password = "MyPHPApp";
		private			$db_name = "Demo";
		private			$dsn = "mysql:host=localhost";

		public function __construct() {
			
			try {
				$this->_pdo = new PDO($this->dsn.";dbname={$this->db_name}", $this->db_username, $this->db_password, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
				$this->_pdo = $this->_pdo;
				error_log("Connection made");
				self::$INSTANCE = $this;
			}
			catch(PDOException $e) {
				error_log ("Connection failed: ".$e->getMessage());
				try{
					$this->_pdo = new PDO($this->dsn, $this->db_username, $this->db_password, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
					$this->_pdo->exec("CREATE DATABASE IF NOT EXISTS {$this->db_name}");
					$this->_pdo->exec("USE {$this->db_name}");
					$this->_pdo = $this->_pdo;
					
					$this->usrsTableCreate();
					$this->imgsTableCreate();
					self::$INSTANCE = $this;
					error_log("Database init complete");
				} catch(PDOException $e) { 
					echo "Connection failed: ".$e->getMessage();
				}
			}
		}

		public function usrsTableCreate() {
			$this->_pdo->exec("CREATE TABLE IF NOT EXISTS `Demo`.`usrs`(
			`Id` INT NOT NULL AUTO_INCREMENT ,
			`userName` VARCHAR(255) NULL DEFAULT NULL ,
			`eMail` VARCHAR(255) NULL DEFAULT NULL ,
			`passWord` VARCHAR(255) NULL DEFAULT NULL ,
			`HashKey` VARCHAR(255) NULL DEFAULT NULL , 
			`Activity` BOOLEAN NULL DEFAULT FALSE,
			`toNotify` BOOLEAN NULL DEFAULT FALSE,
			PRIMARY KEY (`Id`)) ENGINE = InnoDB;");
		}

		public function userNameAlreadyExists ($userName) {
			$query = $this->_pdo->prepare("SELECT * FROM `usrs` WHERE `userName` = :userName");
			$query->bindParam(':userName', $userName, PDO::PARAM_STR);
			$query->execute();
			$rtrnv = $query->fetch();
			if ($rtrnv)
				return TRUE;
			else
				return FALSE;
		}

		public function userDetailsInsertion($userName, $eMail, $passWord, $HashKey, $toNotify) {
			$query = $this->_pdo->prepare("INSERT INTO `usrs` (`userName`, `eMail`, `passWord`, `HashKey`, `Activity`, `toNotify`)
										VALUES (:userName, :eMail, :passWord, :HashKey, 0, :toNotify);");
			$query->bindParam(':userName', $userName, PDO::PARAM_STR);
			$query->bindParam(':eMail', $eMail, PDO::PARAM_STR);
			$query->bindParam(':passWord', $passWord, PDO::PARAM_STR);
			$query->bindParam(':HashKey', $HashKey, PDO::PARAM_STR);
			$query->bindParam(':toNotify', $toNotify, PDO::PARAM_BOOL);
			$query->execute();
		}

		public function activateAccount($HashKey) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `Activity` = 1 WHERE `usrs`.`HashKey` = :HashKey");
			$query->bindParam(':HashKey', $HashKey, PDO::PARAM_STR);
			$query->execute();
		}

		public function findKeyMatch($HashKey) {
			$query = $this->_pdo->prepare("SELECT * FROM `usrs` WHERE `HashKey` = :HashKey LIMIT 1");
			$query->bindParam(':HashKey', $HashKey, PDO::PARAM_STR);
			$query->execute();
			$rtrnv = $query->fetch();
			return ($rtrnv);
		}

		public function findNameMatch($userName) {
			$query = $this->_pdo->prepare("SELECT * FROM `usrs` WHERE `userName` = :userName LIMIT 1");
			$query->bindParam(':userName', $userName, PDO::PARAM_STR);
			$query->execute();
			$rtrnv = $query->fetch();
			return ($rtrnv);
		}

		public function updateUserName($crntName, $newName) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `userName` = :newName WHERE `usrs`.`userName` = :crntName");
			$query->bindParam(":newName", $newName);
			$query->bindParam(":crntName", $crntName);
			$query->execute();
		}

		public function updatePassWord($userName, $newPassWord) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `passWord` = :newPassWord WHERE `usrs`.`userName` = :userName");
			$query->bindParam(":userName", $userName);
			$query->bindParam(":newPassWord", $newPassWord);
			$query->execute();
		}

		public function resetPassWord($HashKey, $newPassWord) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `passWord` = :newPassWord WHERE `usrs`.`HashKey` = :HashKey");
			$query->bindParam(":newPassWord", $newPassWord);
			$query->bindParam(":HashKey", $HashKey);
			$query->execute();
		}

		public function updateTheEmail($userName, $newEmail) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `eMail` = :newEmail WHERE `usrs`.`userName` = :userName");
			$query->bindParam(":newEmail", $newEmail);
			$query->bindParam(":userName", $userName);
			$query->execute();
		}

		public function updateNotification($userName, $toNotify) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `toNotify` = :toNotify WHERE `usrs`.`userName` = :userName");
			$query->bindParam(":toNotify", $toNotify);
			$query->bindParam(":userName", $userName);
			$query->execute();
		}

		//---

		public function imgsTableCreate() {
			$this->_pdo->exec("CREATE TABLE IF NOT EXISTS `Demo`.`imgs`(
			`Id` INT NOT NULL AUTO_INCREMENT ,
			`Img` LONGTEXT CHARACTER SET utf8 NULL DEFAULT NULL ,
			`userId` VARCHAR(255) NULL DEFAULT NULL ,
			PRIMARY KEY (`Id`)) ENGINE = InnoDB;");
		}

		public function imgIntoDBInsert($Img, $userId) {
			$query = $this->_pdo->prepare("INSERT INTO `imgs` (`Img`, `userId`)VALUES (:Img, :userId);");
			$query->bindParam(":Img", $Img);
			$query->bindParam(":userId", $userId);
			$query->execute();
		}

		public function imgFromDBSelect() {
			$query = $this->_pdo->prepare("SELECT `Img` FROM `imgs` ORDER BY `Id` DESC");
			$query->execute();
			$rows = $query->fetchAll();
			return ($rows);
		}

		public function imgFromDBFetch() {
			$query = $this->_pdo->prepare("SELECT `Id`,`Img`,`userId` FROM `imgs` ORDER BY `Id` DESC");
			$query->execute();
			$rows = $query->fetchAll();
			return ($rows);
		}

		public function imgFromDBRemove($Id) {
			$query = $this->_pdo->prepare("DELETE FROM `imgs` WHERE `imgs`.`Id` = :Id");
			$query->bindParam(":Id", $Id);
			$query->execute();
		}
	}
