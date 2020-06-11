import pandas as pd
import dovpanda

df = pd.DataFrame([1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 2, 1, 7, 8])

df.cumsum().apply(lambda x: x // 15).drop_duplicates()


def deneme(a: pd.DataFrame = df) -> pd.DataFrame:
    return a


b = deneme(df)

print(b)


