# pip install streamlit
# pip install mysql-connector-python
import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="mysql", database="ecardb", port="3306"
)
cursor = conn.cursor()

cursor.execute(
    "SELECT SUBSTRING(년월, 1, 7), 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주 FROM ecar"
)

rows = cursor.fetchall()

# for row in rows:
#     st.write(row)
df = pd.DataFrame(rows)
df.columns = [
    "date",
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
]

st.title("전기차 등록 현황")
st.dataframe(df, use_container_width=True, hide_index=True)
# 년월을 기준으로 지역별 전기차 등록 현황을 line 그래프로 표현
st.line_chart(df.set_index("date"), use_container_width=True)
# 년월 기간을 선택하면 해당 기간의 지역별 전기차 등록 현황을 그래프로 표현
# st.input("년월 기간을 입력하세요", type="date")

date = st.selectbox("년월을 선택하세요", df["date"][::-1].unique())

# 각지역별을 을 x 축으로, value 를 y 축으로
# st.bar_chart(df[df["date"] == date].set_index("date"), use_container_width=True)

# 그래프의 x축에 각 지역이 표시되어야해
st.write(df[df["date"] == date].set_index("date"))
# bar 그래프의 x축에 지역명이 표시되도록 수정
st.bar_chart(df[df["date"] == date].set_index("date").T, use_container_width=True)

# 지역을 선택하세요
col1, col2, col3 = st.columns(3)

with col1:
    area = st.selectbox("지역을 선택하세요", df.columns[1:])
with col2:
    start = st.selectbox("시작일을 선택하세요", df["date"][::-1].unique())
with col3:
    end = st.selectbox("종료일을 선택하세요", df["date"][::-1].unique())

# str to time
start = pd.to_datetime(start)
end = pd.to_datetime(end)

st.bar_chart(
    df[
        (pd.to_datetime(df["date"]) >= start) & (pd.to_datetime(df["date"]) <= end)
    ].set_index("date")[area],
    use_container_width=True,
)