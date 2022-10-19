'''
Date: 2022.10.18
Title: 
By: Kang Jin Seong
'''

'''함수 맵핑'''
# # 시리즈의 원소에 apply()적용
# import seaborn as sns

# titanic = sns.load_dataset('titanic')
# df = titanic.loc[:, ['age', 'fare']]
# df['ten'] = 10
# print(df.head())

# # 사용자 함수 정의
# def add_10(n):
#     return n + 10

# def add_two_obj(a,b):
#     return a + b

# # 시리즈 객체에 적용
# sr1 = df['age'].apply(add_10)
# # print(sr1.head())

# # 시리즈 객체와 숫자에 적용: 2개의 인수(시리즈 + 숫자)
# sr2 = df['age'].apply(add_two_obj, b = 10)
# # print(sr2.head())

# # lambda 함수 활용 : 시리즈 객체에 적용
# sr3 = df['age'].apply(lambda x: add_10(x))
# # print(sr3.head())


'''열 재구성'''
# import seaborn as sns
# titanic = sns.load_dataset('titanic')
# df = titanic.loc[0:4, 'survived':'age']
# print(df, '\n')

# # 열 이름의 리스트 만들기
# columns = list(df.columns.values)
# print(columns, '\n')

# columns_sorted = sorted(columns)
# df_sorted = df[columns_sorted]
# print(df_sorted, '\n')

# '''열 분리'''
# import pandas as pd
# df = pd.read_excel('C:/Users/USER/Desktop/DSP_python/Pandas/part6/주가데이터.xlsx', engine = 'openpyxl')
# # print(df.head(), '\n')
# # print(df.dtypes, '\n')

# # 연,월,일 데이터 분리하기
# df['연월일'] = df['연월일'].astype('str')
# dates = df['연월일'].str.split('-')
# print(dates.head(), '\n')

'''필터링'''
# import seaborn as sns
# import pandas as pd

# titanic = sns.load_dataset('titanic')
# #IPyhton 디스플레이 설정 변경 - 출력할 최대 열의 개수
# pd.set_option('display.max_columns', 10)

# mask3 = titanic['sibsp'] == 3
# mask4 = titanic['sibsp'] == 4
# mask5 = titanic['sibsp'] == 5

# df_boolean = titanic[mask3 | mask4 | mask5]
# # print(df_boolean.head())

# isin_filter = titanic['sibsp'].isin([3,4,5])
# print(titanic[isin_filter].head())

'''그룹연산'''
# # 분할
# import pandas as pd
# import seaborn as sns

# titanic = sns.load_dataset('titanic')
# df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
# print('승객 수:', len(df))
# print(df.head());print('\n')

# # class 열을 기준으로 분할
# grouped = df.groupby(['class'])
# # print(grouped)

# # 그룹 객체를 iteration으로 출력
# # for key, group in grouped:
# #     print('* key :', key)
# #     print('* number :', len(group))
# #     print(group.head());print('\n')

# # 연산 메소드 적용
# average = grouped.mean()
# # print(average)

# # 특정 그룹 선택 가능
# group3 = grouped.get_group('Third')
# # print(group3.head())



'''그룹 연산 메소드(적용-결합 단계)'''
# 데이터 집계
import pandas as pd
import seaborn as sns

titanic  = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
# print(std_all);print('\n')

# 각 그룹에 대한 fare 열의 표준편타를 집계하여 시리즈로 반환
std_fare = grouped.fare.std()
# print(std_fare)

def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped.agg(min_max)
# print(agg_minmax)

# 여러 함수를 각 열에 동일하게 적용하여 집계
agg_all = grouped.agg(['min', 'max'])
# print(agg_all.head())

agg_sep = grouped.agg({'fare':['min', 'max'], 'age':'mean'})
# print(agg_sep.head())

# apply 함수 적용 , 필터링
age_filter  = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter);print('\n')

for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head());print('\n')

    