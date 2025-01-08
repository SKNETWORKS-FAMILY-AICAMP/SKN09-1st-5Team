
import streamlit as st

st.image("https://cdn.naeponews.co.kr/news/photo/202407/31376_37437_391.jpg",width= 900)
def start_page():
    st.header("지역별 보조금과 전기차 등록수 조회 웹 ")
    st.markdown('<h style="font-size: 20px;"> 이 페이지는 전기차 등록대수와 지역별 보조금에 대한 자료의 부재로 이를 통합하여 분석할 수 있는 서비스를 제공하도록 설계되었습니다.'
                ,unsafe_allow_html=True)
start_page()

st.markdown("<br>", unsafe_allow_html= True)

st.markdown('<h2 style="font-size: 30px;">우리 페이지에서 제공하는 정보</h2>', unsafe_allow_html=True)
st.write('<h style="font-size: 20px;">  연도별/지역별 전기차 등록 대수',unsafe_allow_html=True)
st.write('<h style="font-size: 20px;"> 연도별/지역별 전기차 보조금',unsafe_allow_html=True)

st.markdown('<h2 style="font-size: 30px;">출처</h2>', unsafe_allow_html=True)
st.markdown('<h style="font-size: 20px;">무공해차 통합누리집', unsafe_allow_html=True)
st.markdown('<h style="font-size: 20px;">차지인포', unsafe_allow_html=True)