import pandas as pd
sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])
print(sr1)
print(sr2)
df=pd.DataFrame(sr1,sr2).reset_index()
print(df)
