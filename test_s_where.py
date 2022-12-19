import pandas as pd

# Créez une série Pandas
s = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])

s_filtered = s.loc[s >= 90]
print(s_filtered)