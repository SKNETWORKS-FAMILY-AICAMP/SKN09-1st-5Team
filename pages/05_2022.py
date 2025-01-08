import mysql.connector
import streamlit as st
import pandas as pd
import plotly.express as px

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="135213",  
    database="ecardb"
)

if conn.is_connected():
    st.write("MySQL 연결 성공!")
else:
    st.write("MySQL 연결 실패!")

cursor = conn.cursor(dictionary=True)

query = """
    SELECT e.id, s.name AS sido_name, s.division AS sido_division, e.year, e.subsidy, r.class, r.regists
    FROM electric_car_subsidy e
    JOIN sido s ON e.sido_id = s.id
    LEFT JOIN electric_car_registration r ON e.sido_id = r.sido_id AND e.year = r.year
    WHERE e.year = '2022';
"""

cursor.execute(query)

data = cursor.fetchall()

if len(data) == 0:
    st.write("2022년 전기차 보조금 데이터가 없습니다.")
else:
    df = pd.DataFrame(data)
    
    df = df.drop(columns=['id'])
    
    df.reset_index(drop=True, inplace=True)
    df.index += 1

cursor.close()
conn.close()

if 'show_table' not in st.session_state:
    st.session_state.show_table = False

if st.button('2022년 전기차 보조금 데이터 보기'):
    st.session_state.show_table = not st.session_state.show_table

if st.session_state.show_table:
    unique_sido_names = df['sido_name'].unique()
    
    selected_sido = st.selectbox('시도 선택', unique_sido_names)

    filtered_df = df[df['sido_name'] == selected_sido]
    
    st.title(f'{selected_sido} - 2022년 전기차 보조금 및 출고대수 데이터')
    st.dataframe(filtered_df)
    
    fig1 = px.scatter(filtered_df, 
                      x='sido_division', 
                      y=['subsidy', 'regists'],
                      labels={'sido_division': 'Sido Division', 'value': 'Value'},
                      title=f'{selected_sido} - Subsidy and Registrations per Sido Division',
                      template="plotly_white")
    fig1.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector='scatter')
    st.plotly_chart(fig1)

    fig2 = px.scatter(df, 
                      x='sido_division', 
                      y=['subsidy', 'regists'],
                      labels={'sido_division': 'Sido Division', 'value': 'Value'},
                      title='Overall - Subsidy and Registrations per Sido Division',
                      template="plotly_white")
    fig2.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector='scatter')
    st.plotly_chart(fig2)
