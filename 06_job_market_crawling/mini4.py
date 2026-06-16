# 권효중 SQL 미니 프로젝트
# 잡코리아 사이트 크롤링 코드
# 빅데이터/AI 직무와 관련된 직무를 모두 선택 후 검색 후 크롤링하는 코드
# Ai 좀 참고했습니다. 

# 라이브러리 불러오기
from urllib.request import urlopen,Request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
import time
from tabulate import tabulate

# 딕셔너리 설정
job_dict = {'회사':[],'공고':[],'업종':[],'업무':[],'경력':[],'학력':[],'스킬':[],'조건':[]}

driver = webdriver.Chrome()
driver.get("https://www.jobkorea.co.kr/recruit/joblist?menucode=duty")

wait = WebDriverWait(driver, 10) # 최대 10초 대기 설정

# url이 바뀌지 않기 때문에 버튼을 눌르고 검색하여서 크롤링
try:

    # --- 1단계: 상위 카테고리 (AI·개발·데이터) 클릭 ---
    # label의 for 속성으로 클릭
    step1_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step1_10031']")))
    step1_btn.click()
    
    # --- 2단계: 직무 (데이터엔지니어) 클릭 ---
    # 클릭 후 리스트가 로딩될 시간을 고려하여 대기
    step2_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000236']")))
    step2_btn.click()
    # 데이터사이언티스트
    step3_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000237']")))
    step3_btn.click()
    # 소프트웨어개발자
    step4_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000239']")))
    step4_btn.click()
    # AI/ML 엔지니어
    step5_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000242']")))
    step5_btn.click()
    # AI/ML 연구원
    step6_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000417']")))
    step6_btn.click()
    # 데이터분석가
    step7_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000418']")))
    step7_btn.click()
    # MLOps엔지니어
    step8_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000422']")))
    step8_btn.click()
    # AI서비스개발자
    step9_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='duty_step2_1000423']")))
    step9_btn.click()
    
    # 3단계 경력 클릭
    career1_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), '경력')]")))
    career1_tab.click()
    # --- 4단계: 경력 (신입) 클릭 ---
    # 경력 탭이 활성화되어 있는지 확인 후 클릭
    career2_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='career1']")))
    career2_btn.click()

    # --- 4단계: 검색 버튼 클릭 ---
    search_btn = wait.until(EC.element_to_be_clickable((By.ID, "dev-btn-search")))
    search_btn.click()

    # --- 5단계: 결과 로딩 대기 및 크롤링 ---
    time.sleep(5) # 검색 결과가 반영되는 시간 대기
    
    # [2] 페이지 순회 (예: 1페이지부터 11페이지까지)
    for page_num in range(1, 12):
        print(f"\n--- 현재 {page_num}페이지 수집 중 ---")
        
        # 1~10페이지 도앙ㄴ 코드
        if page_num > 1 and page_num % 10 !=1:
            # 해당 숫자의 페이지 버튼 클릭
            page_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{page_num}']")))
            driver.execute_script("arguments[0].click();", page_btn)
            time.sleep(2) # 페이지 전환 대기
        # 페이지 11페이지는 10페이지에서 다음 버튼을 누르면 11페이지로 감
        elif page_num > 1 and page_num % 10 == 1:
            page_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='다음']")))
            driver.execute_script("arguments[0].click();", page_btn)
            time.sleep(2) # 페이지 전환 대기
        
        # [3] 기업명 추출
        # .tdlink.al 내부의 .name2 클래스 텍스트 추출
        companies = driver.find_elements(By.CSS_SELECTOR, "a.link.normalLog")
        td_dsc = driver.find_elements(By.CSS_SELECTOR,"td.tplTit")
        
        
        companies = driver.find_elements(By.CSS_SELECTOR, "a.link.normalLog")
        td_dsc = driver.find_elements(By.CSS_SELECTOR, "td.tplTit")

        # 회사와 공고 제목은 리스트 내에서 2개씩 한 쌍이므로 슬라이싱으로 짝을 맞춥니다.
        # (0, 2, 4...) 인덱스는 회사, (1, 3, 5...) 인덱스는 공고 제목
        
        company_list = companies[:-20][0::2]
        title_list = companies[:-20][1::2]
        dsc_list = td_dsc[:-10] # 업무(dsc) 리스트

        for company_elem, title_elem, td_elem in zip(company_list, title_list, dsc_list):
            try:
                # 1. 목록 페이지 기본 정보 추출
                company = company_elem.text
                job_op = title_elem.text
                url = title_elem.get_attribute('href')
                
                # 업무(dsc) 추출
                dsc_tag = td_elem.find_elements(By.CSS_SELECTOR, "p.dsc")
                dsc = dsc_tag[0].text if dsc_tag else None

                # 2. 상세 페이지 데이터 초기값 (실패 시 None 유지를 위함)
                career_text = edu_text = skill_text = condition_text = industry = None

                try:
                    # 상세 페이지 접속
                    driver2 = webdriver.Chrome()
                    driver2.get(url)
                    wait2 = WebDriverWait(driver2, 15)
                    wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-sentry-component='Qualification']")))
                    
                    soup = BeautifulSoup(driver2.page_source, 'html.parser')

                    # 지원자격 항목 파싱
                    # '경력,학력,스킬,우대조건 뒤에 text를 불러오는 코드
                    items = soup.find_all('div', attrs={'data-sentry-component': 'QualificationItem'})
                    for item in items:
                        label_tag = item.find('span', attrs={'data-accent-color': 'gray700'})
                        if not label_tag: continue
                        
                        label_name = label_tag.get_text(strip=True)
                        data_nodes = label_tag.find_next_siblings()
                        content = " ".join([node.get_text(separator=" ", strip=True) for node in data_nodes]).strip()
                        clean_val = content.lstrip(',. ').strip() if content else None
                        
                        

                        if '경력' in label_name: career_text = clean_val
                        elif '학력' in label_name: edu_text = clean_val
                        elif '스킬' in label_name: skill_text = clean_val
                        elif '우대조건' in label_name:
                            condition_text = clean_val.replace("기본우대", "").lstrip(',. ').strip()
                    
                    # 업종 추출 (인덱스 에러 방지)
                    try:
                        corp_boxes = soup.find_all('div', attrs={'data-sentry-component': 'CorpInformationBox'})
                        if len(corp_boxes) >= 3:
                            industry = corp_boxes[2].find('div', {'data-accent-color': 'gray900'}).get_text(strip=True)
                    except: industry = None

                except Exception as detail_e:
                    print(f"상세 페이지({job_op}) 수집 중 일부 오류 발생: {detail_e}")
                    # 일부 수집 실패해도 아래 append는 실행되어 길이를 맞춤
                
                finally:
                    if 'driver2' in locals(): driver2.quit()


                job_dict['회사'].append(company)
                job_dict['공고'].append(job_op)
                job_dict['업무'].append(dsc)
                job_dict['경력'].append(career_text)
                job_dict['학력'].append(edu_text)
                job_dict['스킬'].append(skill_text)
                job_dict['조건'].append(condition_text)
                job_dict['업종'].append(industry)
                print('회사',company)
                print('업무',dsc)
                print('공고',job_op)
                print('경력',career_text)
                print('학력',edu_text)
                print('스킬',skill_text)
                print('조건',condition_text)
                print('업종',industry)

            except Exception as e:
                print(f"해당 공고 수집 실패 (건너뜀): {e}")
                continue


except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()

# csv 파일로 저장
count_dict = {k:len(v) for k,v in job_dict.items()}
print(count_dict)
df = pd.DataFrame(job_dict)
print(df)
df.to_csv('jobkorea.csv',index=False)
    
    