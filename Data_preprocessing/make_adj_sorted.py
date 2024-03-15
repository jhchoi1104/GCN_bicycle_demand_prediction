#!/usr/bin/env python3

import pandas as pd
import numpy as np

bicycle_01 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.01.csv',encoding='cp949')
bicycle_02 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.02.csv',encoding='cp949')
bicycle_03 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.03.csv',encoding='cp949')
bicycle_04 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.04.csv',encoding='cp949')
bicycle_05 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.05.csv',encoding='cp949')
bicycle_06 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.06.csv',encoding='cp949')
bicycle_07 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.07.csv',encoding='cp949')
bicycle_08 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.08.csv',encoding='cp949')
bicycle_09 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.09.csv',encoding='cp949')
bicycle_10 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.10.csv',encoding='cp949')
bicycle_11 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.11.csv',encoding='cp949')
bicycle_12 = pd.read_csv('/Users/jhchoi/Desktop/DS 캡스톤/bicycle_month/bicycle_22.12.csv',encoding='cp949')

bicycle_07 = bicycle_07.iloc[:,:11]
bicycle_08 = bicycle_08.iloc[:,:11]
bicycle_09 = bicycle_09.iloc[:,:11]
bicycle_10 = bicycle_10.iloc[:,:11]
bicycle_11 = bicycle_11.iloc[:,:11]
bicycle_12 = bicycle_12.iloc[:,:11]

bicycle_07.columns = bicycle_01.columns
bicycle_08.columns = bicycle_01.columns
bicycle_09.columns = bicycle_01.columns
bicycle_10.columns = bicycle_01.columns
bicycle_11.columns = bicycle_01.columns
bicycle_12.columns = bicycle_01.columns

raw = pd.concat([bicycle_01,bicycle_02,bicycle_03,bicycle_04,bicycle_05,bicycle_06,bicycle_07,bicycle_08,bicycle_09,bicycle_10,bicycle_11,bicycle_12])
print('concat is done')
raw = raw[raw['이용거리'] != 0]
print('이용거리 끝')

raw['반납대여소번호'] = raw['반납대여소번호'].astype(str).str.lstrip('0')
raw = raw[raw['반납대여소번호']!='\\N']
df = raw.loc[:,['대여 대여소번호','반납대여소번호']]
df['대여 대여소번호'] = df['대여 대여소번호'].astype(str)

print('Step1: 데이터 전처리 완료!')


# 대여소 ID 추출
station_ids = np.unique(np.concatenate([df['반납대여소번호'].astype(str).unique(), df['대여 대여소번호'].astype(str).unique()]))

station_ids = np.sort(station_ids.astype(int))
station_ids = station_ids.astype(str)

# 인접 행렬 초기화
adj_matrix = pd.DataFrame(0, index=station_ids, columns=station_ids)


# 데이터프레임을 순회하며 인접 행렬 값 업데이트
for _, row in df.iterrows():
    rent_station_id = row['대여 대여소번호']
    return_station_id = row['반납대여소번호']
    
    adj_matrix.loc[rent_station_id, return_station_id] += 1

print('Step2: 간이 인접행렬 생성 완료 !')

sorted_station_ids = np.sort(df['대여 대여소번호'].unique()).astype(str)
adj_df_sorted = pd.DataFrame(index=sorted_station_ids, columns=sorted_station_ids, dtype=int)

# adj_df의 일부 행과 열을 가져와서 새로운 데이터프레임에 복사
for row_station_id in sorted_station_ids:
    for col_station_id in sorted_station_ids:
        adj_df_sorted.loc[row_station_id, col_station_id] = adj_matrix.loc[row_station_id, col_station_id]

print('Step3: 진짜 인접행렬 생성 완료 !')
adj_df_sorted.to_csv('adj_df_sorted.csv')
print('Step4: 진짜 인접행렬 저장 완료 !')
