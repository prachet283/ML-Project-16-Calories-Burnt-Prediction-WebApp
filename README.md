# Calories Burnt Prediction Web App
This repository contains the code and resources for a Machine Learning project aimed at predicting the number of calories burnt during physical activities. The web application uses various features such as gender, age, height, weight, duration, heartrate, and body temperature to make the predictions.

# Overview
The purpose of this project is to create a web application that can predict the number of calories burnt based on user inputs. The prediction model is built using machine learning techniques and deployed on a user-friendly web interface.

# Dataset
The dataset used for training the model consists of records of physical activities with the following features:

Gender
Age
Height (in cm)
Weight (in kg)
Duration (in minutes)
Heartrate (in bpm)
Body Temperature (in °C)
The dataset is preprocessed to handle missing values, normalize numerical features, and encode categorical variables.

# Technologies
Python: Programming language Streamlit: Framework for building the web app Scikit-learn: Machine learning library Pandas: Data manipulation library NumPy: Numerical computing library Matplotlib/Seaborn: Data visualization libraries

# Exploratory Data Analysis (EDA)
DA is performed to understand the underlying patterns and relationships in the data. The key steps in the EDA process include:

Descriptive Statistics: Summarizing the main features of the dataset.
Data Visualization: Creating plots to visualize distributions, correlations, and outliers.
Feature Analysis: Analyzing the impact of each feature on the target variable (calories burnt).
Key insights from the EDA are documented to guide the feature engineering and model selection process.

# Model
The machine learning model is built using the following steps:

Data Preprocessing: Handling missing values, normalization, and encoding.
Model Selection: XGBoost
Model Training: Training the selected model on the preprocessed dataset.
Model Evaluation: Evaluating the model using metrics like Mean Absolute Error (MAE) and R-squared.

# Web Application
The web application is built using Streamlit, which provides an interactive interface for users to input their data and get predictions on the calories burnt.

# Usage
Open your browser and go to https://ml-project-16-calories-burnt-prediction-webapp-itkkhxtleghdojs.streamlit.app/
Fill in the input fields with the necessary information (gender, age, height, weight, duration, heartrate, and body temperature).
Click on the "Predict Calorie Burnt" button to get the predicted number of calories burnt.

# Results
The model's performance is evaluated using the test dataset. The following metrics are reported:

Mean Absolute Error (MAE): 1.48
R-squared: 0.99

# Conclusion
This project demonstrates the application of machine learning techniques to predict the number of calories burnt during physical activities based on various input features. The web application provides a user-friendly interface for making predictions, making it accessible to a wide range of users. Future work could involve improving the model by incorporating more advanced features, experimenting with different machine learning algorithms, and increasing the dataset size for better accuracy.

# Contributing
Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

# Deployment
The application is deployed using Streamlit. You can access it here = https://ml-project-16-calories-burnt-prediction-webapp-itkkhxtleghdojs.streamlit.app/
