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
- Spatial_data_preprocessing.ipynb : 인근 500m 공간feature 만드는 코드(일부)

4) Data
- Spatial data.csv : 최종 공간 데이터
- Weather data.csv : 날씨 데이터
- weekday_re_df_1021.pkl : 2022년도 1-12월 과거 대여량
- spatial_feature_1021_scaled.pkl : 공간 feature (GCN)
- weekday_weather_df.pkl : 2022년도 날씨 feature (GCN)

4) Result
- GCN_Analysis.ipynb : GCN-pro 결과분석 코드

5) Research
- 한국인공지능학회(포스터발표ver).pdf
- 디지털미디어학회(KCI논문등재ver).hwp
