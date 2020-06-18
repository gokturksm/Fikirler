import pandas as pd
import numpy as np

df = pd.read_clipboard()
column_names = ["Name", "Origin", "Date", "Open", "High", "Low", "Close", "Date+1", "Open+1", "High+1", "Low", "Close+1"]

def data_getter(data):
    intro = data.iloc[0][0:3]
    open_ = data.iloc[0].Open
    close = data.iloc[1].Close
    high = data.loc[:, 'High'].max()
    low = data.loc[:, 'Low'].min()
    frame = np.append(intro, [open_, high, low, close])
    return frame

def df_formatter(num: int):

    d = []

    for i in range(2):
        data = df.iloc[num*4+(i)*2:num*4+(i+1)*2]
        d.append(data_getter(data))
    
    d = np.append(d[0], [d[1][2:]])
    d = pd.Series(d)
    df.index = column_names
    return d

desired_df = pd.DataFrame(columns=column_names)

for i in range(int(df.shape[0]/4)):
    desired_df = desired_df.append(df_formatter(i), ignore_index=True)

print(desired_df)



# df2.iloc[:, [0,1,2,4,5,6,7]].groupby([0,1,2]).agg(Open=(4,'first'),High=(5,'max'),Low=(6,'min'), Close=(7,'last'))