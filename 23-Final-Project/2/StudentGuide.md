# Unit 23.2 - Final Projects

## Overview

In this class, students will lean how to use pre-trained convolutional neural networks (CNNs) for image classification. The remaining class will be used for project work.

## Class Objectives

* Students will be able to import a pre-trained CNN model.

* Students will be able to load an image from file into a data array.

* Students will be able to apply preprocessing to the input data.

* Students will be able to use the pre-trained model to make a prediction.

- - -

# Activities Preview

* **Explore CNN**
* For this activity students will use pre-trained CNN models.  The goal of this activity is to gain a high level understanding of CNN and their application.

* Files/Instructions:

  * [README.md](Activities/01-Par_Explore_CNNs/README.md)

  * Work with a partner to answer the following questions:

    1. What is a Convolutional Neural Network (CNN)?

    2. What is a CNN typically used for?

    3. What is the difference between a CNN and Deep Neural Network?

* **Xception**
* In this activity, students use the pre-trained `Xception` CNN model to predict image labels.

  * Files/Instructions:
  
    * [Xception.ipynb](Activities/03-Stu_Xception/Unsolved/Xception.ipynb)

    * [README.md](Activities/03-Stu_Xception/README.md)

    * Visit the [Xception](https://keras.io/api/applications/xception) documentation to determine the image_size and other parameters needed to load and use the model.

    * Pre-process the test image using the model's `preprocess_input` function.

    * Use the trained model to predict the output label for the puppy image.

    * Bonus:

      * Refactor the above steps into a reusable function that accepts an input image and returns a pre-processed image.

      * Test the code by preprocessing the image of a kitten and printing the predicted labels.

* **Project Work**
* Students will spend the rest of the class working on their projects.

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
