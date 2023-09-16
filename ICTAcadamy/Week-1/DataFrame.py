import pandas as pd

data={'a':[1,2],'b':[3,4],'c':[5,6]}

df=pd.DataFrame(data)

def float_value(x):
    return x*1.0

df=df.apply(float_value)

print(df)
