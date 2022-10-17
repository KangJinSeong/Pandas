'''
Date: 2022.10.11
Title: 
By: Kang Jin Seong
'''
#%%
import seaborn as sns

# titanic 데이터셋 가져오기
# file_path = 'C:/Users/USER/Desktop/DSP_python/Pandas/part5'
# file_name = file_path +'/'+ 'titanic'
# df = sns.load_dataset('titanic')

# print(df.head())
# # %%
# print(df.info())
# # %%
# # 누락 데이터 확인
# # deck 열의 NaN 개수 계산하기
# nan_deck = df['deck'].value_counts(dropna = False)
# print(nan_deck)

# print(df.head().isnull())   #  누락데이터면 True
# print(df.head().notnull())  # 누락 데이터면 False
# # %%
# # isnull() 메소드로 누락 데이터 개수 구하기
# print(df.head().isnull().sum(axis = 0))
# %%
# 누락 데이터 제거하기

df = sns.load_dataset('titanic')

# for 반복문으로 각 열의 NaN 개수 계산하기
# missing_df = df.isnull()

# for col in missing_df.columns:
#     missing_count = missing_df[col].value_counts()  # 각 열의 Nan 개수 파악

#     try:
#         print(col, ':', missing_count[True])    # NaN 값이 있으면 개수 출력
#     except:
#         print(col, ':', 0)
    
# %%
# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
# df_thresh = df.dropna(axis = 1, thresh = 500)
# print(df_thresh.columns)
# # %%
# # age 열에 나이데이터가 없는 모든 행 삭제
# df_age = df.dropna(subset = ['age'], how = 'any', axis = 0)
# print(len(df_age))
# %%
'''
Date: 2022.10.17
Title: 
By: Kang Jin Seong
'''
# 평균으로 누락 데이터 바꾸기
# age 열의 첫 10개 데이터 출력(5행에 NaN 값)
# print(df['age'].head(10))
# print('\n')

# # age 열의 NaN 값을 다른 나이 데이터의 평균으로 변경하기
# mean_age = df['age'].mean(axis = 0) # age열의 평균계산(NaN 값 제외)
# df['age'].fillna(mean_age, inplace = True)
# print(df['age'].head(10))
# %%
# embark_town 열의 829행의 NaN 데이터 출력
# print(df['embark_town'][825:830])
# print('\n')

# # embark_town 열의 NaN 값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
# most_freq = df['embark_town'].value_counts(dropna = True).idxmax()
# print(most_freq)
# print('\n')

# df['embark_town'].fillna(most_freq, inplace = True)
# print(df['embark_town'][825:830])
# %%
# 이웃하고 있는 값으로 바꾸기
df = sns.load_dataset('titanic')
print(df['embark_town'][825:830])
print('\n')
# embark_town 열의 NaN 값을 바로 앞에 있는 828행의 값으로 변경하기
df['embark_town'].fillna(method = 'ffill', inplace = True)
print(df['embark_town'][825:830])
# %%
'''중복 데이터 처리'''
import pandas as pd

df = pd.DataFrame({'c1': ['a', 'a', 'b', 'a', 'b'],
                    'c2': [1,1,1,2,2],
                    'c3': [1,1,2,2,2]})
print(df);print('\n')

# 데이터프레임에서 행 데이터 중에서 중복값 찾기
df_dup = df.duplicated()
# print(df_dup);print('\n')
# %%
# 특정 열 데이터에서 중복값 찾기
col_dup  = df['c2'].duplicated()
print(col_dup)
# %%
# 중복 데이터 제거
df2 = df.drop_duplicates()
print(df2); print('\n')
# %%
# c2, c3열을 기준으로 중복 행 찾기
df3 = df.drop_duplicates(subset = ['c2', 'c3'])
print(df3)
# %%
