# Unit 21.3 - Neural Networks and Deep Learning!

## Overview

Today's lesson provides students with an introduction to neural nets and deep learning using Keras.

## Class Objectives

* Students will be able to articulate specific problems on which neural networks perform well.

* Students will be able to use Keras to build and train neural networks.

* Students will be able to use Keras to build and a train a deep neural network.

* Students will understand unsupervised learning and how to apply the k-means algorithm.

- - -

# Activities Preview

* **Moons**
* In this activity, students will create a regular Neural Network and a Deep Neural Network. Then, compare the accuracy of each.

  * Files/Instructions:

    * [04-Stu_Moons/Moons.ipynb](Activities/04-Stu_Moons/Unsolved/Moons.ipynb)

    * [04-Stu_Moons/README.md](Activities/04-Stu_Moons/README.md)

    * Create a Neural Network and Deep Neural Network Classifier that correctly classifies both moons from the dataset.

    * Train both models using 100 training epochs.

    * Compare the accuracy of both models.
    
    * Bonus: Try to find the minimal architecture (number of nodes) and minimum training iterations required to achieve a score of at least .90.

* **Deep Voice**
* In this activity, students apply a deep learning neural network to predict the gender of a voice using acoustic properties of the voice and speech.

  * Files/Instructions:

    * [05-Stu_Voice_Recognition.ipynb](Activities/05-Stu_Deep_Voice/Unsolved/Voice_Recognition.ipynb)

    * [05-Stu_Deep_Voice/voice.csv](Activities/05-Stu_Deep_Voice/Resources/voice.csv)

    * [05-Stu_Deep_Voice/voice.md](Activities/05-Stu_Deep_Voice/Resources/voice.md)

    * [05-Stu_Deep_Voice/README.md](Activities/05-Stu_Deep_Voice/README.md)

    * Create a deep learning model with 2 hidden layers.  Each layer should have 100 nodes.

    * Compile and fit the model.

    * Quantify (score) the model.

    * Use the first 5 testing data points to make predictions.  Then, compare the predictions to the actual labels.

* **Predicting Human Activity from Smartphone Accelerometer Data**
* In this activity we'll build model to determine whether someone is standing, sitting, walking, etc., based on accelerometer data collected from their smartphones. This is a **multi-class classification** problem, and neural nets often perform well on such problems.

  * Files/Instructions:

    * [07-Stu_Smartphone/Smartphone_Activity_Detector.ipynb](Activities/07-Stu_Smartphone/Unsolved/Smartphone_Activity_Detector.ipynb)

    * [07-Stu_Smartphone/X_train.txt](Activities/07-Stu_Smartphone/Resources/Train/X_train.txt)

    * [07-Stu_Smartphone/y_train.txt](Activities/07-Stu_Smartphone/Resources/Train/y_train.txt)

    * [07-Stu_Smartphone/X_test.txt](Activities/07-Stu_Smartphone/Resources/Test/X_test.txt)

    * [07-Stu_Smartphone/y_test.txt](Activities/07-Stu_Smartphone/Resources/Test/y_test.txt)

    * [07-Stu_Smartphone/README.txt](Activities/07-Stu_Smartphone/README.md)

    * Follow the comments in the provided starter file to:

      * Encode necessary labels.

      * Build and train a deep learning model.

      * Save the model.

      * Load to model.

      * Use the loaded model to predict the activity of a smartphone user based one data point from the test set.

* **K-means**
* In this activity, we'll explore K-means clustering algorithm

  * Files/Instructions:
  
    * [09-Stu_Kmeans/Kmeans.ipynb](Activities/09-Stu_Kmeans/Unsolved/Kmeans.ipynb)

    * [09-Stu_Kmeans/README.md](Activities/09-Stu_Kmeans/README.md)

    * Use the starter code to fit a Kmeans model to a dataset.

    * Visualize the results by creating a plot that looks like the following.

      ![Stu_Kmeans_plot](Images/Stu_Kmeans_plot.png)

    * Bonus: Look up how to get the centers of the k-means clusters and plot them!

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
