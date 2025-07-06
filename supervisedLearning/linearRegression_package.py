import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ages = np.array([3,4,5,6,7,8,9,10,11,12])
# heights = np.array([30,33,35,38,40,46,48,50,55,56])

# from sklearn.linear_model import LinearRegression
# ages_reshaped = ages.reshape(-1, 1)
# model = LinearRegression().fit(ages_reshaped, heights)
# pred = model.predict(ages_reshaped)
# print(f" Predicted heights: {pred}")

# # Predicting height for a specific age
# age_to_predict = 11
# predicted_height = model.predict(np.array([[age_to_predict]]))
# print(f"Predicted height for age {age_to_predict} is {predicted_height[0]}")

# # plotting the results
# plt.scatter(ages, heights, color='blue', label='Actual Heights')
# plt.plot(ages, pred, color='red', label='Predicted Growth Line')
# plt.xlabel('Age (years)')
# plt.ylabel('Height (cm)')
# plt.title('Height Prediction Based on Age')
# plt.legend()
# plt.show()

path = 'D:\\Learnings\\AIML\\Learning-AIML-IIITH\\data\\'
df = pd.read_csv(path + 'insurance.csv')
print(df.head())

df.shape()