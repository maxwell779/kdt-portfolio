# 알약 이미지 이상탐지

> 비지도 이상탐지(One-Class) · F2-score 채택

> 🔗 **전용 저장소 + 라이브 검사 앱**: [pill-anomaly-detection](https://github.com/maxwell779/pill-anomaly-detection) · [▶️ Live Demo](https://pill-anomaly-detection-azlwvnidzu4zjkahewyadp.streamlit.app/)

- **구성**: 팀(2팀) · 본인: **KNN 이상탐지 모델 담당(PCA 도입)·모델 비교/선정**
- **핵심 성과**: 11개 비교 후 **Color-Specific k-NN(F2 0.85 · Recall 0.84 · Precision 0.875)** 본인 선정 BEST
  - ※ F2 0.964짜리(Recall 1.0)는 임계 0의 "전부 불량" 과적합이라 배제

![confusion_matrix.png](images/confusion_matrix.png)
![defect_sample.png](images/defect_sample.png)
![f2_comparison.png](images/f2_comparison.png)
