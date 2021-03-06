# Exercise 6.3

import numpy as np
from keras.datasets import boston_housing
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()


# a. i.
print("i.")
print("Number of training examples: ", len(x_train))
print("Number of testing examples:  ", len(x_test))

# a. ii.
print("\nii.")
print("Training")
print(" Rank: ", x_train.ndim)
print(" Shape: ", x_train.shape)
print(" Data type: ", x_train.dtype)
print("Testing")
print(" Rank: ", x_test.ndim)
print(" Shape: ", x_test.shape)
print(" Data type: ", x_test.dtype)

# Note about the training and testing shape: I noticed that the lab example used the targets for the size and shape. I used the x data for the sake of consistent comparison. 
# There are the same number of examples and datatype measured either way. The shape is different.
