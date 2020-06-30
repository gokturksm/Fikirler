import pandas as pd

veri: pd.DataFrame = pd.read_excel("TarihselVeriler.xlsx", sheet_name="Genel Bilgiler", engine="xlrd")

para_piyasası = veri.loc[veri['FON ADI'].str.contains('PARA PİYASASI', regex=True)]

df = pd.DataFrame([0, 1, 2, 3])


