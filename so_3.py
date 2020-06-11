import pandas as pd

df = pd.DataFrame(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    columns=list("ABCDEFGHIJKLM"),
)

df.index = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def case_finder(df):
    df_case = df.apply(lambda x: x.value_counts(), axis=1).fillna(0)
    df_case = df_case.loc[df_case[1] != 0]
    return df_case.sort_values(by=1)


df_case = case_finder(df)

def get_loc(ind):
    return df.iloc[ind].loc[df.iloc[ind] == 1]

