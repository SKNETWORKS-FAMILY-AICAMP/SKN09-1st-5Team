import streamlit as st
import pandas as pd
import json

# JSON 파일에서 데이터 불러오기
with open('faq_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# 페이지 설정
st.set_page_config(page_title="FAQ", layout="wide")

# 제목
st.title("FAQ - 전기차 관련 안내")

# 질문 목록 표시 (페이지 내에서 선택)
st.subheader("질문 목록")

# 버튼 상태를 저장하는 session_state 초기화 (세션 상태에 버튼 클릭 여부 저장)
if 'clicked' not in st.session_state:
    st.session_state.clicked = {}

# 각 질문 버튼에 대해 상태를 추적하고, 클릭 시 상태를 변경
for idx, row in df.iterrows():
    question_title = row['제목']
    
    # 버튼 만들기
    if st.button(f"💡 {question_title}", key=idx):
        # 클릭 상태를 반전시켜서 다시 클릭 시 답변이 사라지도록 설정
        st.session_state.clicked[question_title] = not st.session_state.clicked.get(question_title, False)

    # 클릭된 질문에 대한 답변 표시
    if st.session_state.clicked.get(question_title, False):
        st.subheader(question_title)
        st.markdown(row['답변'])

# 출처 추가
st.markdown("출처: [무공해차 통합 누리집](https://ev.or.kr/nportal/partcptn/initFaqAction.do)")
