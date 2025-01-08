DROP TABLE IF EXISTS `sido`;


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


--
DROP TABLE IF EXISTS `car_subsidy_2019`;


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

--
DROP TABLE IF EXISTS `car_subsidy_2020`;

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


--
DROP TABLE IF EXISTS `car_subsidy_2021`;


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


--
DROP TABLE IF EXISTS `car_subsidy_2022`;


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


--
DROP TABLE IF EXISTS `car_subsidy_2023`;


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


--
DROP TABLE IF EXISTS `car_subsidy_2024`;


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


--
DROP TABLE IF EXISTS `electric_car_registration`;


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

--
DROP TABLE IF EXISTS `electric_car_subsidy`;



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

