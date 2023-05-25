#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:33:24 2023

@author: SwasthikBangera
@project: Formula1 winner prediction

"""

# Importing the dependencies

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv("formula1_data.csv")

# Create the features
features = [
    "driver_name",
    "team_name",
    "car_model",
    "circuit_name",
    "weather",
    "track_temperature",
    "air_temperature",
    "race_distance",
]

# Create the target variable
target = "winner"

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.25)

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Print the predicted winner for the next race
next_race = "Spanish Grand Prix"
predicted_winner = model.predict_proba(df[features][df["race_name"] == next_race])[0].argmax()
print("Predicted winner for the {}: {}".format(next_race, df[features]["driver_name"][predicted_winner]))