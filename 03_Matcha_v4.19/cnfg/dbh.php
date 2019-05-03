<?php

	class db_handle {

		private $_pdo;

		public static	$INSTANCE;
		private			$db_username = "root";
		private			$db_password = "12345r";
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
					$this->whoLikesWhoTableCreate();
					$this->chatTableCreate();
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
			`fullName` VARCHAR(255) NULL DEFAULT NULL ,
			`eMail` VARCHAR(255) NULL DEFAULT NULL ,
			`passWord` VARCHAR(255) NULL DEFAULT NULL ,
			`HashKey` VARCHAR(255) NULL DEFAULT NULL , 
			`Activity` BOOLEAN NULL DEFAULT FALSE ,
			`Cnctvity` BOOLEAN NULL DEFAULT FALSE ,
			`Gender` INT NULL DEFAULT NULL ,
			`Sexuality` VARCHAR(255) NULL DEFAULT NULL ,
			`Biography` VARCHAR(255) NULL DEFAULT NULL ,
			`Interests` VARCHAR(255) NULL DEFAULT NULL ,
			`fameRate` INT(255) NULL DEFAULT 0 ,
			`Location` VARCHAR(255) NULL DEFAULT NULL ,
			`Img1` LONGTEXT CHARACTER SET utf8 NULL DEFAULT NULL ,
			`Img2` LONGTEXT CHARACTER SET utf8 NULL DEFAULT NULL ,
			`Img3` LONGTEXT CHARACTER SET utf8 NULL DEFAULT NULL ,
			`Img4` LONGTEXT CHARACTER SET utf8 NULL DEFAULT NULL ,
			`Img5` LONGTEXT CHARACTER SET utf8 NULL DEFAULT NULL ,
			`LastCnctTime` VARCHAR(255) NULL DEFAULT NULL ,
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

		public function userDetailsInsertion($userName, $fullName, $eMail, $passWord, $HashKey, $Gender, $Sexuality, $Biography, $Interests) {
			$query = $this->_pdo->prepare("INSERT INTO `usrs` (`userName`, `fullName`, `eMail`, `passWord`, `HashKey`, `Activity`, `Cnctvity`, `Gender`, `Sexuality`, `Biography`, `Interests`, `fameRate`)
										VALUES (:userName, :fullName, :eMail, :passWord, :HashKey, 0, 0, :Gender, :Sexuality, :Biography, :Interests, 0);");
			$query->bindParam(':userName', $userName, PDO::PARAM_STR);
			$query->bindParam(':fullName', $fullName, PDO::PARAM_STR);
			$query->bindParam(':eMail', $eMail, PDO::PARAM_STR);
			$query->bindParam(':passWord', $passWord, PDO::PARAM_STR);
			$query->bindParam(':HashKey', $HashKey, PDO::PARAM_STR);
			$query->bindParam(':Gender', $Gender, PDO::PARAM_STR);
			$query->bindParam(':Sexuality', $Sexuality, PDO::PARAM_STR);
			$query->bindParam(':Biography', $Biography, PDO::PARAM_STR);
			$query->bindParam(':Interests', $Interests, PDO::PARAM_STR);
			$query->execute();
		}

		// Check https://www.geoplugin.com/webservices/php

		public function userLocationUpdating($userName) {
			$ipAdress = 0;
			$Location = var_export(unserialize(file_get_contents('http://www.geoplugin.net/php.gp?ip='.$ipAdress)));
			$yourCity = $Location['geoplugin_city'];
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `Location` = :yourCity WHERE `usrs`.`userName` = :userName");
			$query->bindParam(':yourCity', $yourCity, PDO::PARAM_STR);
			$query->bindParam(':userName', $userName, PDO::PARAM_STR);
			$query->execute();
		}

		public function activateAccount($HashKey) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `Activity` = 1 WHERE `usrs`.`HashKey` = :HashKey");
			$query->bindParam(':HashKey', $HashKey, PDO::PARAM_STR);
			$query->execute();
		}

		public function getConnected($Id) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `Cnctvity` = 1 WHERE `usrs`.`Id` = :Id");
			$query->bindParam(':Id', $Id, PDO::PARAM_STR);
			$query->execute();
		}

		public function getUnconnected($Id) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `Cnctvity` = 0 WHERE `usrs`.`Id` = :Id");
			$query->bindParam(':Id', $Id, PDO::PARAM_STR);
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

		public function LastCnctTime($some1) {
			$timestring = date("l jS \of F Y h:i:s A");
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `LastCnctTime` = :timestring WHERE Id = :some1;");
			$query->bindParam(':timestring', $timestring);
			$query->bindParam(':some1', $some1, PDO::PARAM_STR);
			$query->execute();
		}

		//---

		public function imgIntoDBInsert($Img, $userName) {
			$query = $this->_pdo->prepare("INSERT INTO `usrs` (`:ImgN`) VALUES (:Img) WHERE userName = :userName;");
			$query->bindParam(":Img", $Img);
			$query->bindParam(":userName", $userName);
			if (imgFromDBSelect("Img1") == NULL)
				$query->bindParam(":ImgN", "Img1");
			else if (imgFromDBSelect("Img2") == NULL)
				$query->bindParam(":ImgN", "Img2");
			else if (imgFromDBSelect("Img3") == NULL)
				$query->bindParam(":ImgN", "Img3");
			else if (imgFromDBSelect("Img4") == NULL)
				$query->bindParam(":ImgN", "Img4");
			else if (imgFromDBSelect("Img5") == NULL)
				$query->bindParam(":ImgN", "Img5");
			else
				$query->bindParam(":ImgN", "Img5");
			$query->execute();
		}

		public function imgFromDBSelect($ImgN, $userId) {
			$query = $this->_pdo->prepare("SELECT `:ImgN` FROM `usrs` WHERE Id = :userId;");
			$query->bindParam(":ImgN", $ImgN);
			$query->bindParam(":userId", $userId);
			$query->execute();
			$rows = $query->fetchAll();
			return ($rows);
		}

		public function usrsFromDBFetch() {
			$query = $this->_pdo->prepare("SELECT `Id`, `fullName`, `Cnctvity`, `Gender`, `Sexuality`, `Biography`, `Interests`, `fameRate`, `Img1`, `Img2`, `Img3`, `Img4`, `Img5`, `LastCnctTime`, `Location` FROM `usrs` WHERE Activity = 1 ORDER BY `Id` DESC");
			$query->execute();
			$rows = $query->fetchAll();
			return ($rows);
		}

		public function imgFromDBRemove($Id) {
			$query = $this->_pdo->prepare("DELETE FROM `imgs` WHERE `imgs`.`Id` = :Id");
			$query->bindParam(":Id", $Id);
			$query->execute();
		}

		public function whoLikesWhoTableCreate() {
			$this->_pdo->exec("CREATE TABLE IF NOT EXISTS `Demo`.`whoLikesWho`(
			`ActionId` INT NOT NULL AUTO_INCREMENT ,
			`Liker` INT(255) NULL DEFAULT NULL ,
			`Liked` INT(255) NULL DEFAULT NULL ,
			`Block` INT(255) NULL DEFAULT NULL ,
			PRIMARY KEY (`ActionId`)) ENGINE = InnoDB;");
		}

		public function fameRate($some1) {
			$query = $this->_pdo->prepare("SELECT COUNT `Liked` FROM `wholikeswho` WHERE `Liked` = :some1");
			$query->bindParam(':some1', $some1, PDO::PARAM_STR);
			$query->execute();
			$rows = $query->fetchAll();
			if ($rows)
				return ($rows);
			else
				return (0);
		}

		public function some1likessome1($Liker, $Liked) {
			$query = $this->_pdo->prepare("INSERT INTO `wholikeswho` (`Liker`, `Liked`)
				VALUES (:Liker, :Liked);");
			$query->bindParam(':Liker', $Liker, PDO::PARAM_STR);
			$query->bindParam(':Liked', $Liked, PDO::PARAM_STR);
			$query->execute();
		}

		public function incrementFameRate($some1) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `fameRate` = `fameRate` + 1 WHERE `usrs`.`Id` = :Id");
			$query->bindParam(':Id', $some1, PDO::PARAM_STR);
			$query->execute();
		}

		public function isntSome1ILike($mySelf, $some1) {
			$query = $this->_pdo->prepare("SELECT * FROM `wholikeswho` WHERE `Liker` = :mySelf AND `Liked` = :some1 LIMIT 1");
			$query->bindParam(':mySelf', $mySelf, PDO::PARAM_STR);
			$query->bindParam(':some1', $some1, PDO::PARAM_STR);
			$query->execute();
			$rows = $query->fetchAll();
			if ($rows)
				return (0);
			else
				return (1);
		}

		public function some1unlikessome1($unLiker, $unLiked) {
			$query = $this->_pdo->prepare("DELETE FROM `wholikeswho` WHERE `wholikeswho`.`Liker` = :unLiker AND `wholikeswho`.`Liked` = :unLiked");
			$query->bindParam(":unLiker", $unLiker);
			$query->bindParam(":unLiked", $unLiked);
			$query->execute();
		}

		public function decrementFameRate($some1) {
			$query = $this->_pdo->prepare("UPDATE `usrs` SET `fameRate` = `fameRate` - 1 WHERE `usrs`.`Id` = :Id");
			$query->bindParam(':Id', $some1, PDO::PARAM_STR);
			$query->execute();
		}

		public function some1BlockedSome1($mySelf, $some1) {
			$query = $this->_pdo->prepare("INSERT INTO `wholikeswho` (`Liker`, `Block`)
				VALUES (:Liker, :Block);");
			$query->bindParam(':Liker', $mySelf, PDO::PARAM_STR);
			$query->bindParam(':Block', $some1, PDO::PARAM_STR);
			$query->execute();
		}

		public function isntBlocked($mySelf, $some1) {
			$query = $this->_pdo->prepare("SELECT * FROM `wholikeswho` WHERE `Liker` = :mySelf AND `Block` = :some1 LIMIT 1");
			$query->bindParam(':mySelf', $mySelf, PDO::PARAM_STR);
			$query->bindParam(':some1', $some1, PDO::PARAM_STR);
			$query->execute();
			$rows = $query->fetchAll();
			if ($rows)
				return (0);
			else
				return (1);
		}

		public function weBothLikeEachOther($mySelf, $some1) {
			$query0 = $this->_pdo->prepare("SELECT * FROM `wholikeswho` WHERE `Liker` = :mySelf AND `Liked` = :some1 LIMIT 1");
			$query0->bindParam(':mySelf', $mySelf, PDO::PARAM_STR);
			$query0->bindParam(':some1', $some1, PDO::PARAM_STR);
			$query0->execute();
			$rows0 = $query0->fetchAll();
			$query1 = $this->_pdo->prepare("SELECT * FROM `wholikeswho` WHERE `Liker` = :some1 AND `Liked` = :mySelf LIMIT 1");
			$query1->bindParam(':some1', $some1, PDO::PARAM_STR);
			$query1->bindParam(':mySelf', $mySelf, PDO::PARAM_STR);
			$query1->execute();
			$rows1 = $query1->fetchAll();
			if ($rows0 && $rows1)
				return (1);
			else
				return (0);
		}

		public function chatTableCreate() {
			$this->_pdo->exec("CREATE TABLE IF NOT EXISTS `Demo`.`chat`(
			`MsgNo` INT NOT NULL AUTO_INCREMENT ,
			`chattedFrom` INT(255) NULL DEFAULT NULL ,
			`chattedTo` INT(255) NULL DEFAULT NULL ,
			`Content` VARCHAR(255) NULL DEFAULT NULL ,
			`timeStmp` INT NULL DEFAULT NULL ,
			PRIMARY KEY (`MsgNo`)) ENGINE = InnoDB;");
		}
	}
