# KDT 12기 프로젝트 포트폴리오 — 권효중

> KDT(경북대 융복합연구원) AI·데이터 과정에서 수행한 프로젝트 모음입니다.
> 데이터 분석 → 머신러닝 → 딥러닝(CV)까지 단계적으로 진행했습니다.

📧 rnjsgywnd777@gmail.com ｜ 💻 [github.com/maxwell779](https://github.com/maxwell779) ｜ 📄 [Notion 포트폴리오](https://standing-whimsey-227.notion.site/_-10837ef64c53825b951681a9b18d1e72)

---

## ⭐ 독립 저장소 + Streamlit 앱 (실모델 구동)

아래 3개는 별도 저장소에서 **실제 학습된 모델로 구동되는 앱**을 제공합니다.

| 프로젝트 | 설명 | 저장소 |
|---|---|---|
| 🔥 산불·연기 실시간 탐지 | YOLOv8 실탐지 + **산림청용 관제 앱**(이미지·영상) · mAP50 0.78 | [wildfire-detection](https://github.com/maxwell779/wildfire-detection) · [▶️Demo](https://wildfire-detection-magbcdezyjoskgcholyiyw.streamlit.app/) |
| 💊 알약 이미지 이상탐지 | KNN 비지도 이상탐지 + **산업 검사 앱**(PASS/FAIL) · F2 0.85 | [pill-anomaly-detection](https://github.com/maxwell779/pill-anomaly-detection) · [▶️Demo](https://pill-anomaly-detection-azlwvnidzu4zjkahewyadp.streamlit.app/) |
| 📦 식료품 폐기 리스크 ML | 회귀·스태킹 + **폐기 예측 앱** · MAE 0.0337 | [grocery-waste-ml](https://github.com/maxwell779/grocery-waste-ml) · [▶️Demo](https://grocery-waste-ml-5fezqfu8kdm8tm69kojv7g.streamlit.app/) |

---

## 📂 이 저장소의 프로젝트 (KDT 미니프로젝트)

| 프로젝트 | 분류 | 내 역할 | 핵심 성과 |
|---|---|---|---|
| [🔥 산불·연기 실시간 탐지](10_wildfire_detection) | 딥러닝(객체탐지) | 딥러닝 모델링·Hybrid | YOLO+ResNet Hybrid, mAP50 0.78 |
| [💊 알약 이미지 이상탐지](09_pill_anomaly_cv) | 컴퓨터비전 | KNN 모델 담당(PCA)·BEST 선정 | Color-Specific k-NN F2 0.85 |
| [📦 식료품 폐기 리스크 ML](08_grocery_waste_ml) | 머신러닝 | 폐기 회귀·스태킹 | 스태킹 MAE 0.0337 |
| [💼 채용시장 크롤링 분석](06_job_market_crawling) | 데이터 수집 | 단독 | Selenium 900건, ADsP·SQLD 도출 |
| [🏠 빈집 영향 요인 (SQL)](05_empty_house_sql) | SQL/DB | 소득 파트·소득 테이블 설계 | 다중 JOIN·합성키, 소득↔빈집 -0.32 |
| [🏀 NBA 소포모어 징크스](07_nba_sophomore_jinx) | 통계분석 | 단독 | 동명이인 분리, "징크스 없음" 검증 |
| [🏅 올림픽 메달 분석](03_olympic_medal_analysis) | 데이터 시각화 | 종목 분류·상관 | 52종목→7분류, GDP 상관 0.90 |
| [🌡 기후-자연재해 분석](04_climate_disaster) | 공공데이터 | 산불 파트 | 습도↔산불 -0.62 |
| [🦟 모기 개체수 예측](02_mosquito_prediction) | 데이터 분석 | 전처리·회귀 | 강수 시차분석 "성충화 14~16일" |
| [🐍 Python 기초 GUI](01_python_basic) | 기초 | 단독 | Tkinter 문서 분석기 |

---

## 🔗 다른 주요 프로젝트 (별도 저장소)

| 프로젝트 | 설명 | 링크 |
|---|---|---|
| 🏭 엠엔비전 버스바 결함 탐지 | 기업 프로젝트 · 비지도 이상탐지(Stage2 전담) · 외관 AUROC 0.994 | [repo](https://github.com/KDT12-mnvision/KDT12-mnvison/tree/feature/stage2-sweep-portfolio) |
| 📑 AJIN BizAI | 경진대회 본선 · 신청서 자동화 풀스택 | [repo](https://github.com/KDT12-AJIN-PROJECT/Ajin-BizAI) |
| 🗳 PolyElection 선거 대시보드 | FastAPI+MySQL 백엔드 전체 | [repo](https://github.com/maxwell779/korean_election_project) |
| 🤖 NEW LEARN 교육 챗봇 | EXAONE LoRA 파인튜닝(반도체) | [repo](https://github.com/new-learn12/new-learn) |
| 🐶 Paw-옹 유기견 매칭 | 팀장 · 가중치 추천 | [repo](https://github.com/paw-ong1/paw-ong) |

---

*각 폴더의 README에 프로젝트별 상세(역할·성과·결과 이미지)가 있습니다. 대부분 팀 프로젝트이며, 본인 역할을 명시했습니다.*
