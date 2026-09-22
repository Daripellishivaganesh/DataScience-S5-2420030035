import pandas as pd

data = {'col1': [3, 2, 0, 1], 'col2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)
print(df)