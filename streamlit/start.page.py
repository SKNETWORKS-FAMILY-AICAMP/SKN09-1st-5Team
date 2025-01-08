import streamlit as st

st.set_page_config(page_title="어두운 테마 예시", page_icon="🌙", layout="centered", initial_sidebar_state="auto")
# 연도별 / 지역별 / 기업 FAQ

st.subheader("지역별 전기 자동차 보조금에 따른 등록 수 변화 추이")

st.markdown("<br>", unsafe_allow_html= True)

st.image("https://cdn.naeponews.co.kr/news/photo/202407/31376_37437_391.jpg",width= 1000)

st.markdown("<br><br>", unsafe_allow_html=True)

num_button = 3
col1, col2, col3 = st.columns(num_button)

with col1:
    if st.button("차트1"):
        st.write("차트1")

with col2:
    if st.button("차트 2"):
        st.write("차트 2")

with col3:
    if st.button("차트 3"):
        st.write("차트3")


# cd streamlit
# streamlit run start.



# pick motion
    