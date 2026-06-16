# 권효중 SQL 미니 프로젝트
# 자소설 닷컴 크롤링 코드

# 라이브러리 불러오기
from urllib.request import urlopen,Request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

jaso_dict = {'회사':[],'업종':[],'전공':[],'학점':[],'토익':[],'자격증':[]}


for i in range(1,9):
    url = f'https://jasoseol.com/search?page={i}&division=1&dutyGroupIds=167'
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    link_list1 = soup.select('a.block')
    # 2번째 링크를 통해 연결
    for link in link_list1:
        com = link.text
        link = link['href']
        url2 = 'https://jasoseol.com' + link
        driver2 = webdriver.Chrome()
        driver2.get(url2)
        wait = WebDriverWait(driver2, 10)
        wait.until(lambda d: "undefined" not in d.find_element(By.CSS_SELECTOR, 'a.filter2-p').get_attribute("href"))
        soup2 = BeautifulSoup(driver2.page_source, 'html.parser')
        
        # 3번째 링크를 통해 연결
        link2 = soup2.select_one('a.filter2-p')['href']
        url3 = 'https://jasoseol.com' + link2
        driver3 = webdriver.Chrome()
        driver3.get(url3)
        soup3 = BeautifulSoup(driver3.page_source, 'html.parser')
        
        # 크롤링
        try:
            jaso_dict['회사'].append(soup3.select_one('h1.header5.text-gray-900').text)
            print('회사:',soup3.select_one('h1.header5.text-gray-900').text)
            jaso_dict['업종'].append(soup3.select_one('div.body5.text-gray-700').text)
            print('업종:',soup3.select_one('div.body5.text-gray-700').text)
            result = []
            for i in soup3.select('span.body6.flex-1.truncate')[6:]:
                result.append(i.text)
            jaso_dict['전공'].append(result)
            print('전공:',result)
            jaso_dict['학점'].append(soup3.select('span.header5.text-gray-800')[0].text)
            print('학점:',soup3.select('span.header5.text-gray-800')[0].text)
            jaso_dict['토익'].append(soup3.select('span.header5.text-gray-800')[3].text)
            print('토익:',soup3.select('span.header5.text-gray-800')[3].text)
            items = soup3.select('span.block.truncate')
            
            # image로 되어 있는 부분을 읽어오는 문제가 있어서  canvas 
            result2 = []
            for item in items:
            # 각 요소 내부의 canvas를 찾아 제거
                for canvas in item.find_all('canvas'):
                    canvas.decompose()
                result2.append(item.text)
                result2 = result2[:6] # 자격증 파트만 읽어오기
            jaso_dict['자격증'].append(result2)
            print('자격증:',result2)
                
            print('-'*80)

        except Exception as e:
            print(f'작업 실패: {com}')
            continue


print(jaso_dict)
df = pd.DataFrame(jaso_dict)
df.to_csv('jasoseol.csv',encoding='utf-8')



