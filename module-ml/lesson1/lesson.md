# Machine Learning Module - Lesson 1: Introduction to ML

Welcome to the first lesson of the Machine Learning module! Let's explore the foundations of ML.

## Learning Objectives

- Understand basic ML concepts and terminology
- Explore the difference between supervised and unsupervised learning
- Learn about common ML algorithms
- Implement a simple classification model

## Machine Learning Basics

Machine Learning (ML) is a subset of artificial intelligence that focuses on building systems that can learn from and make decisions based on data.

### Types of Machine Learning

1. **Supervised Learning**: The algorithm learns from labeled training data, making predictions or decisions based on that data.
   - Classification: Predicting a category (e.g., spam/not spam)
   - Regression: Predicting a continuous value (e.g., house prices)

2. **Unsupervised Learning**: The algorithm finds patterns in unlabeled data.
   - Clustering: Grouping similar data points
   - Dimensionality Reduction: Simplifying data while preserving information

3. **Reinforcement Learning**: Learning through trial and error with rewards/penalties.

### Common Algorithms

- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forests
- Support Vector Machines (SVM)
- K-means Clustering
- Neural Networks

## Data Preprocessing

Before applying ML algorithms, data typically needs to be preprocessed:

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv('dataset.csv')

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.drop('target', axis=1))
```

## Challenge

In the `challenge.py` file, you'll find a dataset and instructions to build a simple classification model. Complete the challenge to earn your key to the next lesson!

## Next Steps

After completing this lesson's challenge, you'll unlock Lesson 2, where we'll dive deeper into feature engineering and model evaluation techniques.
