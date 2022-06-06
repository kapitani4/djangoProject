import pandas as pd
import aviadb

draw = aviadb.Drawing()

data_download = pd.read_excel('./T2.xlsx')

s = data_download.all()

print(s)