-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema killteam
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema killteam
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `killteam` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `killteam` ;

-- -----------------------------------------------------
-- Table `killteam`.`Operative`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Operative` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `fireteamid` VARCHAR(250) NOT NULL,
  `opseq` INT NULL DEFAULT '0',
  `opid` VARCHAR(50) NOT NULL,
  `opname` VARCHAR(250) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `edition` VARCHAR(45) NULL DEFAULT 'kt24',
  `M` VARCHAR(15) NULL DEFAULT NULL,
  `APL` VARCHAR(15) NULL DEFAULT NULL,
  `GA` VARCHAR(15) NULL DEFAULT NULL,
  `DF` VARCHAR(15) NULL DEFAULT NULL,
  `SV` VARCHAR(15) NULL DEFAULT NULL,
  `W` VARCHAR(15) NULL DEFAULT NULL,
  `keywords` VARCHAR(4000) NULL DEFAULT NULL,
  `fireteammax` INT NULL DEFAULT '0',
  `specialisms` VARCHAR(50) NULL DEFAULT '',
  PRIMARY KEY (`factionid`, `killteamid`, `fireteamid`, `opid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `IX_Operative_FactionIdKillTeamIdFireTeamID` ON `killteam`.`Operative` (`factionid` ASC, `killteamid` ASC, `fireteamid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Ability`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Ability` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `fireteamid` VARCHAR(50) NOT NULL,
  `opid` VARCHAR(50) NOT NULL,
  `abilityid` VARCHAR(50) NOT NULL,
  `title` VARCHAR(200) NOT NULL,
  `description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`killteamid`, `fireteamid`, `opid`, `abilityid`, `factionid`),
  CONSTRAINT `FK_Ability_Operative`
    FOREIGN KEY (`factionid` , `killteamid` , `fireteamid` , `opid`)
    REFERENCES `killteam`.`Operative` (`factionid` , `killteamid` , `fireteamid` , `opid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `FK_Ability_Operative_idx` ON `killteam`.`Ability` (`factionid` ASC, `killteamid` ASC, `fireteamid` ASC, `opid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Equipment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Equipment` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `fireteamid` VARCHAR(50) NULL DEFAULT '',
  `opid` VARCHAR(50) NULL DEFAULT '',
  `eqid` VARCHAR(50) NOT NULL,
  `eqseq` INT NULL DEFAULT '0',
  `eqpts` VARCHAR(10) NULL DEFAULT NULL,
  `eqname` VARCHAR(250) NULL DEFAULT NULL,
  `eqdescription` TEXT NULL DEFAULT NULL,
  `eqtype` VARCHAR(45) NULL DEFAULT NULL,
  `eqvar1` VARCHAR(45) NULL DEFAULT NULL,
  `eqvar2` VARCHAR(45) NULL DEFAULT NULL,
  `eqvar3` VARCHAR(45) NULL DEFAULT NULL,
  `eqvar4` VARCHAR(45) NULL DEFAULT NULL,
  `eqcategory` VARCHAR(200) NULL DEFAULT 'Equipment',
  PRIMARY KEY (`factionid`, `killteamid`, `eqid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `FK_Equipment_Killteam_idx` ON `killteam`.`Equipment` (`factionid` ASC, `killteamid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Event` (
  `eventid` INT NOT NULL AUTO_INCREMENT,
  `datestamp` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `sessiontype` VARCHAR(50) NULL DEFAULT '',
  `userid` VARCHAR(45) NULL DEFAULT NULL,
  `eventtype` VARCHAR(50) NULL DEFAULT NULL,
  `action` VARCHAR(45) NULL DEFAULT NULL,
  `label` VARCHAR(45) NULL DEFAULT NULL,
  `var1` VARCHAR(45) NULL DEFAULT NULL,
  `var2` VARCHAR(45) NULL DEFAULT NULL,
  `var3` VARCHAR(45) NULL DEFAULT NULL,
  `url` VARCHAR(500) NULL DEFAULT '',
  `userip` VARCHAR(250) NULL DEFAULT '',
  `useragent` VARCHAR(500) NULL DEFAULT '',
  `referrer` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`eventid`))
ENGINE = InnoDB
AUTO_INCREMENT = 15523047
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `IX_TAL` ON `killteam`.`Event` (`userid` ASC, `eventtype` ASC, `action` ASC, `label` ASC) INVISIBLE;

CREATE INDEX `IX_VAR1` ON `killteam`.`Event` (`var1` ASC, `eventtype` ASC, `action` ASC, `label` ASC) VISIBLE;

CREATE INDEX `IX_datestamp` ON `killteam`.`Event` (`datestamp` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Event_BKP_20240720`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Event_BKP_20240720` (
  `eventid` INT NOT NULL AUTO_INCREMENT,
  `datestamp` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `sessiontype` VARCHAR(50) NULL DEFAULT '',
  `userid` VARCHAR(45) NULL DEFAULT NULL,
  `eventtype` VARCHAR(50) NULL DEFAULT NULL,
  `action` VARCHAR(45) NULL DEFAULT NULL,
  `label` VARCHAR(45) NULL DEFAULT NULL,
  `var1` VARCHAR(45) NULL DEFAULT NULL,
  `var2` VARCHAR(45) NULL DEFAULT NULL,
  `var3` VARCHAR(45) NULL DEFAULT NULL,
  `url` VARCHAR(500) NULL DEFAULT '',
  `userip` VARCHAR(250) NULL DEFAULT '',
  `useragent` VARCHAR(500) NULL DEFAULT '',
  `referrer` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`eventid`))
ENGINE = InnoDB
AUTO_INCREMENT = 14186874
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `IX_TAL` ON `killteam`.`Event_BKP_20240720` (`userid` ASC, `eventtype` ASC, `action` ASC, `label` ASC) INVISIBLE;

CREATE INDEX `IX_VAR1` ON `killteam`.`Event_BKP_20240720` (`var1` ASC, `eventtype` ASC, `action` ASC, `label` ASC) VISIBLE;

CREATE INDEX `IX_datestamp` ON `killteam`.`Event_BKP_20240720` (`datestamp` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Faction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Faction` (
  `factionid` VARCHAR(10) NOT NULL,
  `seq` INT NULL DEFAULT NULL,
  `factionname` VARCHAR(250) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`factionid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `killteam`.`Killteam`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Killteam` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `edition` VARCHAR(45) NULL DEFAULT 'kt24',
  `killteamname` VARCHAR(250) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `killteamcomp` TEXT NULL DEFAULT NULL,
  `customkeyword` VARCHAR(250) NULL DEFAULT '',
  PRIMARY KEY (`factionid`, `killteamid`),
  CONSTRAINT `FK_Killteam_Faction`
    FOREIGN KEY (`factionid`)
    REFERENCES `killteam`.`Faction` (`factionid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `FK_Killteam_Faction_idx` ON `killteam`.`Killteam` (`factionid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Fireteam`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Fireteam` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `fireteamid` VARCHAR(200) NOT NULL,
  `seq` INT NULL DEFAULT '0',
  `description` TEXT NULL DEFAULT NULL,
  `killteammax` INT NULL DEFAULT NULL,
  `fireteamname` VARCHAR(200) NULL DEFAULT NULL,
  `archetype` VARCHAR(250) NULL DEFAULT NULL,
  `fireteamcomp` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`factionid`, `killteamid`, `fireteamid`),
  CONSTRAINT `FK_Fireteam_Killteam`
    FOREIGN KEY (`factionid` , `killteamid`)
    REFERENCES `killteam`.`Killteam` (`factionid` , `killteamid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `FK_Fireteam_Killteam_idx` ON `killteam`.`Fireteam` (`factionid` ASC, `killteamid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Ploy`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Ploy` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(10) NOT NULL,
  `ploytype` VARCHAR(250) NOT NULL,
  `ployid` VARCHAR(50) NOT NULL,
  `ployname` VARCHAR(250) NULL DEFAULT NULL,
  `CP` VARCHAR(10) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`factionid`, `killteamid`, `ploytype`, `ployid`),
  CONSTRAINT `FK_Ploy_Killteam`
    FOREIGN KEY (`factionid` , `killteamid`)
    REFERENCES `killteam`.`Killteam` (`factionid` , `killteamid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `killteam`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`User` (
  `userid` VARCHAR(50) NOT NULL,
  `username` VARCHAR(250) NULL DEFAULT NULL,
  `passhash` VARCHAR(500) NULL DEFAULT NULL,
  `createddate` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `username_UNIQUE` ON `killteam`.`User` (`username` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Roster`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Roster` (
  `userid` VARCHAR(50) NOT NULL,
  `rosterid` VARCHAR(50) NOT NULL,
  `seq` INT NULL DEFAULT NULL,
  `rostername` VARCHAR(250) NULL DEFAULT NULL,
  `factionid` VARCHAR(50) NULL DEFAULT NULL,
  `killteamid` VARCHAR(50) NULL DEFAULT NULL,
  `notes` VARCHAR(2000) NULL DEFAULT '',
  `keyword` VARCHAR(250) NULL DEFAULT '',
  `TP` INT NULL DEFAULT '1',
  `CP` INT NULL DEFAULT '2',
  `VP` INT NULL DEFAULT '2',
  `RP` INT NULL DEFAULT '0',
  `spotlight` INT NULL DEFAULT '0',
  `hascustomportrait` INT NULL DEFAULT '0',
  `portraitcopyok` INT NULL DEFAULT '0',
  `viewcount` INT NULL DEFAULT '0',
  `importcount` INT NULL DEFAULT '0',
  `ployids` VARCHAR(250) NULL DEFAULT NULL,
  `tacopids` VARCHAR(250) NULL DEFAULT NULL,
  `reqpts` INT NULL DEFAULT '0',
  `stratnotes` TEXT NULL DEFAULT NULL,
  `eqnotes` TEXT NULL DEFAULT NULL,
  `specopnotes` TEXT NULL DEFAULT NULL,
  `createddate` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userid`, `rosterid`),
  CONSTRAINT `FK_Roster_User`
    FOREIGN KEY (`userid`)
    REFERENCES `killteam`.`User` (`userid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `rosterid_UNIQUE` ON `killteam`.`Roster` (`rosterid` ASC) VISIBLE;

CREATE INDEX `IX_Roster_rosterid` ON `killteam`.`Roster` (`rosterid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`RosterOperative`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`RosterOperative` (
  `userid` VARCHAR(50) NOT NULL,
  `rosterid` VARCHAR(50) NOT NULL,
  `rosteropid` VARCHAR(50) NOT NULL,
  `seq` INT NULL DEFAULT NULL,
  `opname` VARCHAR(250) NULL DEFAULT NULL,
  `factionid` VARCHAR(50) NULL DEFAULT NULL,
  `killteamid` VARCHAR(50) NULL DEFAULT NULL,
  `fireteamid` VARCHAR(50) NULL DEFAULT NULL,
  `opid` VARCHAR(50) NULL DEFAULT NULL,
  `wepids` VARCHAR(250) NULL DEFAULT NULL,
  `eqids` VARCHAR(250) NULL DEFAULT NULL,
  `curW` INT NULL DEFAULT NULL,
  `notes` VARCHAR(2000) NULL DEFAULT NULL,
  `activated` TINYINT NULL DEFAULT '0',
  `hidden` TINYINT NULL DEFAULT '0',
  `xp` INT NULL DEFAULT '0',
  `oporder` VARCHAR(45) NULL DEFAULT 'conceal',
  `hascustomportrait` INT NULL DEFAULT '0',
  `specialism` VARCHAR(50) NULL DEFAULT '',
  `isinjured` TINYINT NULL DEFAULT '0',
  `rested` INT NULL DEFAULT '0',
  PRIMARY KEY (`userid`, `rosterid`, `rosteropid`),
  CONSTRAINT `FK_RosterOperative_Roster`
    FOREIGN KEY (`userid` , `rosterid`)
    REFERENCES `killteam`.`Roster` (`userid` , `rosterid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `rosteropid_UNIQUE` ON `killteam`.`RosterOperative` (`rosteropid` ASC) VISIBLE;

CREATE INDEX `IX_RosterOperative_rosteropid` ON `killteam`.`RosterOperative` (`rosteropid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`TacOp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`TacOp` (
  `tacopid` VARCHAR(50) NOT NULL,
  `edition` VARCHAR(45) NULL DEFAULT 'kt21',
  `archetype` VARCHAR(50) NULL DEFAULT NULL,
  `tacopseq` INT NULL DEFAULT NULL,
  `title` VARCHAR(50) NULL DEFAULT NULL,
  `description` VARCHAR(2000) NULL DEFAULT NULL,
  PRIMARY KEY (`tacopid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `killteam`.`RosterTacOp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`RosterTacOp` (
  `userid` VARCHAR(50) NOT NULL,
  `rosterid` VARCHAR(50) NOT NULL,
  `tacopid` VARCHAR(50) NOT NULL,
  `revealed` TINYINT NULL DEFAULT '0',
  `VP1` TINYINT NULL DEFAULT '0',
  `VP2` TINYINT NULL DEFAULT '0',
  PRIMARY KEY (`userid`, `rosterid`, `tacopid`),
  CONSTRAINT `FK_RosterTacOp_Roster`
    FOREIGN KEY (`userid` , `rosterid`)
    REFERENCES `killteam`.`Roster` (`userid` , `rosterid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_RosterTacOp_TacOp`
    FOREIGN KEY (`tacopid`)
    REFERENCES `killteam`.`TacOp` (`tacopid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_RosterTacOp_User`
    FOREIGN KEY (`userid`)
    REFERENCES `killteam`.`User` (`userid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `FK_RosterTacOp_TacOp_idx` ON `killteam`.`RosterTacOp` (`tacopid` ASC) VISIBLE;

CREATE INDEX `FK_RosterTacOp_User_idx` ON `killteam`.`RosterTacOp` (`userid` ASC) VISIBLE;

CREATE INDEX `FK_RosterTacOp_Roster_idx` ON `killteam`.`RosterTacOp` (`userid` ASC, `rosterid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`Session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Session` (
  `sessionid` VARCHAR(50) NOT NULL,
  `userid` VARCHAR(50) NULL DEFAULT NULL,
  `lastactivity` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`sessionid`),
  CONSTRAINT `FK_Session_User`
    FOREIGN KEY (`userid`)
    REFERENCES `killteam`.`User` (`userid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `FK_Session_Player_idx` ON `killteam`.`Session` (`userid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`UniqueAction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`UniqueAction` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `fireteamid` VARCHAR(50) NOT NULL,
  `opid` VARCHAR(50) NOT NULL,
  `uniqueactionid` VARCHAR(50) NOT NULL,
  `title` VARCHAR(200) NULL DEFAULT NULL,
  `AP` INT NULL DEFAULT '1',
  `description` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`factionid`, `killteamid`, `fireteamid`, `opid`, `uniqueactionid`),
  CONSTRAINT `FK_UniqueActions_Operative`
    FOREIGN KEY (`factionid` , `killteamid` , `fireteamid` , `opid`)
    REFERENCES `killteam`.`Operative` (`factionid` , `killteamid` , `fireteamid` , `opid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `killteam`.`UserSetting`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`UserSetting` (
  `userid` VARCHAR(50) NOT NULL,
  `key` VARCHAR(50) NOT NULL,
  `value` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`userid`, `key`),
  CONSTRAINT `FK_Setting_User`
    FOREIGN KEY (`userid`)
    REFERENCES `killteam`.`User` (`userid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `killteam`.`Weapon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`Weapon` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `fireteamid` VARCHAR(50) NOT NULL,
  `opid` VARCHAR(50) NOT NULL,
  `wepid` VARCHAR(50) NOT NULL,
  `wepseq` INT NULL DEFAULT '0',
  `wepname` VARCHAR(250) NULL DEFAULT NULL,
  `weptype` VARCHAR(1) NULL DEFAULT NULL,
  `isdefault` SMALLINT NULL DEFAULT '0',
  PRIMARY KEY (`factionid`, `killteamid`, `fireteamid`, `opid`, `wepid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `FK_weapon_operative_idx` ON `killteam`.`Weapon` (`killteamid` ASC, `fireteamid` ASC, `opid` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `killteam`.`WeaponProfile`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `killteam`.`WeaponProfile` (
  `factionid` VARCHAR(10) NOT NULL,
  `killteamid` VARCHAR(50) NOT NULL,
  `fireteamid` VARCHAR(50) NOT NULL,
  `opid` VARCHAR(50) NOT NULL,
  `wepid` VARCHAR(50) NOT NULL,
  `profileid` VARCHAR(200) NOT NULL,
  `name` VARCHAR(200) NULL DEFAULT NULL,
  `A` VARCHAR(5) NULL DEFAULT NULL,
  `BS` VARCHAR(5) NULL DEFAULT NULL,
  `D` VARCHAR(5) NULL DEFAULT NULL,
  `SR` VARCHAR(4000) NULL DEFAULT NULL,
  PRIMARY KEY (`factionid`, `killteamid`, `fireteamid`, `opid`, `wepid`, `profileid`),
  CONSTRAINT `FK_WeaponProfile_Weapon`
    FOREIGN KEY (`factionid` , `killteamid` , `fireteamid` , `opid` , `wepid`)
    REFERENCES `killteam`.`Weapon` (`factionid` , `killteamid` , `fireteamid` , `opid` , `wepid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `killteam` ;

-- -----------------------------------------------------
-- procedure FixDupRosterOpId
-- -----------------------------------------------------

DELIMITER $$
USE `killteam`$$
CREATE DEFINER=`vince`@`%` PROCEDURE `FixDupRosterOpId`()
BEGIN
	DECLARE dupcount INT;
    DECLARE oldrosteropid VARCHAR(10);
    DECLARE newrosteropid VARCHAR(10);
    DECLARE updateuserid VARCHAR(10);
    
    DROP TABLE IF EXISTS Commands;
    CREATE TEMPORARY TABLE Commands (command VARCHAR(4000));
    
    SELECT COUNT(*) INTO dupcount FROM (SELECT rosteropid, COUNT(*) AS DupCount FROM RosterOperative GROUP BY rosteropid HAVING COUNT(*) > 1) A;
    
    WHILE dupcount > 0 DO
		SELECT rosteropid INTO oldrosteropid FROM (SELECT rosteropid, COUNT(*) AS DupCount FROM RosterOperative GROUP BY rosteropid HAVING COUNT(*) > 1 LIMIT 1) A;
        SELECT userid INTO updateuserid FROM RosterOperative WHERE rosteropid = oldrosteropid LIMIT 1;
        SET newrosteropid = CONCAT(oldrosteropid, LEFT(MD5(RAND()), 5));
        
        INSERT INTO Commands (command)
        SELECT CONCAT('UPDATE RosterOperative SET rosteropid = ''', newrosteropid, ''' WHERE userid = ''', updateuserid, ''' AND rosteropid = ''', oldrosteropid, '''');
        
        UPDATE RosterOperative SET rosteropid = newrosteropid WHERE userid = updateuserid AND rosteropid = oldrosteropid;
        
        #Now check for more roster op dups
		SELECT COUNT(*) INTO dupcount FROM (SELECT rosteropid, COUNT(*) FROM RosterOperative GROUP BY rosteropid HAVING COUNT(*) > 1) A;
        
        SELECT dupcount AS DupCount;
    END WHILE;
    
    SELECT * FROM Commands;
    
    DROP TABLE Commands;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function SPLIT_STR
-- -----------------------------------------------------

DELIMITER $$
USE `killteam`$$
CREATE DEFINER=`vince`@`%` FUNCTION `SPLIT_STR`(
  x VARCHAR(255),
  delim VARCHAR(12),
  pos INT
) RETURNS varchar(255) CHARSET utf8mb4
    READS SQL DATA
    DETERMINISTIC
RETURN REPLACE(SUBSTRING(SUBSTRING_INDEX(x, delim, pos),
       LENGTH(SUBSTRING_INDEX(x, delim, pos - 1)) + 1),
       delim, '')$$

DELIMITER ;

-- -----------------------------------------------------
-- View `killteam`.`EventLogView`
-- -----------------------------------------------------
USE `killteam`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`vince`@`%` SQL SECURITY DEFINER VIEW `killteam`.`EventLogView` AS select `E`.`eventid` AS `eventid`,`E`.`datestamp` AS `datestamp`,(case concat(`E`.`eventtype`,'|',`E`.`action`) when 'page|view' then concat(ifnull(concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a>'),'[Anon]'),' viewed page <a href="',`E`.`url`,'">',`E`.`url`,'</a>') when 'roster|addop' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> added ',`O`.`opname`,' "',`RO`.`opname`,'" to <a href="/fa/',`K`.`factionid`,'/kt/',`K`.`killteamid`,'">',`K`.`killteamname`,'</a> roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>') when 'roster|create' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> created new <a href="/fa/',`K`.`factionid`,'/kt/',`K`.`killteamid`,'">',`K`.`killteamname`,'</a> roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>') when 'roster|importv1' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> imported a v1 roster') when 'roster|gettext' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> viewed roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>','\'s text description') when 'roster|cloneop' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> cloned a new operative into roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>') when 'dashboard|TP' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a>\'s ',' roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>',(case when (`E`.`var2` = 1) then ' moved to the next TP' else ' went back to the previous TP' end)) when 'session|signup' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> signed up') when 'dashboard|W' then concat(`RO`.`opname`,' of ','<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a>\'s ',' roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>',' ',(case when (`E`.`var2` = 1) then 'gained' else 'lost' end),' 1 Wound') when 'dashboard|CP' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a>\'s ',' roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>',' ',(case when (`E`.`var2` = 1) then 'gained' else 'used' end),' 1 CP') when 'dashboard|VP' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a>\'s ',' roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>',' ',(case when (`E`.`var2` = 1) then 'gained' else 'lost' end),' 1 VP') when 'dashboard|RP' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a>\'s ',' roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>',' ',(case when (`E`.`var2` = 1) then 'gained' else 'lost' end),' 1 RP') when 'roster|print' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> printed their "',(case `E`.`label` when 'roster' then `R`.`rostername` else `RO`.`opname` end),(case `E`.`label` when 'roster' then '" roster' else '" operative' end)) when 'roster|opportrait' then concat('<a href="/u/',`U`.`userid`,'">',`U`.`username`,'</a> added a new ',(case when (`E`.`label` = 'custom') then 'custom' else 'default' end),' portrait for "',`RO`.`opname`,'" of ',' roster <a href="/r/',`R`.`rosterid`,'">',`R`.`rostername`,'</a>') else '' end) AS `ActionLog`,`E`.`userid` AS `userid`,`E`.`userip` AS `userip`,`E`.`eventtype` AS `eventtype`,`E`.`action` AS `action`,`E`.`label` AS `label`,`E`.`var1` AS `var1`,`E`.`var2` AS `var2`,`E`.`var3` AS `var3`,`U`.`username` AS `username`,`R`.`rostername` AS `rostername`,`RO`.`opname` AS `opname`,`O`.`opname` AS `optype` from (((((`killteam`.`Event` `E` left join `killteam`.`User` `U` on((`U`.`userid` = `E`.`userid`))) left join `killteam`.`Roster` `R` on((`R`.`rosterid` = `E`.`var1`))) left join `killteam`.`Killteam` `K` on(((`K`.`factionid` = `R`.`factionid`) and (`K`.`killteamid` = `R`.`killteamid`)))) left join `killteam`.`RosterOperative` `RO` on(((`RO`.`rosterid` = `E`.`var1`) and (`RO`.`rosteropid` = `E`.`var2`)))) left join `killteam`.`Operative` `O` on(((`O`.`factionid` = `RO`.`factionid`) and (`O`.`killteamid` = `RO`.`killteamid`) and (`O`.`fireteamid` = `RO`.`fireteamid`) and (`O`.`opid` = `RO`.`opid`)))) where ((`E`.`eventtype` not in ('compendium','pwa','opname')) and (concat(`E`.`eventtype`,'|',`E`.`action`) not in ('dashboard|selectroster','dashboard|reset','settings|view','roster|edit','settings|set','session|login','roster|view','roster|editop','roster|delop','dashboard|init','rosters|view','roster|killteamcomp','roster|delete','roster|gallery'))) order by `E`.`eventid` desc;

-- -----------------------------------------------------
-- View `killteam`.`RosterOperativeView`
-- -----------------------------------------------------
USE `killteam`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`vince`@`%` SQL SECURITY DEFINER VIEW `killteam`.`RosterOperativeView` AS select `RO`.`userid` AS `userid`,`RO`.`rosterid` AS `rosterid`,`RO`.`rosteropid` AS `rosteropid`,`RO`.`seq` AS `seq`,`RO`.`opname` AS `opname`,`RO`.`factionid` AS `factionid`,`RO`.`killteamid` AS `killteamid`,`RO`.`fireteamid` AS `fireteamid`,`RO`.`opid` AS `opid`,`RO`.`hascustomportrait` AS `hascustomportrait`,`RO`.`specialism` AS `specialism`,`RO`.`isinjured` AS `isinjured`,`RO`.`rested` AS `rested`,`O`.`M` AS `M`,`O`.`APL` AS `APL`,`O`.`GA` AS `GA`,`O`.`DF` AS `DF`,`O`.`SV` AS `SV`,`O`.`W` AS `W`,(case when (`R`.`keyword` <> '') then replace(`O`.`keywords`,`K`.`customkeyword`,concat('<',`R`.`keyword`,'>')) else `O`.`keywords` end) AS `keywords`,`O`.`specialisms` AS `specialisms`,`RO`.`curW` AS `curW`,`RO`.`activated` AS `activated`,`RO`.`oporder` AS `oporder`,`RO`.`hidden` AS `hidden`,`RO`.`wepids` AS `wepids`,`RO`.`eqids` AS `eqids`,`RO`.`notes` AS `notes`,`RO`.`xp` AS `xp`,`U`.`username` AS `username`,`R`.`rostername` AS `rostername`,`F`.`factionname` AS `factionname`,`K`.`killteamname` AS `killteamname`,`K`.`edition` AS `edition`,`FT`.`fireteamname` AS `fireteamname`,`FT`.`archetype` AS `archetype`,`O`.`opname` AS `optype` from ((((((`killteam`.`RosterOperative` `RO` join `killteam`.`User` `U` on((`U`.`userid` = `RO`.`userid`))) join `killteam`.`Roster` `R` on(((`R`.`userid` = `RO`.`userid`) and (`R`.`rosterid` = `RO`.`rosterid`)))) join `killteam`.`Faction` `F` on((`F`.`factionid` = `RO`.`factionid`))) join `killteam`.`Killteam` `K` on(((`K`.`factionid` = `RO`.`factionid`) and (`K`.`killteamid` = `RO`.`killteamid`)))) join `killteam`.`Fireteam` `FT` on(((`FT`.`factionid` = `RO`.`factionid`) and (`FT`.`killteamid` = `RO`.`killteamid`) and (`FT`.`fireteamid` = `RO`.`fireteamid`)))) join `killteam`.`Operative` `O` on(((`O`.`factionid` = `RO`.`factionid`) and (`O`.`killteamid` = `RO`.`killteamid`) and (`O`.`fireteamid` = `RO`.`fireteamid`) and (`O`.`opid` = `RO`.`opid`))));

-- -----------------------------------------------------
-- View `killteam`.`RosterView`
-- -----------------------------------------------------
USE `killteam`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`vince`@`%` SQL SECURITY DEFINER VIEW `killteam`.`RosterView` AS select `R`.`userid` AS `userid`,`U`.`username` AS `username`,`R`.`rosterid` AS `rosterid`,`R`.`seq` AS `seq`,`R`.`rostername` AS `rostername`,`R`.`notes` AS `notes`,`R`.`factionid` AS `factionid`,`R`.`killteamid` AS `killteamid`,`R`.`hascustomportrait` AS `hascustomportrait`,`R`.`keyword` AS `keyword`,`R`.`portraitcopyok` AS `portraitcopyok`,`R`.`TP` AS `TP`,`R`.`CP` AS `CP`,`R`.`VP` AS `VP`,`R`.`RP` AS `RP`,`R`.`ployids` AS `ployids`,`R`.`tacopids` AS `tacopids`,`R`.`spotlight` AS `spotlight`,`F`.`factionname` AS `factionname`,`K`.`killteamname` AS `killteamname`,`K`.`edition` AS `edition`,`K`.`customkeyword` AS `killteamcustomkeyword`,`K`.`description` AS `killteamdescription`,group_concat(distinct `O`.`opname` order by `RO`.`seq` ASC separator ', ') AS `oplist`,`R`.`viewcount` AS `viewcount`,`R`.`importcount` AS `importcount`,`R`.`reqpts` AS `reqpts`,`R`.`stratnotes` AS `stratnotes`,`R`.`eqnotes` AS `eqnotes`,`R`.`specopnotes` AS `specopnotes` from (((((`killteam`.`Roster` `R` join `killteam`.`User` `U` on((`U`.`userid` = `R`.`userid`))) join `killteam`.`Faction` `F` on((`F`.`factionid` = `R`.`factionid`))) join `killteam`.`Killteam` `K` on(((`K`.`factionid` = `R`.`factionid`) and (`K`.`killteamid` = `R`.`killteamid`)))) left join `killteam`.`RosterOperative` `RO` on(((`RO`.`userid` = `R`.`userid`) and (`RO`.`rosterid` = `R`.`rosterid`)))) left join `killteam`.`Operative` `O` on(((`O`.`factionid` = `RO`.`factionid`) and (`O`.`killteamid` = `RO`.`killteamid`) and (`O`.`fireteamid` = `RO`.`fireteamid`) and (`O`.`opid` = `RO`.`opid`)))) group by `R`.`userid`,`U`.`username`,`R`.`rosterid`,`R`.`seq`,`R`.`rostername`,`R`.`factionid`,`R`.`killteamid`,`R`.`hascustomportrait`,`R`.`TP`,`R`.`CP`,`R`.`VP`,`R`.`RP`,`R`.`ployids`,`R`.`tacopids`,`R`.`spotlight`,`F`.`factionname`,`K`.`killteamname`,`K`.`edition`,`K`.`description`;

-- -----------------------------------------------------
-- View `killteam`.`RosterView_Orig`
-- -----------------------------------------------------
USE `killteam`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`vince`@`%` SQL SECURITY DEFINER VIEW `killteam`.`RosterView_Orig` AS select `R`.`userid` AS `userid`,`U`.`username` AS `username`,`R`.`rosterid` AS `rosterid`,`R`.`seq` AS `seq`,`R`.`rostername` AS `rostername`,`R`.`notes` AS `notes`,`R`.`factionid` AS `factionid`,`R`.`killteamid` AS `killteamid`,`R`.`hascustomportrait` AS `hascustomportrait`,`R`.`TP` AS `TP`,`R`.`CP` AS `CP`,`R`.`VP` AS `VP`,`R`.`RP` AS `RP`,`R`.`ployids` AS `ployids`,`R`.`tacopids` AS `tacopids`,`R`.`spotlight` AS `spotlight`,`F`.`factionname` AS `factionname`,`K`.`killteamname` AS `killteamname`,`K`.`description` AS `killteamdescription`,group_concat(distinct (case `RO`.`opcount` when 1 then `RO`.`optype` else concat(`RO`.`opcount`,' ',`RO`.`optype`) end) order by `RO`.`firstseq` ASC separator ', ') AS `oplist`,`R`.`viewcount` AS `viewcount`,`R`.`importcount` AS `importcount` from ((((`killteam`.`Roster` `R` join `killteam`.`User` `U` on((`U`.`userid` = `R`.`userid`))) join `killteam`.`Faction` `F` on((`F`.`factionid` = `R`.`factionid`))) join `killteam`.`Killteam` `K` on(((`K`.`factionid` = `R`.`factionid`) and (`K`.`killteamid` = `R`.`killteamid`)))) left join (select `killteam`.`RosterOperative`.`userid` AS `userid`,`killteam`.`RosterOperative`.`rosterid` AS `rosterid`,`killteam`.`Operative`.`opname` AS `optype`,count(0) AS `opcount`,min(`killteam`.`RosterOperative`.`seq`) AS `firstseq` from (`killteam`.`RosterOperative` join `killteam`.`Operative` on(((`killteam`.`Operative`.`factionid` = `killteam`.`RosterOperative`.`factionid`) and (`killteam`.`Operative`.`killteamid` = `killteam`.`RosterOperative`.`killteamid`) and (`killteam`.`Operative`.`fireteamid` = `killteam`.`RosterOperative`.`fireteamid`) and (`killteam`.`Operative`.`opid` = `killteam`.`RosterOperative`.`opid`)))) group by `killteam`.`RosterOperative`.`userid`,`killteam`.`RosterOperative`.`rosterid`,`killteam`.`Operative`.`opname`) `RO` on(((`RO`.`userid` = `R`.`userid`) and (`R`.`rosterid` = `RO`.`rosterid`)))) group by `R`.`userid`,`U`.`username`,`R`.`rosterid`,`R`.`seq`,`R`.`rostername`,`R`.`factionid`,`R`.`killteamid`,`R`.`hascustomportrait`,`R`.`TP`,`R`.`CP`,`R`.`VP`,`R`.`RP`,`R`.`ployids`,`R`.`tacopids`,`R`.`spotlight`,`F`.`factionname`,`K`.`killteamname`,`K`.`description`;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
