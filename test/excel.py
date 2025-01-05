# pip install pandas openpyxl xlrd
# pip install mysql-connector-python
import pandas as pd
import os
import csv
import mysql.connector

# get the data from the excel file
filepath = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(f"{filepath}/resource/data.xls", sheet_name="Sheet1")

# ignore the first second row

df = df[3:]
# naming columns
df.columns = [
    "년월",
    "서울",
    "부산",
    "대구",
    "인천",
    "광주",
    "대전",
    "울산",
    "세종",
    "경기",
    "강원",
    "충북",
    "충남",
    "전북",
    "전남",
    "경북",
    "경남",
    "제주",
    "합계",
]

# 년월	서울	부산	대구	인천	광주	대전	울산	세종	경기	강원	충북	충남	전북	전남	경북	경남	제주	합계
# 2024-07	79548	40368	32631	48073	13820	19933	8883	4905	134741	19611	22759	27979	22494	28386	30810	43013	43117	621071
df.to_csv(f"{filepath}/resource/data.csv", index=False, encoding="utf-8-sig")

# save to mysql
# connect to mysql
conn = mysql.connector.connect(
    host="localhost", user="root", password="mysql", database="ecardb", port="3306"
)

cursor = conn.cursor()

# 전기차 등록 현황
# DROP TABLE IF EXISTS ecar;
# CREATE TABLE IF NOT EXISTS ecar (
#         `id` INT AUTO_INCREMENT PRIMARY KEY,
#         `년월` DATE,
#         `서울` INT,
#         `부산` INT,
#         `대구` INT,
#         `인천` INT,
#         `광주` INT,
#         `대전` INT,
#         `울산` INT,
#         `세종` INT,
#         `경기` INT,
#         `강원` INT,
#         `충북` INT,
#         `충남` INT,
#         `전북` INT,
#         `전남` INT,
#         `경북` INT,
#         `경남` INT,
#         `제주` INT,
#         `합계` INT
#     )
# '''
# insert into the table

with open(f"{filepath}/resource/data.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader)
    values = []
    for row in reader:
        row[0] += "-01"
        values.append(row)
    print(values[0])
    cursor.executemany(
        "INSERT INTO ecar VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        values[::-1],
    )

    conn.commit()
    cursor.close()
    conn.close()
