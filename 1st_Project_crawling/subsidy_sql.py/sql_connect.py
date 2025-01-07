import mysql.connector
import json

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'car_subsidy'
)

# if connection.is_connected():
#     print("연결 성공")

cursor = connection.cursor()
# cursor = db.cursor()

with open('subsidy_data_2021.json', 'r', encoding= 'utf-8') as file:
    data = json.load(file)


year = data["연도"]
for entry in data["데이터"]:
    sido_name = entry["시도"]
    division = entry["지역구분"]

    for entry2 in entry["차종별 보조금"]:
        car_class = entry2['차종']
        model = entry2['모델명']
        total_subsidy = entry2["보조금(만원)"].replace(",", "")

        insert_query = """
        INSERT INTO car_subsidy_2021 (year, sido_name, division, car_class, model, total_subsidy)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (year, sido_name, division, car_class, model, total_subsidy))

connection.commit()


cursor.close()
connection.close()
