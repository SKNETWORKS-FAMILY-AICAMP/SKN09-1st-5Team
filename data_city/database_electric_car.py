# database_electric_car.py

import json
import mysql.connector

# MySQL 연결

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ecardb",
)

# MySQL 커서 생성

cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS subsidy_data")

for year in range(2019, 2025):
    with open(f"data_city/subsidy_data_{year}.json") as f:
        json_data = json.load(f)

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

        conn.commit()
cursor.close()