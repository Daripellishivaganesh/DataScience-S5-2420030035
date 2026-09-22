#drop rows with misssing values
import pandas as pd
import numpy as np
df = pd.DataFrame({ 'Age': [25, 30, np.nan, 40, 35],'Department': ['HR', 'IT', 'Finance', np.nan, 'IT']})
#diplay original dataset
print("original Dataset")
print(df)
#drop colums with missing values
df_drop_cols = df.dropna(axis=1)
print("After dropping columns:\n", df_drop_cols)