'''
Date: 2022.10.11
Title: 
By: Kang Jin Seong
'''
# import pandas as pd
# file_path = 'C:/Users/USER/Desktop/DSP_python/Pandas/part5/auto-mpg.csv'
# # print(file_path)
# df = pd.read_csv(file_path, header= None)
# # print(df)
# # 열이름 지정
# df.columns = ['mpg','cylinders', 'displacement', 'horespower', 'weight',
#  'acceleration', 'model year', 'origin', 'name']
# print(df.head(3));print('\n')

# # mpg(mile per gallon)를 kpl(kilometer per liter)로 변환(mpg to kpl = 0.425)
# mpg_to_kpl = 1.60934/3.78541

# #mpg 열에 0.425를 곱한 결과를 새로운 열(kpl)에 추가
# df['kpl'] = df['mpg'] * mpg_to_kpl
# # print(df.head(3));print('\n')

# df['kpl'] = df['kpl'].round(2)
# # print(df.head(3));print('\n')

'''자료형 변환'''
# import pandas as pd
# file_path = 'C:/Users/USER/Desktop/DSP_python/Pandas/part5/auto-mpg.csv'
# df = pd.read_csv(file_path, header= None)
# # 열이름 지정
# df.columns = ['mpg','cylinders', 'displacement', 'horsepower', 'weight',
#  'acceleration', 'model year', 'origin', 'name']

# print(df.info())
# print(df['horsepower'].unique());print('\n')

# # 누락 데이터'?' 삭제
# import numpy as np
# df['horsepower'].replace('?', np.nan, inplace = True)
# df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
# df['horsepower'] = df['horsepower'].astype('float')

# # print(df['horsepower'].dtypes)

# # origin 열의 고유값 확인
# print(df['origin'].unique())
# df['origin'].replace({1: 'USA', 2:'EU', 3:'JPN'}, inplace = True)

# print(df['origin'].unique())
# print(df['origin'].dtypes)

'''범주형(category) 데이터 처리'''

# import pandas as pd
# import numpy as np
# file_path = 'C:/Users/USER/Desktop/DSP_python/Pandas/part5/auto-mpg.csv'
# df = pd.read_csv(file_path, header= None)
# # 열이름 지정
# df.columns = ['mpg','cylinders', 'displacement', 'horsepower', 'weight',
#  'acceleration', 'model year', 'origin', 'name']

# df['horsepower'].replace('?', np.nan, inplace = True)
# df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
# df['horsepower'] = df['horsepower'].astype('float')

# # np.histogram 함수로 3개의 bin으로 구분할 경계값의 리스트 구하기
# count, bin_dividers = np.histogram(df['horsepower'], bins = 3)
# # print(bin_dividers)
# bin_names = ['저출력', '보통출력', '고출력']

# df['hp_bin'] = pd.cut(x = df['horsepower'],
# bins = bin_dividers,
# labels = bin_names,
# include_lowest=True)

# # print(df[['horsepower', 'hp_bin']].head(15))

# '''더미 변수'''
# horsepower_dummies = pd.get_dummies(df['hp_bin'])
# print(horsepower_dummies.head(15))

'''시계열 데이터'''
import pandas as pd

df = pd.read_csv('C:/Users/USER/Desktop/DSP_python/Pandas/part5/stock-data.csv')
# print(df.head())
# print('\n')
# print(df.info())

# 문자열을 타임스테프로 변환
df['new_Date'] = pd.to_datetime(df['Date'])
# print(df.head());print('\n')
# print(df.info());print('\n')
# print(type(df['new_Date'][0]))

# 시게열 값으로 변환된 열을 새로운 행 인덱스로 지정
df.set_index('new_Date', inplace= True)
df.drop('Date', axis = 1, inplace = True)

# print(df.head());print('\n')
# print(df.info())

