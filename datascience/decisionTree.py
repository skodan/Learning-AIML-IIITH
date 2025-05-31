import pandas as pd
df = pd.read_csv('data/dt_31May.csv')
print(df.head())

# Manual computation of entropy
from math import log2
man_en = -((5/14)*log2(5/14) + (9/14)*log2(9/14))
print("Entropy computed manually: ",man_en)

from scipy.stats import entropy
play_entropy = entropy([5/14, 9/14], base=2)
print("Entropy computed via scipy-entropy: ",play_entropy)
