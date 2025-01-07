import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 웹사이트 열기
url = "https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do"
driver.get(url)


    # 'year1' select 요소 로드 대기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "year1")))

select_element = Select(driver.find_element(By.ID, "year1"))

    # 옵션 확인
if not select_element.options:
    print("연도 옵션이 없습니다.")
    driver.quit()
    exit()

for option in select_element.options:
    try:
        year = option.text
        if year == "2025":  # 특정 연도 제외
            continue
        print(f"현재 연도 처리 중: {year}")


        data = []
        # tbody 요소가 로드될 때까지 기다리기
        tbody_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "tbody"))
        )

        # 2번째 tbody가 있을 경우 처리
        if len(tbody_elements) > 1:
            tbody = tbody_elements[1]
            trs = tbody.find_elements(By.TAG_NAME, "tr")

            for tr in trs:
                td = tr.find_elements(By.TAG_NAME, "td")
                count = 0
                if year == "2019":
                    count = td[6].text.split('\n')[0].strip()
                elif year == "2020":
                    if td[2].text != "승용":
                        continue
                    print("2020년도 수집")
                    count = td[7].text.split('\n')[0].strip()
                else:
                    count = td[7].text.split('\n')[0].strip()

                print(td[0].text, "|", td[1].text, "|", td[2].text, "|", count)

                entry = {
                    "시도": td[0].text,
                    "지역구분": td[1].text,
                    "차종구분": td[2].text if td[2].text != "다운로드" else "전기승용",
                    "출고대수": count
                }
                data.append(entry)

            # 연도별 데이터 저장 (각 연도마다 개별 JSON 파일 생성)
            with open(f"car_cnt/car_cnt_{year}.json", "w", encoding="utf-8") as json_file:
                json.dump(
                    {"연도": year, "데이터": data},
                    json_file,
                    ensure_ascii=False,
                    indent=4,
                )
        else:
            print(f"연도 {year}에 대한 tbody 요소를 찾을 수 없습니다.")
    except Exception as e:
        print(f"연도 {year} 처리 중 오류 발생: {e}")
