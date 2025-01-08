# import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
import traceback

# MySQL 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="비밀번호",
    database="ecardb",
)
#DB CREATE 피저는 추가할 것!!! 
#일단 주석으로 설명 + 리드미에 추가할 것

# db폴더 ddl.spl 실행할 것것

# MySQL 커서 생성
# cursor = conn.cursor()
cursor = conn.cursor(buffered=True)

# 데이터베이스 초기화
cursor.execute("SET FOREIGN_KEY_CHECKS = 0; ")
cursor.execute("TRUNCATE TABLE electric_car_registration")
cursor.execute("TRUNCATE TABLE electric_car_subsidy")
cursor.execute("TRUNCATE TABLE sido")
cursor.execute("TRUNCATE TABLE car_subsidy_2019")
cursor.execute("TRUNCATE TABLE car_subsidy_2020")
cursor.execute("TRUNCATE TABLE car_subsidy_2021")
cursor.execute("TRUNCATE TABLE car_subsidy_2022")
cursor.execute("TRUNCATE TABLE car_subsidy_2023")
cursor.execute("TRUNCATE TABLE car_subsidy_2024")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1; ")

# Chrome 웹드라이버 설정
options = webdriver.ChromeOptions()
# options.add_argument("headless")
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
    for year in [option.text for option in select_element.options]:
        try:
            if year == "2025":  # 특정 연도 제외
                continue
            # year = option.text
            print(f"현재 연도 처리 중: {year}")

            # Select 요소를 매번 다시 가져오기
            select_element = Select(
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "year1"))
                )
            )
            select_element.select_by_visible_text(year)

            # 버튼 요소를 다시 가져오기
            # button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "조회")]'))
            # )
            button = driver.find_element(By.XPATH, '//button[contains(text(), "조회")]')
            button.click()

            # 텍스트가 특정 연도로 변경될 때까지 대기
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.ID, "title_year"), year)
            )

            data = []
            # editForm > div.contentList.fz13 > table > tbody > tr:nth-child(1)
            ## TODO: 전기차 출고대수 데이터 수집
            tbody = driver.find_elements(By.TAG_NAME, "tbody")[1]
            trs = tbody.find_elements(By.TAG_NAME, "tr")
            print("출고대수 데이터 수집 중...")
            for tr in trs:
                td = tr.find_elements(By.TAG_NAME, "td")
                count = ""
                if year == "2019":
                    count = td[6].text.split("\n")[0].strip()
                elif year == "2020":
                    if td[2].text != "승용":
                        continue
                    count = td[7].text.split("\n")[0].strip()
                else:
                    count = td[7].text.split("\n")[0].strip()
                # print(td[0].text, "|", td[1].text, "|", td[2].text, "|" , count)
                count = count.replace(",", "")
                if count == "":
                    count = 0
                entry = {
                    "시도": td[0].text.strip(),
                    "지역구분": td[1].text.strip(),
                    "차종구분": (
                        td[2].text.strip()
                        if td[2].text not in ["", "다운로드"]
                        else "전기승용"
                    ),
                    "출고대수": count,
                }
                cursor.execute(
                    "SELECT id FROM sido WHERE division = %s", (entry["지역구분"],)
                )

                try:
                    sido_id = cursor.fetchone()[0]
                except:
                    cursor.execute(
                        "INSERT INTO sido (name, division) VALUES (%s, %s)",
                        (entry["시도"], entry["지역구분"]),
                    )
                    conn.commit()
                    sido_id = cursor.lastrowid

                cursor.execute(
                    "INSERT INTO electric_car_registration (sido_id, year, class, regists) VALUES (%s, %s, %s, %s)",
                    (sido_id, year, entry["차종구분"], entry["출고대수"]),
                )

                # data.append(entry)
            conn.commit()
            print("출고대수 데이터 수집 완료\n")
        except Exception as e:
            print(f"연도 {year} 처리 중 에러 발생: {str(e)}")
            continue
            # 연도별 데이터 저장 (각 연도마다 개별 JSON 파일 생성)
            # with open(
            #     f"car_cnt/car_cnt_{year}.json", "w", encoding="utf-8"
            # ) as json_file:
            #     json.dump(
            #         {"연도": year, "데이터": data},
            #         json_file,
            #         ensure_ascii=False,
            #         indent=4,
            #     )
            # 체크포인트 : 출고대수를 크롤링 할동안 새로운 창 열려 에러가 발생할 수 있음
    # 'year1' select 요소 로드 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "year1")))
    select_element = Select(driver.find_element(By.ID, "year1"))
    for option in select_element.options:
        year = option.text
        if year == "2025":  # 특정 연도 제외
            continue
        try:
            select_element = Select(
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "year1"))
                )
            )
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
            # continue
            # 데이터 수집
            rows = driver.find_elements(By.CSS_SELECTOR, "table.table01 tbody tr")
            data = []
            print("보조금 데이터 수집 중...")
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if len(cols) >= 7:
                    entry = {
                        "시도": cols[0].text.strip(),
                        "지역구분": cols[1].text.strip(),
                        "보조금/승용(만원)": cols[3].text.strip().replace(",", ""),
                        # "보조금/초소형(만원)": cols[4].text.strip(),
                        # "보조금/화물(만원)": cols[5].text.strip(),
                        # "보조금/승합(만원)": cols[6].text.strip(),
                    }

                    if entry["보조금/승용(만원)"] == "":
                        entry["보조금/승용(만원)"] = 0

                    try:
                        cursor.execute(
                            "SELECT id FROM sido WHERE division = %s",
                            (entry["지역구분"],),
                        )

                        try:
                            sido_id = cursor.fetchone()[0]
                        except:
                            cursor.execute(
                                "INSERT INTO sido (name, division) VALUES (%s, %s)",
                                (entry["시도"], entry["지역구분"]),
                            )
                            conn.commit()
                            sido_id = cursor.lastrowid

                        cursor.execute(
                            "INSERT INTO electric_car_subsidy (sido_id, year, subsidy) VALUES (%s, %s, %s)",
                            (sido_id, year, entry["보조금/승용(만원)"]),
                        )
                    except Exception as e:
                        print(f"보조금 데이터 삽입 중 에러 발생: {str(e)}")

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

                                # 2023년의 경우 열이 하나 더 있음 (6개가 아닌 7개 열)
                                if year == "2023":
                                    if len(sub_cols) >= 7:
                                        sub_data.append(
                                            {
                                                "차종": sub_cols[0].text.strip(),
                                                "제조사": sub_cols[1].text.strip(),
                                                "모델명": sub_cols[2].text.strip(),
                                                "국비(만원)": sub_cols[3].text.strip(),
                                                "지방비(만원)": sub_cols[
                                                    4
                                                ].text.strip(),
                                                "보급목표이행보조금(만원)": sub_cols[
                                                    5
                                                ].text.strip(),  # 추가된 열 처리
                                                "보조금(만원)": sub_cols[
                                                    6
                                                ].text.strip(),
                                            }
                                        )
                                else:
                                    if len(sub_cols) >= 6:  # 일반적인 경우 6개의 열 처리
                                        sub_data.append(
                                            {
                                                "차종": sub_cols[0].text.strip(),
                                                "제조사": sub_cols[1].text.strip(),
                                                "모델명": sub_cols[2].text.strip(),
                                                "국비(만원)": sub_cols[3].text.strip(),
                                                "지방비(만원)": sub_cols[
                                                    4
                                                ].text.strip(),
                                                "보조금(만원)": sub_cols[
                                                    5
                                                ].text.strip(),
                                            }
                                        )
                                sub_data_entry = sub_data[-1]
                                car_class = sub_data_entry['차종']
                                model = sub_data_entry['모델명']
                                total_subsidy = sub_data_entry["보조금(만원)"].replace(",", "")
                                if total_subsidy == "":
                                    total_subsidy = 0

                                insert_query = f"""
                                    INSERT INTO car_subsidy_{year} (year, sido_id, car_class, model, total_subsidy)
                                    VALUES (%s, %s, %s, %s, %s)
                                """
                                cursor.execute(insert_query, (year, sido_id, car_class, model, total_subsidy))

                            # 추가 데이터를 entry에 저장
                            # entry["차종별 보조금"] = sub_data

                            # 창 닫기 및 원래 창으로 복귀
                            driver.close()
                            driver.switch_to.window(driver.window_handles[-1])

                        except Exception as e:
                            print(
                                f"추가 데이터 수집 중 에러 발생 (연도: {year}, 시도: {entry['시도']}): {str(e)}"
                            )
                            driver.switch_to.window(driver.window_handles[-1])
                conn.commit()
                    # data.append(entry)

            # 연도별 데이터 저장 (각 연도마다 개별 JSON 파일 생성)
            # with open(f"subsidy_data_{year}.json", "w", encoding="utf-8") as json_file:
            #     json.dump(
            #         {"연도": year, "데이터": data},
            #         json_file,
            #         ensure_ascii=False,
            #         indent=4,
            #     )
            print(f"{year}년 데이터 저장 완료\n")

            # 창 닫기 및 원래 창으로 복귀
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"연도 {year} 처리 중 에러 발생: {str(e)}")
            driver.switch_to.window(driver.window_handles[0])
            print(e.with_traceback(None))
            print(traceback.format_exc())
            continue
    conn.commit()
    cursor.close()
    conn.close()

except Exception as e:
    print(f"스크립트 실행 중 에러 발생: {str(e)}")
finally:
    driver.quit()