# 권효중 miniproject_sql
# 

import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import koreanize_matplotlib

conn = pymysql.connect(host='172.30.1.4',user='kwon',
                       password=YOUR_PASSWORD,database='mini',charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)

query="""
SELECT e.year,e.region,e.empty_rate,e.empty_number,e.total_house,pi.personal_income,c.credit,eg.economy_growth,pr.price_index
FROM empty2 as e
    INNER JOIN personal_income2 as pi
    ON e.region_id = pi.region_id
    INNER JOIN credit2 as c
    ON pi.region_id = c.region_id
    INNER JOIN economy_growth as eg
    ON pi.region_id = eg.region_id
    INNER JOIN price_index2 as pr
    ON pi.region_id = pr.region_id
    
"""
# 큰 따옴표 사용 지향(내부에 문자열('')입력 용이)
# 마지막에 세미콜론 없음
 
cur.execute(query)

rows = cur.fetchall() # 모든 데이터를 가져옴
result_df = pd.DataFrame(rows) # DataFrame 형태로 변환

sns.lineplot(data=result_df,x='year',y='empty_rate',hue='region')
sns.barplot(data=result_df,x='region',y='empty_rate')
plt.show()
cur.close()
conn.close()


"""
SELECT e.year,e.region,e.empty_rate,pi.personal_income,cs.consumer5,cs.consumer4,c.credit,eg.economy_growth,ins.income5,ins.income4,pr.price_index
FROM empty2 as e
    INNER JOIN personal_income2 as pi
    ON e.region_id = pi.region_id
    INNER JOIN consumer_satisfaction as cs
    ON pi.region_id = cs.region_id
    INNER JOIN credit2 as c
    ON pi.region_id = c.region_id
    INNER JOIN economy_growth as eg
    ON pi.region_id = eg.region_id
    INNER JOIN income_satisfaction as ins
    ON pi.region_id = ins.region_id
    INNER JOIN price_index2 as pr
    ON pi.region_id = pr.region_id
    
"""