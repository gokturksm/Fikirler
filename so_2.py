# coding in UTF-8
# File Name     : so_2.py
# Author        : Göktürk Şahin
# E-mail        : gokturksm[at]gmail[dot]com
# Date          : dd-05-2020
# Description   : This file contains coding work for a Stackoverflow question.
#                 The problem here is the dataframe has missing variable in
#                 certain columns. So it's trying to fill those values by
#                 a rule which is getting the mean value of the last 3 values.

#   === Changelogs ===
#   --> dd-05-2020
#   1. created the file
#   

import pandas as pd

df = pd.DataFrame(
    [
        [17, 19, 49],
        [4, 9, 2],
        [2, 23, 3],
        [8, 23, 7],
        [6, 21, 24],
        [5, "", ""],
        [5, "", ""],
        [5, "", ""],
        [5, "", ""],
        [5, "", ""],
        [5, "", ""],
        [5, "", ""],
    ],
    columns=list("ABC"),
)

df.index = pd.date_range(start="12-31-2019", end="01-11-2020", freq="D")


def forecast(df):
    """
    Calculates last 3 days mean value.

    ``Parameters``
        df (Dataframe): Input dataframe where timestamped data is available.

    ``Returns``
        Series: 1-sized calculated series data with a new timestamp.
    """
    last_day = df.iloc[-1]
    new_day = last_day.name + pd.Timedelta(days=1)
    new_data = df.loc[last_day.name - pd.Timedelta(days=3) : last_day.name, :].mean()
    new_data.name = new_day
    return new_data


num_predict_days = 7
columns_to_predict = ["B", "C"]

available_data = df.shape[0] - num_predict_days
df_to_predict = df.iloc[:available_data, :].loc[:, columns_to_predict]

for i in range(num_predict_days):
    df_to_predict = df_to_predict.append(forecast(df_to_predict))

df.update(df_to_predict)
