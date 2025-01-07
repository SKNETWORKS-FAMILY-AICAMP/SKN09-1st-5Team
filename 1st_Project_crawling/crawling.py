import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome 웹드라이버 설정
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

# 웹사이트 열기
url = "https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do"
driver.get(url)

try:
    # 'year1' select 요소 로드 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "year1")))
    select_element = Select(driver.find_element(By.ID, "year1"))

    # 옵션 확인
    if not select_element.options:
        print("연도 옵션이 없습니다.")
        driver.quit()
        exit()
    # 옵션 순회
    # options = select_element.options[:]
    
    for year in ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]:
        try:
            if year == "2025":  # 특정 연도 제외
                continue
            # year = option.text
            print(f"현재 연도 처리 중: {year}")
            
            # Select 요소를 매번 다시 가져오기
            select_element = Select(WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "year1"))
            ))
            select_element.select_by_visible_text(year)
            
            # 버튼 요소를 다시 가져오기
            # button = WebDriverWait(driver, 20).until(
            #     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "조회")]'))
            # )
            button = driver.find_element(By.XPATH, '//button[contains(text(), "조회")]')
            button.click()

            # 텍스트가 특정 연도로 변경될 때까지 대기
            WebDriverWait(driver, 20).until(
                EC.text_to_be_present_in_element((By.ID, "title_year"), year)
            )

            data = []
            # editForm > div.contentList.fz13 > table > tbody > tr:nth-child(1)
            ## TODO: 전기차 출고대수 데이터 수집
            tbody = driver.find_elements(By.TAG_NAME, "tbody")[1]
            trs = tbody.find_elements(By.TAG_NAME, "tr")
            for tr in trs:
                td = tr.find_elements(By.TAG_NAME, "td")
                count = ""
                if year == "2019":
                    count = td[6].text.split('\n')[0].strip()
                elif year == "2020":
                    if td[2].text != "승용":
                        continue
                    print("2020년도 수집")
                    count = td[7].text.split('\n')[0].strip()
                else:
                    count = td[7].text.split('\n')[0].strip()
                print(td[0].text, "|", td[1].text, "|", td[2].text, "|" , count)
                count = count.replace(",", "")
                if count == "":
                    count = 0
                entry = {
                    "시도": td[0].text.strip(),
                    "지역구분": td[1].text.strip(),
                    "차종구분": td[2].text.strip() if td[2].text not in ["","다운로드"] else "전기승용",
                    "출고대수": count,
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
            # 체크포인트 : 출고대수를 크롤링 할동안 새로운 창 열려 에러가 발생할 수 있음    

            # 연도 선택
            select_element.select_by_visible_text(year)
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnLocalCarPrc"))
            )
            button.click()

            # 새 창으로 전환
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            driver.switch_to.window(driver.window_handles[-1])

            # 테이블 데이터 로드 대기
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "table.table01 tbody tr")
                )
            )

            # 데이터 수집
            rows = driver.find_elements(By.CSS_SELECTOR, "table.table01 tbody tr")
            data = []

            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if len(cols) >= 7:
                    entry = {
                        "시도": cols[0].text.strip(),
                        "지역구분": cols[1].text.strip(),
                        "보조금/승용(만원)": cols[3].text.strip(),
                        "보조금/초소형(만원)": cols[4].text.strip(),
                        "보조금/화물(만원)": cols[5].text.strip(),
                        "보조금/승합(만원)": cols[6].text.strip(),
                    }

                    # 2021년 이상인 경우, 버튼 클릭 후 추가 데이터 수집
                    if int(year) >= 2021:
                        try:
                            detail_button = row.find_element(
                                By.CSS_SELECTOR,
                                "a.btnDown[onclick^='psPopupLocalCarModelPrice']",
                            )
                            driver.execute_script(
                                "arguments[0].click();", detail_button
                            )

                            # 새 창 전환
                            WebDriverWait(driver, 10).until(
                                lambda d: len(d.window_handles) > 2
                            )
                            driver.switch_to.window(driver.window_handles[-1])

                            # 추가 테이블 데이터 로드 대기
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_all_elements_located(
                                    (By.CSS_SELECTOR, "table.table01 tbody tr")
                                )
                            )

                            # 추가 데이터 긁어오기
                            sub_rows = driver.find_elements(
                                By.CSS_SELECTOR, "table.table01 tbody tr"
                            )
                            sub_data = []
                            for sub_row in sub_rows:
                                sub_cols = sub_row.find_elements(By.TAG_NAME, "td")
                                if (
                                    len(sub_cols) >= 6
                                ):  # 차종, 제조사, 모델명 등 추가 항목 포함
                                    sub_data.append(
                                        {
                                            "차종": sub_cols[0].text.strip(),
                                            "제조사": sub_cols[1].text.strip(),
                                            "모델명": sub_cols[2].text.strip(),
                                            "국비(만원)": sub_cols[3].text.strip(),
                                            "지방비(만원)": sub_cols[4].text.strip(),
                                            "보조금(만원)": sub_cols[5].text.strip(),
                                        }
                                    )

                            # 추가 데이터를 entry에 저장
                            entry["차종별 보조금"] = sub_data

                            # 창 닫기 및 원래 창으로 복귀
                            driver.close()
                            driver.switch_to.window(driver.window_handles[-1])

                        except Exception as e:
                            print(
                                f"추가 데이터 수집 중 에러 발생 (연도: {year}, 시도: {entry['시도']}): {str(e)}"
                            )
                            driver.switch_to.window(driver.window_handles[-1])

                    data.append(entry)

            # 연도별 데이터 저장 (각 연도마다 개별 JSON 파일 생성)
            with open(f"subsidy_data_{year}.json", "w", encoding="utf-8") as json_file:
                json.dump(
                    {"연도": year, "데이터": data},
                    json_file,
                    ensure_ascii=False,
                    indent=4,
                )
            print(f"{year}년 데이터 저장 완료")

            # 창 닫기 및 원래 창으로 복귀
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"연도 {year} 처리 중 에러 발생: {str(e)}")
            driver.switch_to.window(driver.window_handles[0])
            continue

except Exception as e:
    print(f"스크립트 실행 중 에러 발생: {str(e)}")
finally:
    driver.quit()
