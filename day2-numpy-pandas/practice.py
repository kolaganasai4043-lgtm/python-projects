import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", arr.mean())

data = {"Name": ["A", "B", "C"], "Score": [85, 90, 95]}
df = pd.DataFrame(data)
print(df)
