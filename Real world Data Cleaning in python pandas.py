#%% 
# Import Pandas
import pandas as pd
#%%
#Import CSV
df = pd.read_csv('CricketData.csv')
#%%
#Rename Multiple Coloums
df= df.rename(columns={'NO':'NotOuts', 'Inns':'Innings', 'Mat':'Matches', 'HS':'HighScore', 'Ave':'Average', 'SR':'ScoreRate'})
#%%
#Check the Null Values
df.isnull().any()
df[df['BF'].isna()==1]
#%%
#Drop Duplicate
df[df['Player'].duplicated()==1]# Check if there any duplicates
df=df.drop_duplicates()# Drop the duplicates
#%%
#Split the Span intoi two diffrent coloumns 
df['StartYear'] = df['Span'].str.split(pat ='-').str[0]#Split 1
df['EndYear'] = df['Span'].str.split(pat ='-').str[1]# Split 2nd
df = df.drop(columns=['Span'])# Drop Column
#%%
# Split the Country name from Player name
df['Country'] = df['Player'].str.split(pat ='(').str[1]#Split the Column
df['Player'] = df['Player'].str.split(pat ='(').str[0]#update the Player Column
#%%
df['Country'] = df['Country'].str.split(pat =')').str[0]#update the Countery coloumn
#%%
# Remone '*' From HighScore Column
df['HighScore'] = df['HighScore'].str.split(pat ='*').str[0]
#%%
#Remove + from BF
df['BF'] = df['BF'].str.split(pat ='+').str[0]
#%%
#Remove + from 4s, 6s
df['4s'] = df['4s'].str.split(pat ='+').str[0]
df['6s'] = df['6s'].str.split(pat ='+').str[0]
#%%
#In Bf Drop "-" Entries or Rows
df= df.drop(7, axis=0)
#%%
df= df.drop(13, axis=0)
df= df.drop(53, axis=0)
#%%
# Fix the Data Types
df = df.astype({'StartYear':'int', 'EndYear':'int', 'HighScore':'int', 'BF':'int', '4s':'int', '6s':'int'})
#%%
df.dtypes
#%%
#Career Length
df['CareerLength'] = df['EndYear']-df['StartYear']
#%%
#Average Career Length
df['CareerLength'].mean()
#%%
#Average Batting Strike Rate for crickter played more than 10 years
df[df['CareerLength']>10]['ScoreRate'].mean()
#%%
# Number of Crickter Played before 1960
df[df['StartYear']<1960]['Player'].count()
#%%
#output as csv
df.to_csv('output.csv', index=False)
#%%
