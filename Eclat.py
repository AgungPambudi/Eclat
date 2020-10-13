# Eclat Algorithm tutorial from Machine Learning A-Z - SuperDataScience -> Input by Ryan L Buchanan 12OCT20

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing 
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])

# Training the Eclat model on the dataset


