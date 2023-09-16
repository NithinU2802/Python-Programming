import pandas as pd

df1 = pd.DataFrame([['a', 1, 2], ['b', 2, 3], ['c', 4, 5]], columns=['A', 'B', 'C'])
df2 = pd.DataFrame([['a', 6, 7], ['a', 8, 9]], columns=['A', 'D', 'E'])


merged_df = df1.merge(df2, on='A', how='left')

print(merged_df)
