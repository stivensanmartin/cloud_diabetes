import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle

if __name__ == "__main__":
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    #Train and test data
    diabetes_X_train,diabetes_X_test,diabetes_y_train,diabetes_y_test=train_test_split(diabetes_X,diabetes_y,test_size=.3)

    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)

    print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))

    #Registro
    with open('./outputs/diabetes_model.pkl', 'wb') as model_pkl:
        pickle.dump(regr, model_pkl)