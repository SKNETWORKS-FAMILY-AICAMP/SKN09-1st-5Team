import json
import mysql.connector

# MySQL 연결

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="ecardb",
)

# MySQL 커서 생성

cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS subsidy_data")

for year in range(2019, 2025):
    f = open(f"car_cnt/car_cnt_{year}.json")
    json_data = json.load(f)
    f.close()

    for data in json_data["데이터"]:
        sido = data["시도"]
        division = data["지역구분"]
        car_class = data["차종구분"]
        count = data["출고대수"]
        if count == "":
            count = 0

        cursor.execute("SELECT id FROM sido WHERE division = %s", (division,))

        try:
            sido_id = cursor.fetchone()[0]
        except:
            cursor.execute(
                "INSERT INTO sido (name, division) VALUES (%s, %s)",
                (sido, division),
            )
            conn.commit()
            sido_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO electric_car_registration (sido_id, year, class, regists) VALUES (%s, %s, %s, %s)",
            (sido_id, year, car_class, count),
        )

        conn.commit()

        f = open(f"data_city/subsidy_data_{year}.json")
    json_data = json.load(f)
    # print(json_data)
    f.close()

    for data in json_data["데이터"]:
        sido = data["시도"]
        division = data["지역구분"]
        subsidy = data["보조금/승용(만원)"].replace(",", "")
        # subsidy2 = data["보조금/초소형(만원)"].replace(",", "")
        # subsidy3 = data.get("조금/화물(만원)", None)
        # subsidy4 = data.get("보조금/승합(만원)", None)

        if subsidy == "":
            subsidy = 0
        # if subsidy2 == "":
        #     subsidy2 = 0

        cursor.execute("SELECT id FROM sido WHERE division = %s", (division,))

        try:
            sido_id = cursor.fetchone()[0]
        except:
            cursor.execute(
                "INSERT INTO sido (name, division) VALUES (%s, %s)",
                (sido, division),
            )
            conn.commit()
            sido_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO electric_car_subsidy (sido_id, year, subsidy) VALUES (%s, %s, %s)",
            (sido_id, year, subsidy),
        )

        conn.commit()
cursor.close()

# CREATE TABLE
#     `sido` (
#         `id` int NOT NULL AUTO_INCREMENT,
#         `name` varchar(20) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '시도명',
#             `division` varchar(20) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '시도구분',
#             `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
#             `deleted_at` datetime DEFAULT NULL,
#             PRIMARY KEY (`id`)
#     ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# CREATE TABLE
#     `electric_car_registration` (
#         `id` int NOT NULL AUTO_INCREMENT,
#         `sido_id` int DEFAULT NULL COMMENT '시도코드',
#         `year` char(4) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '연도',
#             `class` varchar(20) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '차종구분',
#             `regists` int NOT NULL DEFAULT '0' COMMENT '출고대수',
#             `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
#             `updated_at` datetime DEFAULT NULL,
#             `deleted_at` datetime DEFAULT NULL,
#             PRIMARY KEY (`id`),
#             KEY `sido_id` (`sido_id`),
#             CONSTRAINT `electric_car_registration_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`) ON UPDATE CASCADE
#     ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# CREATE TABLE
#     `electric_car_subsidy` (
#         `id` int NOT NULL AUTO_INCREMENT,
#         `sido_id` int NOT NULL COMMENT '시도코드',
#         `year` char(4) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '연도',
#             `subsidy` int NOT NULL COMMENT '보조금/승용(만원)',
#             `subsidy2` int NOT NULL COMMENT '보조금/초소형(만원)',
#             `subsidy3` varchar(50) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '보조금/화물(만원)',
#             `subsidy4` varchar(50) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '보조금/승합(만원)',
#             `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
#             `updated_at` datetime DEFAULT NULL,
#             `deleted_at` datetime DEFAULT NULL,
#             PRIMARY KEY (`id`),
#             KEY `sido_id` (`sido_id`),
#             CONSTRAINT `electric_car_subsidy_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
#     ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# CREATE TABLE
#     `electric_car_subsidy_detail` (
#         `id` int NOT NULL AUTO_INCREMENT,
#         `sido_id` int DEFAULT NULL COMMENT '시도코드',
#         `year` char(4) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '연도',
#             `class` varchar(20) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '차종',
#             `company` varchar(20) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '제조사',
#             `model` varchar(50) CHARACTER
#         SET
#             utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '모델명',
#             `national_subsidy` int DEFAULT NULL COMMENT '국비(만원)',
#             `sido_subsidy` int DEFAULT NULL COMMENT '지방비(만원)',
#             `total_subsidy` int DEFAULT NULL COMMENT '보조금(만원)',
#             `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
#             `updated_at` datetime DEFAULT NULL,
#             `deleted_at` datetime DEFAULT NULL,
#             PRIMARY KEY (`id`),
#             KEY `sido_id` (`sido_id`),
#             CONSTRAINT `electric_car_subsidy_detail_ibfk_1` FOREIGN KEY (`sido_id`) REFERENCES `sido` (`id`)
#     ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
