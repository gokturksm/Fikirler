import pandas as pd
import os
from os import listdir
from os.path import isfile, join

# get all files in the directory
# i used os.getcwd() to get the current directory
# if your text files are in another dir, then write exact dir location
# this gets you all files in your text dir
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]

# convert it to series
deneme = pd.Series(onlyfiles)

# an apply function to get just txt files
# others will be returned as None
def file_name_getter(x):
    names = x.split(".", maxsplit=1)
    if names[1] == "txt":
        return names[0]
    else:
        return None

# apply the function and get a new series with name values
mem_list = deneme.apply(lambda x: file_name_getter(x))

# now read first line of txt files
# and this is the function for it
def get_txt_data(x):
    if x != None:
        with open(f'{x}.txt') as f:
            return int(f.readline().rstrip())
    else:
        return 0

# apply the function, get a new series with memory values
mem_val_list = mem_list.apply(lambda x: get_txt_data(x))

# create a df where our Name and Memory data are present
# cast Memory data as int
df = pd.DataFrame(mem_val_list, columns=["Memory"], dtype="int")
df["Name"] = mem_list

# get rid of -memory now
def name_normalizer(x):
    if x is None:
        return x
    else:
        return x.rsplit("-", maxsplit=1)[0]

# apply function
df["Name"] = df["Name"].apply(lambda x:  name_normalizer(x))

# our sample orig_df
orig_df = pd.DataFrame([["algo_2", "10.10.10"], ["other", "20.20.20"]], columns=["Name", "PrivateIP"])

# merge using on, so if we miss data; that data wont cause any problem
# all matching names will get their memory values
final_df = orig_df.merge(df, on="Name")

final_df.add_suffix('_item')

pd.concat(final_df, orig_df)

deneme


