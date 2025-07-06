import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = 'D:\\Learnings\\AIML\\Learning-AIML-IIITH\\data\\'
df = pd.read_csv(path+'insurance.csv')
df.head()

plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-v0_8-whitegrid')

sns.lmplot(x='age', y='charges', data=df, height=6, aspect=1.5)
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.title('Scatter plot of BMI vs Charges')
plt.show()