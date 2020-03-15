# CS344 Exercise 6.3
# @author: Ian Park

from keras.datasets import boston_housing

(train_examples, train_labels), (test_examples, test_labels) = boston_housing.load_data()

print("Number of training examples ", len(train_examples))
print("Number of testing examples ", len(test_examples))

print("\tRank: ", test_labels.ndim)
print("\tShape: ", test_labels.shape)
print("\tData Type: ", test_labels.dtype)
