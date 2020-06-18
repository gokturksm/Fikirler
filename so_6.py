import pandas as pd

df = pd.read_clipboard()

# all your new data is here
df2 = df.groupby(["Date", "Name", "Origin"]).agg(
    {"Open": ["min"], "High": ["max"], "Low": ["min"], "Close": ["max"]}
)

df2 = df2.droplevel(1, axis=1).reset_index()

column_names = ["Name", "Origin", "Date", "Open", "High", "Low", "Close", "Date+1", "Open+1", "High+1", "Low", "Close+1"]
desired_df = pd.DataFrame(columns=column_names)

df3 = pd.concat([df2, df2.add_suffix('+1').shift(-1)], axis=1)

df4 = df3.iloc[::2]

df4 = df4.drop(columns=['Date+1', 'Name+1', 'Origin+1']).reset_index(drop=True)
