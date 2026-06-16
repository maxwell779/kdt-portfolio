# 권효중 SQL 미니 프로젝트
# 캐치 사이트 크롤링 코드
# IT개발 직무를 선택 후 빅데이터/AI 직무에서 만든 catch3.csv와 결합하는 코드


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

driver = webdriver.Chrome()
driver.get("https://www.catch.co.kr/NCS/RecruitSearch")

catch_dict = {'회사':[],'업종':[],'공고':[],'특징':[],'종합':[],'급여':[],'조직문화':[],'워라밸':[],
              '커리어':[],'경영진':[],'리뷰1':[],'리뷰1점수':[],
              '리뷰2':[],'리뷰2점수':[],
              '리뷰3':[],'리뷰3점수':[],
              '리뷰4':[],'리뷰4점수':[],
              '리뷰5':[],'리뷰5점수':[]}

# 캐치 사이트의 경우 url이 바뀌는 게 아니라 버튼을 클릭하면 바뀌기 때문에 다음과 같이 클릭하게 설정
try:
    wait = WebDriverWait(driver, 20)

    # 1. '직무' 버튼 클릭 (이미 selected여도 클릭해서 메뉴 활성화 확인)
    job_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '직무')]")))
    driver.execute_script("arguments[0].click();", job_btn)

    # 2. 'IT개발' 클릭
    ai_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='IT개발']")))
    driver.execute_script("arguments[0].click();", ai_btn)

    # 3. '채용구분' 버튼 클릭 (메뉴를 펼쳐야 '신입'이 보입니다)
    recruit_type_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '채용구분')]")))
    driver.execute_script("arguments[0].click();", recruit_type_btn)

    # 4. '신입' 라벨 클릭
    # input은 숨겨져 있는 경우가 많으므로 사용자에게 보이는 'label'을 클릭합니다.
    freshman_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='career_1']")))
    driver.execute_script("arguments[0].click();", freshman_label)

    # 5. 데이터 로딩 대기
    # 데이터가 포함된 테이블이나 리스트가 나타날 때까지 기다립니다.
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tdlink.al")))
    
    time.sleep(2) # 필터 적용 후 리스트 갱신 잠시 대기

    # [2] 페이지 순회 (예: 1페이지부터 3페이지까지)
    # page가 바뀌어도 url이 바뀌지 않기 때문에 버튼을 누르도록 설정
    for page_num in range(1, 4):
        print(f"\n--- 현재 {page_num}페이지 수집 중 ---")
        
        if page_num > 1:
            # 해당 숫자의 페이지 버튼 클릭
            page_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{page_num}']")))
            driver.execute_script("arguments[0].click();", page_btn)
            time.sleep(2) # 페이지 전환 대기

        # [3] 기업명 추출
        # .tdlink.al 내부의 .name2 클래스 텍스트 추출
        companies = driver.find_elements(By.CSS_SELECTOR, "a.tdlink.al")
        
        # 
        for element in companies:
            try:
                # 1. 회사 정보가 담긴 링크인지 확인 (.name2 존재 여부)
                name_tags = element.find_elements(By.CLASS_NAME, 'name2')
                if name_tags:
                    name = name_tags[0].text.strip()
                    catch_dict['회사'].append(name)
            
                    # 리뷰 페이지 URL 생성 및 상세 정보 크롤링 (Requests + BeautifulSoup)
                    link = element.get_attribute('href')
                    comp_id = link.split('/')[-1]
                    review_url = f'https://www.catch.co.kr/Comp/ReviewInfo/{comp_id}'
            
                    resp = requests.get(review_url, headers={'User-Agent': 'Mozilla/5.0'})
                    soup = BeautifulSoup(resp.text, 'html.parser')

                    # 점수 및 항목별 데이터 추출 (IndexError 방지를 위한 select 사용)
                    score_tag = soup.select_one('p.score')
                    catch_dict['종합'].append(score_tag.text if score_tag else "N/A")
            
                    fills = soup.select('span.fill')
                    # 상세 지표가 충분히 있을 때만 저장
                    if len(fills) >= 6:
                        catch_dict['급여'].append(fills[1].text)
                        catch_dict['조직문화'].append(fills[2].text)
                        catch_dict['워라밸'].append(fills[3].text)
                        catch_dict['커리어'].append(fills[4].text)
                        catch_dict['경영진'].append(fills[5].text)
                    else:
                        for key in ['급여', '조직문화', '워라밸', '커리어', '경영진']:
                            catch_dict[key].append("N/A")
                    
                    items = soup.select('li.item p.txt')
                    if len(items) >= 5:
                        for i in range(5):
                            # p.txt 내부의 모든 span 태그를 가져옵니다.
                            spans = items[i].find_all('span')
        
                            # 첫 번째 span은 리뷰 내용, 두 번째 span은 점수(백분율)
                            content = spans[0].get_text(strip=True) if len(spans) > 0 else "N/A"
                            score = spans[1].get_text(strip=True) if len(spans) > 1 else "N/A"
        
                            catch_dict[f'리뷰{i+1}'].append(content)
                            catch_dict[f'리뷰{i+1}점수'].append(score)
                    else:
                        for key in ['리뷰1','리뷰1점수','리뷰2','리뷰2점수','리뷰3','리뷰3점수','리뷰4','리뷰4점수','리뷰5','리뷰5점수']:
                            catch_dict[key].append("N/A")

                # 2. 공고 제목이 담긴 링크인지 확인 (.subj2 존재 여부)
                subj_tags = element.find_elements(By.CLASS_NAME, 'subj2')
                if subj_tags:
                    subj = subj_tags[0].text.strip()
                    catch_dict['공고'].append(subj)
            
                    # 공고 상세 페이지 특징 추출
                    recruit_link = element.get_attribute('href')
                    resp2 = requests.get(recruit_link, headers={'User-Agent': 'Mozilla/5.0'})
                    soup2 = BeautifulSoup(resp2.text, 'html.parser')
            
                    txt_tags = soup2.select('p.txt')
                    catch_dict['특징'].append(txt_tags[1].text if len(txt_tags) > 1 else "N/A")
                    catch_dict['업종'].append(soup2.select('div.cont_corp div.info2 span.txt')[1].text)

            except Exception as e:
                print(f"항목 수집 중 오류 발생 (건너뜀): {e}")
                continue


except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()

# 만든 catch3.csv와 데이터프레임 결합
df1 = pd.read_csv('catch3.csv')

df2 = pd.DataFrame(catch_dict)
df = pd.concat([df1,df2], ignore_index=True)
df = df.drop_duplicates()

print(tabulate(df, headers='keys', tablefmt='grid'))
df.to_csv('catch4.csv',index=False)