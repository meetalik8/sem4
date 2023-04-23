import pandas as pd
import numpy as np
exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew','Laura','Kevin','Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df=pd.DataFrame(exam_data, index=labels)
#print(df)
print("\n3 ROWS")
print(df[:3])

print("\nGreater than 2 attempts")
print(df[df['attempts']>2])

print("\nScore between 15 and 20 included")
print(df[df['score'].between(15,20)])

print("\nMean of scores")
print(df['score'].mean())

print("\nAppend new row")
df.loc['k']=['Suresh',15.5,1,'yes']
print(df)

print("\nDelete new row")
df=df.drop('k')

print("\nInsert new column")
color=['red','blue','green','white','black','cyan','magenta','yellow','purple','orange']
df['color']=color
print(df)

print("\nDeleting th column")
del df['color']
print(df)

print("\nset a value for a cell using index")
df._set_value('i','score',10)
print(df)

