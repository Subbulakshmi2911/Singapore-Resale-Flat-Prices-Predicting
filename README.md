# Singapore-Resale-Flat-Prices-Predicting
singapore  Resale Flat Prices Predicting

Introduction

This project aims to construct a machine learning model and implement it as a user-friendly online application to predict resale prices for apartments in Singapore. The prediction model is based on historical data of resale flats, taking various factors into account, such as the location, flat type, square footage, and lease duration. The model's goal is to provide potential buyers and sellers with an estimate of the resale price of a flat after it has been resold, thus making the real estate decision-making process more informed and efficient.
Domain

    Real Estate: The focus of this project is on predicting the resale value of flats in Singapore, a critical factor for buyers, sellers, and real estate investors in making decisions regarding property transactions.

Project Overview

The resale price of apartments can be influenced by several factors such as location, type of apartment, floor area, and lease duration. By using a dataset of previous flat transactions, we can build a predictive model to estimate the resale price based on these features.
Prerequisites

    Python – Programming Language for implementing the model and application.
    Pandas – Python library for data manipulation and analysis.
    NumPy – Fundamental Python package for scientific computing.
    Streamlit – Framework for building interactive, user-friendly web apps for data science and machine learning.
    Scikit-learn – Python library for machine learning, used for building and evaluating the prediction model.

Data Source

The data used in this project is sourced from the Singapore government’s open data portal:

    Link: Singapore Resale Flat Prices Dataset

This dataset consists of five distinct CSV files, each covering a specific time period:

    1990 - 1999
    2000 - 2012
    2012 - 2014
    2015 - 2016
    2017 onwards

Each file contains transaction details such as flat type, location, and resale price for the specified time period. The goal is to merge these five files into a unified dataset for analysis.
Project Workflow
1. Data Collection and Merging

    The first step is to merge the five CSV files into one unified dataset. The data spans multiple time periods, so merging them ensures a comprehensive dataset that covers all relevant years.

2. Data Preprocessing

    Cleaning: Any missing or erroneous data is addressed. This includes handling missing values, outliers, and ensuring that data types are appropriate for analysis.

    Feature Engineering: We extract relevant features such as:
        town: The location of the flat.
        flat_type: Type of the flat (e.g., 3-room, 4-room).
        storey_range: Range of floors the flat is located on (e.g., 1-3 floors, 4-6 floors).
        floor_area: The size of the flat in square feet.
        flat_model: The model of the flat (e.g., Standard, Improved).
        lease_commence_date: The start date of the flat's lease.

3. Model Building

    Decision Tree Regressor: We use a Decision Tree Regressor to predict the resale price of the flats. This algorithm is well-suited for this type of problem as it can capture non-linear relationships between the features and the target variable (resale_price).
        Hyperparameter Tuning: The performance of the decision tree can be improved by tuning parameters such as max_depth, min_samples_split, and min_samples_leaf.

4. Model Evaluation

    The model's performance is evaluated using standard regression metrics such as:
        Mean Squared Error (MSE)
        Root Mean Squared Error (RMSE)
        R² (R-squared)

5. Building the Streamlit Application

    A Streamlit web application is developed where users can input the relevant values for each feature and get the predicted resale price for a flat. The application will be interactive and provide an easy-to-use interface for users to predict flat prices based on their inputs.

Key Features of the Model

    Location-based Predictions: Since the location of the flat plays a significant role in its resale price, the model will take the town feature into account.
    Flat Characteristics: The model uses the type, size, and model of the flat as key features for predicting the resale price.
    Interactive Streamlit App: Users can input data such as flat type, floor area, and location to get an estimate of the resale price.

Conclusion

    The Decision Tree Regressor model will provide a solid prediction for flat resale prices.
    The Streamlit application makes it user-friendly and accessible for anyone interested in predicting resale prices for flats in Singapore.
    This model can help buyers, sellers, and real estate investors make informed decisions by estimating the resale price of flats based on specific features.
