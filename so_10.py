import csv
import numpy as np
import pandas as pd


def tabbed_to_df(file_name: str) -> pd.DataFrame:
    reader_output = []
    with open(file_name, newline='') as csvfile:
        f_reader = csv.reader(csvfile, delimiter='\t')
        for row in f_reader:
            reader_output.append(row)
    df = pd.DataFrame(data=reader_output,
                      columns=['Date', 'Price', 'Change', 'Change Percent', 'Change Cumulative Percent'],
                      dtype='float')
    df.set_index(['Date'], inplace=True)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
    return df


file_names = ['GAU', 'IPP']
file_paths = [f"{f}.txt" for f in file_names]
isbank_data = [tabbed_to_df(f) for f in file_paths]

all_data = pd.concat(isbank_data, keys=file_names)
all_data.drop(columns=['Change', 'Change Percent', 'Change Cumulative Percent'], inplace=True)

all_data = all_data.unstack(level=0).dropna().droplevel(0, axis=1)

all_data.loc[:, 'GAU']

