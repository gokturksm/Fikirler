import pandas as pd

df1 = pd.DataFrame([[1,2,3], [1,2,3]])
df2 = pd.DataFrame([[3,4,5], [3,4,5]])
df_list = (df1, df2)

temp = pd.DataFrame([])
for i, df in enumerate(df_list):
    temp = temp.append(df.iloc[-1], ignore_index=True)

