import pandas as pd
import numpy as np
# sample dataset
df = pd.DataFrame({ 'Age': [25, 30, np.nan, 40, 35],'Department': ['HR', 'IT', 'Finance', np.nan, 'IT']})
#display original datasset
print("Original Dataset (with Missing Values):")
print(df)
df_bfill = df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)

