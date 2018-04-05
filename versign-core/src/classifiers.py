from sklearn import svm, preprocessing, decomposition
import scipy.io
import numpy as np, os

def OneClassSVM(x_train, x_test):
    # Fit SVM model
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=2**-11)
    clf.fit(x_train)

    # Calculate model error
    Y_train = clf.predict(x_train)
    n_error_train = Y_train[Y_train == -1].size

    # Predict results
    Y_test = clf.predict(x_test)

    return Y_test, Y_train, n_error_train

def OneClassSVMWithPCA(x_train, x_test):
    # Dimensionality reduction
    x_train = np.array(x_train)
    x_test = np.array(x_test)
    print x_train.shape
    print x_test.shape
    
    x_train = decomposition.PCA(n_components=25).fit_transform(x_train)
    x_test = decomposition.PCA(n_components=25).fit_transform(x_test)

    print x_train.shape
    print x_test.shape

    # Fit SVM model
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=2**-11)
    clf.fit(x_train)

    # Calculate model error
    Y_train = clf.predict(x_train)
    n_error_train = Y_train[Y_train == -1].size

    # Predict results
    Y_test = clf.predict(x_test)

    return Y_test, Y_train, n_error_train