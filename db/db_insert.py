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

# cursor = conn.cursor()
cursor = conn.cursor(buffered=True)

# 데이터베이스 초기화
cursor.execute("SET FOREIGN_KEY_CHECKS = 0; ")
cursor.execute("TRUNCATE TABLE electric_car_registration")
cursor.execute("TRUNCATE TABLE electric_car_subsidy")
cursor.execute("TRUNCATE TABLE electric_car_subsidy_detail")
cursor.execute("TRUNCATE TABLE sido")
cursor.execute("TRUNCATE TABLE car_subsidy_2019")
cursor.execute("TRUNCATE TABLE car_subsidy_2020")
cursor.execute("TRUNCATE TABLE car_subsidy_2021")
cursor.execute("TRUNCATE TABLE car_subsidy_2022")
cursor.execute("TRUNCATE TABLE car_subsidy_2023")
cursor.execute("TRUNCATE TABLE car_subsidy_2024")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1; ")

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
    f.close()

    for data in json_data["데이터"]:
        sido = data["시도"]
        division = data["지역구분"]
        subsidy = data["보조금/승용(만원)"].replace(",", "")

        if subsidy == "":
            subsidy = 0

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
        # 차종별 보조금이 있는지 체크
        if data.get("차종별 보조금"):
            for entry in data["차종별 보조금"]:
                car_class = entry['차종']
                model = entry['모델명']
                total_subsidy = entry["보조금(만원)"].replace(",", "")

                insert_query = f"""
                    INSERT INTO car_subsidy_{year} (year, sido_name, division, car_class, model, total_subsidy)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (year, sido, division, car_class, model, total_subsidy))

        conn.commit()
cursor.close()