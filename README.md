
# SKN09-1st-5Team

> **SK Networks AI CAMP 9기** <br/> **개발기간: 2025.01.07 ~ 2025.01.08** <br/> **팀명: 무공해즈** 
  
<div align="center">
  <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/sk_encore.png" width="1000" alt="image"/>
  <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/minions_main.jpg" width="1000" alt="image"/>
</div>

<br>
</br>  

# Introduction Team (팀 소개)
### ✅ 팀명 : 무공해즈👨‍💻👩‍💻👩‍💻👨‍💻
<table align=center>
  <tbody>
    <tr>
    <br>
      <td align=center><b>이광운</b></td>
      <td align=center><b>이윤재</b></td>
      <td align=center><b>임수연</b></td>
      <td align=center><b>허정윤</b></td>
    </tr>
    <tr>
      <td align="center">
        <div>
          <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/minion_kw.jpg" width="200px;" alt="이광운"/>
        </div>
      </td>
      <td align="center">
        <div>
          <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/minion_yj.jpg" width="200px;" alt="이윤재"/>
        </div>
      </td>
      <td align="center">
        <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/minion_sy.jpg" width="200px;" alt="임수연"/>
      </td>
      <td align="center">
        <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/minion_jy.jpg" width="200px;" alt="허정윤"/>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/Leegwangwoon"><div align=center>@Woony</div></a></td>
      <td><a href="https://github.com/dadambi116"><div align=center>@dadambi116</div></a></td>
      <td><a href="https://github.com/ohback"><div align=center>@ohback</div></a></td>
      <td><a href="https://github.com/devunis"><div align=center>@jy</div></a></td>
    </tr>
  </tbody>
</table>


<br>
</br>
  
# Introduction Project (프로젝트 개요)

### ✅프로젝트 명
지역별 보조금과 전기차 등록수 조회 웹 페이지

### ✅프로젝트 소개
[환경부https://ev.or.kr/nportal/main.do](https://ev.or.kr/nportal/main.do)의 전기차 등록대수, 지역별 보조금, 차종별 보조금 정보를 크롤링하여 데이터를 수집, DB에 저장한 뒤, 수집한 데이터를 시각화 및 분석하여 사용자에게 지역별 보조금에 따른 전기차 등록수를 보여주고 전기차 누리집 사이트에서 제공하는 FAQ중 전기차 키워드가 들어간 질문만 크롤링하여 제공하도록 설계되었습니다.<br>
### ✅프로젝트 필요성(배경) 
💡전기차 등록대수와 지역별 보조금에 대한 통합 자료의 부재\
매년 전기차 등록대수가 증가하고 있는 현재 추세가 지역별 보조금과 유의미한 관계가 있는지에 대하여 파악해 볼 필요성을 느꼈고 이를 통해 도출된 자료가 관련 부서와 기업에 참고가 될 수 있을 것이라 생각하였습니다.

### ✅프로젝트 목표
💡분석 및 정책/계획 수립 지원\
지자체 관계자 및 전기차 생산 기업에게 지역별 전기차 보조금과 전기차 등록대수에 대한 통합 자료를 제공함으로써 지역별 보조금 정책의 재점검 또는 정책 수립에 도움을 주며 나아가 보조금 편성에 따른 전기차 판매량을 예상하고 생산/판매 업체에게 시장 공략 등의 계획 수립을 지원 할 수 있습니다.
 

<br>
</br>

# 시작 가이드
## 설치/사용 방법

###  GitHub에서 리포지토리 클론

```bash
git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team.git
```

###  라이브러리 설치

```bssh
cd SKN09-1st-5Team
pip install -r requirements.txt
```

###  정보수집(크롤링코드 실행)
```bssh
python 파일이름.py
``` 
###  서비스 페이지 실행
```bssh
streamlit run app.py
``` 
<br>
</br>

# Tech Stack (기술 스택)

>### <span style="color:white"> 개발환경 및 도구 </span>
<table>
  <tr>
    <td><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/VScode-007ACC?style=for-the-badge&logo=Vscode&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"/></td>
  </tr>  
</table>

>### <span style="color:white"> UI </span>
<table>
  <tr>
    <td><img src="https://img.shields.io/badge/-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/></td>
  </tr>
</table>

>### <span style="color:white"> 데이터 수집 및 처리 </span>
<table>
  <tr>
    <td><img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=Plotly&logoColor=white"/></td>
  </tr>
</table>


<br>
</br>


# 요구사항 명세서
<div align="center">
  <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD%20%EB%AA%85%EC%84%B8%EC%84%9C.png" width="1000" alt="요구사항 명세서"/>
</div>

<br>
</br>

# ERD
<div align="center">
  <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/erd_fin.png" width="1000" alt="ERD"/>
</div>

<br>
</br>

# 수행결과(시연 페이지)
<div align="center">
  <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/main_page.png" width="1000" alt="1"/>
  <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-1st-5Team/blob/main/img_readme/second_page.png" width="1000" alt="2"/>
</div>

<br>
</br>

# 디렉토리 구조
```bash
| .gitignore  
| app.py  
| directory_structure.txt  
| faq_data.json  
| README.md  
| requirements.txt  
+---1st_Project_crawling  
| | crawling.py  
| | faq.py  
| |  
| ---json  
|     crawling.py  
|     regist.py  
+---car_cnt  
|     .gitkeep  
+---data_city  
|     .gitkeep  
+---db  
|     db_insert.py  
|     DDL.sql 
+---img_readme  
|     ERD.png  
|     erd_fin.png  
|     minions_main.jpg  
|     minion_jy.jpg  
|     minion_kw.jpg  
|     minion_sy.jpg  
|     minion_yj.jpg  
|     sk_encore.png  
|     요구사항 명세서.png  
---pages  
    02_2019.py  
    03_2020.py  
    04_2021.py  
    05_2022.py  
    06_2023.py  
    07_2024.py
```
# 한 줄 회고
🤖<b>이광운</b>🤖\
Streamlit session_state를 잘 고려하자.... 테스트는 여러 기기에서 꼭 해보자 

🐧<b>이윤재</b>🐧\
Table에서 컬럼 수정이  필요할 때,  Database에서 차트를 구성할 때 필요한 자료를 어디에서 가져올지, 모두 ERD가 바탕이 된다는 것을 깨닫고 사전 ERD 작업의 중요성을 느끼게 되었다.

🐵<b>임수연</b>🐵\
셀레니움 코드를 짜고 크롤링 하여 DB저장 후 웹앱 제작까지 지난 2주간 배웠던 것들을 이틀동안 다양하게 시도하여 깨달음이 많은 이틀이었습니다🫠

🍊<b>허정윤</b>🍊\
셀레니움에서 웹 엘리먼트 조회 및 조작 간 페이지 새로고침 및 이동 상황 등을 잘 고려해서 구현해야 하는 점이랑 데이터 피버팅을 고려하여 모델링을 작업해야 데이터 혹은 데이터프레임 조작에 유리하단걸 깨달았다..
