# Invistico Airlines: Predicting Passenger Satisfaction

## Motivation
Apply supervised machine learning models to accurately predict airline passenger satisfaction/dissatisfaction and calculate feature importances, such that targeted customer loyalty schemes and the improvement of services can be prioritized.

## File Links

* [Overview Report](https://github.com/dilraj451/Airline-Passenger-Satisfaction-Prediction/blob/main/report.pdf)
* [Jupyter Notebook](https://github.com/dilraj451/Airline-Passenger-Satisfaction-Prediction/blob/main/invistico_airline.ipynb) containing full analysis

## Methodology
* Exploratory Data Analysis (EDA) using pandas, matplotlib, and ydata (for initial automated EDA report).
* Data Cleaning carried out by use of pandas functions to remove duplicates, encode categorical features, and fill blank fields.
* Machine learning models (RandomForestClassifier and XGBClassifier) were fine-tuned using cross-validation methods to optimize each models parameters and their performances evaluated against a basseline model; methods for hyperparameter optimisation and model evaluation were provided by scikit-learn.

## Conclusions
* Recall values of ~93% by both machine learning models massively surpoasses baseline model and is comparable to high quality models in similar classification scenarios.
* Averaged feature importance data indicates inflight entertainment, seat comfort, and ease of online booking are the three most importnat services impacting passenger satisfaction.
