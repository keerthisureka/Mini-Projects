-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: mlis
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `ApptID` int NOT NULL,
  `UserID` varchar(5) DEFAULT NULL,
  `LabID` varchar(5) DEFAULT NULL,
  `TestID` varchar(5) DEFAULT NULL,
  `ApptDate` date DEFAULT NULL,
  PRIMARY KEY (`ApptID`),
  KEY `UserID` (`UserID`),
  KEY `LabID` (`LabID`),
  KEY `TestID` (`TestID`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE,
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`LabID`) REFERENCES `lab` (`LabID`) ON DELETE CASCADE,
  CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`TestID`) REFERENCES `test` (`TestID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (4001,'3001','1001','2001','2024-04-10'),(4002,'3001','1002','2001','2024-02-26'),(4003,'3002','1005','2004','2024-03-10'),(4004,'3003','1004','2003','2024-03-15'),(4005,'3001','1003','2002','2024-04-27');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `details_view`
--

DROP TABLE IF EXISTS `details_view`;
/*!50001 DROP VIEW IF EXISTS `details_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `details_view` AS SELECT 
 1 AS `TestName`,
 1 AS `LabName`,
 1 AS `ContactNo`,
 1 AS `Location`,
 1 AS `Price`,
 1 AS `OpenHrs`,
 1 AS `YrsOfExp`,
 1 AS `Description`,
 1 AS `SampleType`,
 1 AS `TestDuration`,
 1 AS `TestsPerday`,
 1 AS `Sensitivity`,
 1 AS `Specificity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `efficiency`
--

DROP TABLE IF EXISTS `efficiency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `efficiency` (
  `LabID` varchar(5) NOT NULL,
  `TestID` varchar(5) NOT NULL,
  `Price` float DEFAULT NULL,
  `TestsPerDay` int DEFAULT NULL,
  `Sensitivity` varchar(20) DEFAULT NULL,
  `Specificity` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`LabID`,`TestID`),
  KEY `FK_TestID` (`TestID`),
  CONSTRAINT `FK_LabID` FOREIGN KEY (`LabID`) REFERENCES `lab` (`LabID`) ON DELETE CASCADE,
  CONSTRAINT `FK_TestID` FOREIGN KEY (`TestID`) REFERENCES `test` (`TestID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `efficiency`
--

LOCK TABLES `efficiency` WRITE;
/*!40000 ALTER TABLE `efficiency` DISABLE KEYS */;
INSERT INTO `efficiency` VALUES ('1001','2001',1700,10,'67-100%','25-80%'),('1002','2002',800,30,'80-90%','60-70%'),('1002','2004',960,23,'48-56%','67-85%'),('1003','2003',480,45,'55-60%','77-85%'),('1004','2002',800,50,'79-85%','66-80%'),('1006','2005',1600,25,'75-80%','50-60%');
/*!40000 ALTER TABLE `efficiency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab`
--

DROP TABLE IF EXISTS `lab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab` (
  `LabID` varchar(5) NOT NULL,
  `LabName` varchar(50) DEFAULT NULL,
  `ContactNo` bigint DEFAULT NULL,
  `Location` varchar(100) DEFAULT NULL,
  `OpenHrs` int DEFAULT NULL,
  `YrsOfExp` int DEFAULT NULL,
  PRIMARY KEY (`LabID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab`
--

LOCK TABLES `lab` WRITE;
/*!40000 ALTER TABLE `lab` DISABLE KEYS */;
INSERT INTO `lab` VALUES ('1001','Aarthi Scans and Labs',9980209664,'Indiranagar',24,23),('1002','Apollo Diagnostics',7498989533,'Ulsoor',12,5),('1003','Ragavs Diagnostic and Research Centre',8876989800,'Koramangala',24,8),('1004','Gokul Diagnostics',8876509090,'Whitefield',24,10),('1005','GM Healthcare Pvt Ltd',9876543210,'AECS Layout',24,15),('1006','Metropolis Healthcare Pvt Ltd',5675674343,'Brookefield',12,12),('1007','Dr Lal Pathlabs',7767788900,'Kundalahalli',12,8),('1008','Sri Vinayaka Laboratory',9998887777,'Shivajinagar',24,20),('1009','Acculab',8876887690,'MG Road',24,7),('1010','XYZ',9987998709,'MG Road',12,10);
/*!40000 ALTER TABLE `lab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `TestID` varchar(5) NOT NULL,
  `TestName` varchar(50) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  `SampleType` varchar(50) DEFAULT NULL,
  `TestDuration` varchar(20) DEFAULT NULL,
  `NormalRange` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`TestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES ('2001','CT Scan','Diagnostic imaging of the inside of the body','NA','15 mins','NA'),('2002','Blood Test','Complete blood count','Blood','1 hour','12-15 g/dL'),('2003','Urine Test','Urinalysis','Urine','30 minutes','Clear yellow'),('2004','X-Ray','Radiographic imaging','NA','15 minutes','NA'),('2005','Cholesterol Test','Lipid panel','Blood','45 minutes','Below 200 mg/dL'),('2006','COVID-19 Test','PCR Test for COVID-19','Swab from Nose and throat','2 hours','Negative');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserID` varchar(5) NOT NULL,
  `UserName` varchar(40) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `UserType` varchar(20) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('3001','Anil','anil@gmail.com','anil','Patient',20,'M'),('3002','Akash','akash@gmail.com','akash','Patient',30,'M'),('3003','Riya','riya@gmail.com','riya','Patient',22,'F'),('3004','Sharon','sharon@gmail.com','sharon','Admin',38,'M'),('3005','Rahul','rahul@gmail.com','rahul','Patient',28,'M'),('3006','Anjali','anjali@gmail.com','anjali','Admin',29,'F');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `details_view`
--

/*!50001 DROP VIEW IF EXISTS `details_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `details_view` AS select `t`.`TestName` AS `TestName`,`l`.`LabName` AS `LabName`,`l`.`ContactNo` AS `ContactNo`,`l`.`Location` AS `Location`,`e`.`Price` AS `Price`,`l`.`OpenHrs` AS `OpenHrs`,`l`.`YrsOfExp` AS `YrsOfExp`,`t`.`Description` AS `Description`,`t`.`SampleType` AS `SampleType`,`t`.`TestDuration` AS `TestDuration`,`e`.`TestsPerDay` AS `TestsPerday`,`e`.`Sensitivity` AS `Sensitivity`,`e`.`Specificity` AS `Specificity` from ((`lab` `l` join `test` `t`) join `efficiency` `e`) where ((`t`.`TestID` = `e`.`TestID`) and (`t`.`TestID` = `e`.`TestID`) and (`t`.`TestName` = 'Blood Test')) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-26 19:07:35
