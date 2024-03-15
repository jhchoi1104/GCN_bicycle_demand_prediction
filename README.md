## 연구 주제: Predicting bicycle demand  at the station level by incorporating station-specific spatial features in graph convolutional network model
### 폴더
1) GCN
- GCN : GCN-pro, GCN-UP 코드 및 결과 시각화

2) Compare model
- LSTM
- CNN
- XGBoost
- ARIMA

3) Data preprocessing
- make_adj_sorted.py : 인접행렬 만드는 코드
- past_rental_matrix.ipynb : 특성행렬 만드는 코드(일부)
- make_bike_road.ipynb : 인근 500m 자전거도로 데이터 만드는 코드
- Spatial data preprocessing.ipynb : 인근 500m 공간feature 만드는 코드

4) Data
- Spatial data.csv : 최종 공간 데이터
- Weather data.csv : 날씨 데이터
- weekday_re_df_1021.pkl : 2022년도 1-12월 과거 대여량
- spatial_feature_1021_scaled.pkl : 공간 feature (GCN)
- weekday_weather_df.pkl : 2022년도 날씨 feature (GCN)

4) Result
- 한국 인공지능 학회 제출용.pdf
- Full_thesis(stage_editor).pdf : 최종 논문, Journal of Intelligent Transportation Systems 저널 제출 단계
- GCN_Analysis.ipynb : GCN-pro 결과분석 코드
