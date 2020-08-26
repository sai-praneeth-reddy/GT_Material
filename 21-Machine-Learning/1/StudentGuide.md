# Unit 21.1 - Introduction to Machine Learning

## Overview

Today's lesson plan introduces students to classical machine learning algorithms in the context of [sklearn](http://scikit-learn.org/stable/), covering data preprocessing and common machine learning algorithms.

## Class Objectives

* Students will understand how to calculate and apply regression analysis to datasets.

* Students will understand the difference between linear and non-linear data.

* Students will understand how to quantify and validate linear models.

* Students will understand how to apply scaling and normalization as part of the data preprocessing step in machine learning.

- - -

# Activities Preview

* **Stu_Univariate_Linear_Regression**
* In this activity, students calculate a regression line using a dataset of LSD drug concentrations vs. math scores.

  * Files/Instructions:
  
    * [Stu_LSD.ipynb](Activities/02-Stu_LSD/Unsolved/Stu_LSD.ipynb)
  
    * [README.md](Activities/02-Stu_LSD/README.md)

    * Start by creating a scatter plot of the data to visually see if any linear trend exists.

    * Next, use sklearn's linear regression model and fit the model to the data.

      * Print the weight coefficients and the y-axis intercept for the trained model.

    * Calculate the `y_min` and `y_max` values using `model.predict`

    * Plot the model fit line using `[x_min[0], x_max[0]], [y_min[0], y_max[0]]`

* **Brains!**
* In this activity, students calculate a regression line to predict head size vs. brain weight.

  * Files/Instructions:
  
    * [Stu_Brains.ipynb](Activities/04-Stu_Brains/Unsolved/Stu_Brains.ipynb)

    * [README.md](Activities/04-Stu_Brains/README.md)

    * Start by creating a scatter plot of the data to visually see if any linear trend exists.

    * Split the data into training and testing using sklearn's `train_test_split` function.

    * Next, use sklearn's linear regression model and fit the model to the training data.

    * Use the test data to make new predictions. Calculate the MSE and R2 score for those predictions.

    * Use `model.score` to calculate the the R2 score for the test data.

* **Beer Foam**
* In this activity, we are using 2 features for our X data, `foam` and `beer`. Using more than one feature (independent variable) is considered multiple regression.
  
  * File: [Stu_Beer_Foam.ipynb](Activities/06-Stu_Beer_Foam/Unsolved/Stu_Beer_Foam.ipynb)

* **Respiratory Disease**
* In this activity we'll use dataset with categorical values for the columns `sex` and `smoker`. We need to use the pandas `get_dummies` function to convert these to binary values.

  * File: [Stu_Respiratory_Disease.ipynb](Activities/08-Stu_Respiratory_Disease/Unsolved/Stu_Respiratory_Disease.ipynb)

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
