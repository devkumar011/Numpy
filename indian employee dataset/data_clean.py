#import necessary libraries
import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv('indian employee dataset\employees.csv')
print(df.head())

#cheking the missing values 
print('Missing values in each column')
print(df.isnull().sum())

df['Salary (INR'].fillna(df['Salary(INR)'].mean(),inplace=True)

df['Performance Rating'].fillna(df['Performance Rating'].median(),inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(),inplace=True)
#remove duplicates replace 
df.drop_duplicates(inplace=True)

#replace negative salaries

df['Salary (INR)'] = np.where(df['Salary (INR)'] <0, df['Salary(INR)'].mean(), df['salary'])

salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
super_bound = salarr_mean + (3 * salary_std)

#remove rows wher salary is too high or too low

df = df[(df['Salary(INR)'] >= lower_bound) & (df['Salary (INR)'] <= uper_bound)]

df.to_csv('indian employee dataset\employees.csv', index=False)
print('')