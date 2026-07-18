import pandas as pd

print("USING PANDAS")
print(pd.__version__)
print(pd.__file__)

csvFile = "data/mycsv.csv"

df  = pd.read_csv(csvFile)
print(df)
print(df.head())

candidateExcel = "data/Count_Candidate.xlsx"

df = pd.read_excel(candidateExcel)
print(df)
print(df[['Date', 'Name']])

uniqueDf = df['Date'].unique()
print(uniqueDf)

#create series from list 
print("create series from list ")
data = [10,20,30,40,50]
s = pd.Series(data)
print(s)
print(s[2])

#casting dictionary to dataframe
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)
print(df)
print(type(x))
print(type(df))
print('df2')
df2 = df
df2 = df2.set_index('Name')
print(df2.loc['Rose':'Jane', 'ID':'Department'])

a = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}
df1 = pd.DataFrame(a)
print(df1)
print(df1.loc[0,'Student'])
print(df1.loc[2,'Course'])


print(df1.iloc[0:2,0:3])
