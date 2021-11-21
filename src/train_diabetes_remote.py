# Code source: Jaques Grobler
# License: BSD 3 clause

import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


from azureml.core import Run

run = Run.get_context()

if __name__ == "__main__":
    # Load the diabetes dataset
    print('Cargando dataset')
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Use only one feature
    diabetes_X = diabetes_X[:, np.newaxis, 2]

    print('Separando en train y test')
    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    # Create linear regression object
    print('instanciando modelo')
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    print('Entrenando modelo')
    regr.fit(diabetes_X_train, diabetes_y_train)
    print('Entrenamiento finalizado')