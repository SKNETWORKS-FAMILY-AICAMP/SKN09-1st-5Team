import mysql.connector
import streamlit as st
import pandas as pd

# MySQL 데이터베이스 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="135213",  
    database="ecardb"
)

# 연결이 제대로 되었는지 확인
if conn.is_connected():
    st.write("MySQL 연결 성공!")
else:
    st.write("MySQL 연결 실패!")

cursor = conn.cursor(dictionary=True)

# 수정된 SQL 쿼리 작성 (electric_car_registration 테이블과 electric_car_subsidy 테이블을 JOIN)
query = """
    SELECT e.id, s.name AS sido_name, s.division AS sido_division, e.year, e.subsidy, r.class, r.regists
    FROM electric_car_subsidy e
    JOIN sido s ON e.sido_id = s.id
    LEFT JOIN electric_car_registration r ON e.sido_id = r.sido_id AND e.year = r.year
    WHERE e.year = '2019';
"""

# 쿼리 실행
cursor.execute(query)

# 결과 가져오기
data = cursor.fetchall()

# 쿼리 실행 결과가 있는지 확인
if len(data) == 0:
    st.write("2019년 전기차 보조금 데이터가 없습니다.")
else:
    # 데이터프레임으로 변환
    df = pd.DataFrame(data)
    
    # 'id' 컬럼 삭제
    df = df.drop(columns=['id'])
    
    # 인덱스 1부터 시작하도록 수정
    df.reset_index(drop=True, inplace=True)
    df.index += 1

# 커서 종료
cursor.close()
conn.close()

# 세션 상태로 버튼 클릭 여부를 관리
if 'show_table' not in st.session_state:
    st.session_state.show_table = False

# 버튼 클릭시, 테이블 표시 여부를 변경
if st.button('2019년 전기차 보조금 데이터 보기'):
    st.session_state.show_table = True

# 드롭다운을 사용하여 시도 선택
if st.session_state.show_table:
    # 시도 이름을 리스트로 가져오기
    unique_sido_names = df['sido_name'].unique()
    
    # 시도 선택 드롭다운
    selected_sido = st.selectbox('시도 선택', unique_sido_names)

    # 선택된 시도에 해당하는 데이터만 필터링
    filtered_df = df[df['sido_name'] == selected_sido]
    
    # 필터링된 데이터 출력
    st.title(f'{selected_sido} - 2019년 전기차 보조금 및 출고대수 데이터')
    st.dataframe(filtered_df)
