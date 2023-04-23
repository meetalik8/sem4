import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

df=pd.DataFrame(d)
print(df)

print("\nValue of rows in col1 where value==4")
print(df.loc[df['col1']==4])

print("\nColumns for a specific row")
print(df.loc[4])

print("\nadding prefix to column")
print(df.add_prefix("00_"))

print("\nadding suffix")
print(df.add_suffix("_10"))
