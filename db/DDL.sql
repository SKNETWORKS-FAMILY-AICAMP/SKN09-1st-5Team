-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: 127.0.0.1    Database: ecardb
-- ------------------------------------------------------
-- Server version	9.1.0
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

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sido`
--
-- DROP TABLE IF EXISTS `sido`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `sido` (
        `id` int NOT NULL AUTO_INCREMENT,
        `name` varchar(20) CHARACTER
        SET
            utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '시도명',
            `division` varchar(20) CHARACTER
        SET
            utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '시도구분',
            PRIMARY KEY (`id`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 163 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_subsidy_2019`
--
DROP TABLE IF EXISTS `car_subsidy_2019`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `car_subsidy_2019` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int DEFAULT NULL COMMENT '시도코드',
        `year` char(4) DEFAULT NULL COMMENT '연도',
        `car_class` varchar(30) DEFAULT NULL COMMENT '차종',
        `model` varchar(70) DEFAULT NULL COMMENT '모델명',
        `total_subsidy` int DEFAULT NULL COMMENT '보조금(만원)',
        PRIMARY KEY (`id`),
        KEY `sido_id` (`sido_id`),
        CONSTRAINT `car_subsidy_2019_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_subsidy_2020`
--
DROP TABLE IF EXISTS `car_subsidy_2020`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `car_subsidy_2020` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int DEFAULT NULL COMMENT '시도코드',
        `year` char(4) DEFAULT NULL COMMENT '연도',
        `car_class` varchar(30) DEFAULT NULL COMMENT '차종',
        `model` varchar(70) DEFAULT NULL COMMENT '모델명',
        `total_subsidy` int DEFAULT NULL COMMENT '보조금(만원)',
        PRIMARY KEY (`id`),
        KEY `sido_id` (`sido_id`),
        CONSTRAINT `car_subsidy_2020_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_subsidy_2021`
--
DROP TABLE IF EXISTS `car_subsidy_2021`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `car_subsidy_2021` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int DEFAULT NULL COMMENT '시도코드',
        `year` char(4) DEFAULT NULL COMMENT '연도',
        `car_class` varchar(30) DEFAULT NULL COMMENT '차종',
        `model` varchar(70) DEFAULT NULL COMMENT '모델명',
        `total_subsidy` int DEFAULT NULL COMMENT '보조금(만원)',
        PRIMARY KEY (`id`),
        KEY `sido_id` (`sido_id`),
        CONSTRAINT `car_subsidy_2021_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_subsidy_2022`
--
DROP TABLE IF EXISTS `car_subsidy_2022`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `car_subsidy_2022` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int DEFAULT NULL COMMENT '시도코드',
        `year` char(4) DEFAULT NULL COMMENT '연도',
        `car_class` varchar(30) DEFAULT NULL COMMENT '차종',
        `model` varchar(70) DEFAULT NULL COMMENT '모델명',
        `total_subsidy` int DEFAULT NULL COMMENT '보조금(만원)',
        PRIMARY KEY (`id`),
        KEY `sido_id` (`sido_id`),
        CONSTRAINT `car_subsidy_2022_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_subsidy_2023`
--
DROP TABLE IF EXISTS `car_subsidy_2023`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `car_subsidy_2023` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int DEFAULT NULL COMMENT '시도코드',
        `year` char(4) DEFAULT NULL COMMENT '연도',
        `car_class` varchar(30) DEFAULT NULL COMMENT '차종',
        `model` varchar(70) DEFAULT NULL COMMENT '모델명',
        `total_subsidy` int DEFAULT NULL COMMENT '보조금(만원)',
        PRIMARY KEY (`id`),
        KEY `sido_id` (`sido_id`),
        CONSTRAINT `car_subsidy_2023_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_subsidy_2024`
--
DROP TABLE IF EXISTS `car_subsidy_2024`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `car_subsidy_2024` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int DEFAULT NULL COMMENT '시도코드',
        `year` char(4) DEFAULT NULL COMMENT '연도',
        `car_class` varchar(30) DEFAULT NULL COMMENT '차종',
        `model` varchar(70) DEFAULT NULL COMMENT '모델명',
        `total_subsidy` int DEFAULT NULL COMMENT '보조금(만원)',
        PRIMARY KEY (`id`),
        KEY `sido_id` (`sido_id`),
        CONSTRAINT `car_subsidy_2024_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `electric_car_registration`
--
DROP TABLE IF EXISTS `electric_car_registration`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `electric_car_registration` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int DEFAULT NULL COMMENT '시도코드',
        `year` char(4) CHARACTER
        SET
            utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '연도',
            `class` varchar(20) CHARACTER
        SET
            utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '차종구분',
            `regists` int NOT NULL DEFAULT '0' COMMENT '출고대수',
            PRIMARY KEY (`id`),
            KEY `sido_id` (`sido_id`),
            CONSTRAINT `electric_car_registration_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`) ON UPDATE CASCADE
    ) ENGINE = InnoDB AUTO_INCREMENT = 960 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `electric_car_subsidy`
--
DROP TABLE IF EXISTS `electric_car_subsidy`;

/*!40101 SET @saved_cs_client     = @@character_set_client */;

/*!50503 SET character_set_client = utf8mb4 */;

CREATE TABLE
    `electric_car_subsidy` (
        `id` int NOT NULL AUTO_INCREMENT,
        `sido_id` int NOT NULL COMMENT '시도코드',
        `year` char(4) CHARACTER
        SET
            utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '연도',
            `subsidy` int NOT NULL COMMENT '보조금/승용(만원)',
            PRIMARY KEY (`id`),
            KEY `sido_id` (`sido_id`),
            CONSTRAINT `electric_car_subsidy_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 970 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

--
-- Dumping routines for database 'ecardb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;

/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-08 10:44:22