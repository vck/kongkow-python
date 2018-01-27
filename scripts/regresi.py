from sklearn.linear_model import LinearRegression 
import numpy as np
import matplotlib.pyplot as plt 

# training data
x = np.array([[200], [250], [300], [378], [456], [680], [750]])
y = np.array([[2000], [3500], [5000], [5400], [6500], [8700], [9500]])


clf = LinearRegression()

# train model
clf.fit(x, y)

# make prediction with the model
predicted_y = clf.predict(x)

# assign m param to coef
coef = clf.get_params()

print(coef)
print(predicted_y)

# plot data
plt.scatter(x, y, label='data')

# plot predicted values
plt.plot(x, predicted_y, label='predicted values')
plt.legend()
plt.show()


