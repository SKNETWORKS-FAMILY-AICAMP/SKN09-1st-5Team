from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

chrome_options = Options()
# chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않으려면 이 주석을 제거하세요.

# ChromeDriver 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 크롤링하려는 URL
url = "https://ev.or.kr/nportal/partcptn/initFaqAction.do"  

# 웹 페이지 열기
driver.get(url)

wait = WebDriverWait(driver, 10)  # 최대 10초 대기
wait.until(EC.presence_of_all_elements_located((By.ID, "searchValue")))  # 검색 입력 필드가 나타날 때까지 대기

# 검색 입력 필드 찾기
search_box = driver.find_element(By.ID, "searchValue")

# "전기"라는 글씨를 입력
search_box.send_keys("전기")

# 검색 버튼 클릭 (엔터키 대신 버튼 클릭을 사용)
enter_box = driver.find_element(By.CSS_SELECTOR, "#frm > div.leftRight > div.right > span > button")
enter_box.click()

# 페이지 로딩 기다리기 (검색 결과가 로드될 때까지)
time.sleep(3)  # 페이지 로딩 시간에 맞춰 대기 시간 조정

# 제목과 답변 찾기 (제목의 CSS 선택자 변경)
titles = driver.find_elements(By.CSS_SELECTOR, "#subPage > div > div > div.contentList > div > div.faq_title > div.title")
answers = driver.find_elements(By.CSS_SELECTOR, "#subPage > div > div > div.contentList > div > div.faq_con > div:nth-child(2)")

# 데이터 저장 리스트
data = []

# 제목과 답변을 따로 append로 저장
for i in range(len(titles)):
    # 각 제목에 대응되는 답변이 있는지 확인
    answer_text = "답변 없음"  # 기본값 설정
    if i < len(answers):
        answer_text = answers[i].text.strip()  # 답변이 있을 경우
    title_text = titles[i].text.strip()  # 제목은 항상 존재
    data.append({"제목": title_text, "답변": answer_text})


next_btn = driver.find_element(By.CSS_SELECTOR, "#pageingPosition > a.next.arrow ")
next_btn.click()
time.sleep(3)  # 페이지 로딩 시간에 맞춰 대기 시간 조정


titles = driver.find_elements(By.CSS_SELECTOR, "#subPage > div > div > div.contentList > div > div.faq_title > div.title")
answers = driver.find_elements(By.CSS_SELECTOR, "#subPage > div > div > div.contentList > div > div.faq_con > div:nth-child(2)")

for i in range(len(titles)):
    # 각 제목에 대응되는 답변이 있는지 확인
    answer_text = "답변 없음"  # 기본값 설정
    if i < len(answers):
        answer_text = answers[i].text.strip()  # 답변이 있을 경우
    title_text = titles[i].text.strip()  # 제목은 항상 존재
    data.append({"제목": title_text, "답변": answer_text})
 

# 데이터 출력 (제목과 답변만)
for item in data:
    print(f"제목: {item['제목']}")
    print(f"답변: {item['답변']}")
    print("-" * 50)  # 구분선


# 제목과 답변을 저장할 리스트

# JSON 파일로 저장
with open('faq_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("데이터가 'faq_data.json' 파일에 저장되었습니다.")
    

# 브라우저 종료
driver.quit()
