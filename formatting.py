import pandas as pd
import matplotlib.pylab as plt
import numpy as np

filename = "C:/Users/SR/Desktop/DataFrame1.csv"
df_test = pd.read_csv(filename)

df_test[['Production_Start','Production_End']] = df_test['Production_Years'].str.split("-",expand=True,)

df_test.replace("", np.nan, inplace = True)

df_test.dropna(subset=["Production_Start"], axis=0, inplace=True)
df_test.dropna(subset=["Production_End"], axis=0, inplace=True)

df_test[["Production_Start"]] = df_test[["Production_Start"]].astype("float")
df_test[["Production_End"]] = df_test[["Production_End"]].astype("float")
df_test['Production_Period']=df_test['Production_End']-df_test['Production_Start']

avg_period=df_test['Production_Period'].astype('float').mean(axis=0)
avg_period=round(avg_period)

df = pd.read_csv(filename)

df[['Production_Start','Production_End']] = df['Production_Years'].str.split("-",expand=True,)

df.replace("", np.nan, inplace = True)
df.dropna(subset=["Production_Start"], axis=0, inplace=True)

df[["Production_Start"]] = df[["Production_Start"]].astype("float")
df[["Production_End"]] = df[["Production_End"]].astype("float")

df["Production_En"]=df["Production_Start"]+avg_period
df["Production_End"].replace(np.nan,df["Production_En"] , inplace=True)

df.drop(["Production_En"], axis=1, inplace=True)
df.drop(["Production_Years"], axis=1, inplace=True)

df['Production_Period']=df['Production_End']-df['Production_Start']

df[['Produced_Sold','aa','bb','cc','dd']] = df['Number Produced_Sold'].str.split(" ",expand=True)

df.drop(['aa','bb','cc','dd'], axis=1, inplace=True)
df.drop(['Number Produced_Sold'], axis=1, inplace=True)

df[['ee','ff']] = df['Top Speed_Text'].str.split("(",expand=True)

df[['kmh','gg']] = df['ff'].str.split("km",expand=True)
df[['mph','hh']] = df['ff'].str.split("mp",expand=True)

df.drop(['ee','ff','gg','hh'], axis=1, inplace=True)

df['kk']=df['kmh'].str.contains("m")
df['mm']=df['mph'].str.contains("m")

df['kk'].replace(True, np.nan, inplace = True)
df['mm'].replace(True, np.nan, inplace = True)

dfk=df.dropna(subset=["kk"], axis=0)
dfm=df.dropna(subset=["mm"], axis=0)

dfk[["kmh"]] = dfk[["kmh"]].astype("float")
dfm[["mph"]] = dfm[["mph"]].astype("float")

dfm['kmh'] = dfm["mph"]*1.609

df=pd.concat([dfk,dfm])

df.drop(['Top Speed_Text','mph','kk','mm'], axis=1, inplace=True)

df.to_csv('FinalData.csv')