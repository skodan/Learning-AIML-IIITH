# Datasets

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ages = np.array([3,4,5,6,7,8,9,10,11,12])
heights = np.array([30,33,35,38,40,46,48,50,55,56])

growth_rate = 0.0
starting_height = 30

learning_rate = 0.01
num_iterations = 1000

for i in range(num_iterations):
    # Calculate predictions and gradients
    prediction = starting_height + (growth_rate * ages)
    # Calculate errors and gradients
    errors = prediction - heights
    # Update parameters using gradient descent
    gradient_growth_rate = np.mean(errors * ages)*2
    gradient_starting_height = np.mean(errors)*2
    # # Update parameters
    growth_rate = growth_rate - (learning_rate * gradient_growth_rate)
    starting_height = starting_height - (learning_rate * gradient_starting_height)
    
    if i == num_iterations - 1:
        print(f"Iteration {i}: Growth Rate = {growth_rate}, Starting Height = {starting_height}")

age_to_predict = 10
predicted_height = starting_height + (growth_rate * age_to_predict)
print(f"Predicted height for age {age_to_predict} is {predicted_height} = {starting_height} + ({growth_rate} * {age_to_predict})")

# Plotting the results
plt.scatter(ages, heights, color='blue', label='Actual Heights')
plt.plot(ages, starting_height + (growth_rate * ages), color='red', label='Predicted Growth Line')
plt.xlabel('Age (years)')
plt.ylabel('Height (cm)')
plt.title('Height Prediction Based on Age')
plt.legend()
plt.show()