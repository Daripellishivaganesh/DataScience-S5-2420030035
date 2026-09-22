import pandas as pd
import numpy as np
# sample dataset
df = pd.DataFrame({ 'Age': [25, 30, np.nan, 40, 35],'Department': ['HR', 'IT', 'Finance', np.nan, 'IT']})
print(df)
#mean for numeric
df['Age']=df['Age'].fillna(df['Age'].mean())
#mode for categorical
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)