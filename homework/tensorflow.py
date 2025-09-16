import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4, 5], dtype=float)
y_data = np.array([3, 5, 7, 9, 11], dtype=float)

#  linear Model: y = m*x + c
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x_data, y_data, epochs=500, verbose=0)


x_test = np.array([6, 7, 8], dtype=float)
y_pred = model.predict(x_test)

print("Predictions for x =", x_test, "are", y_pred.flatten())

# Plot
plt.scatter(x_data, y_data, label="Training data")
plt.plot(x_test, y_pred, label="Model predictions")
plt.legend(); plt.xlabel("x"); plt.ylabel("y"); plt.title("Linear Model")
plt.show()
