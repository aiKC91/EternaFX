---
created: 2025-01-08T09:16:34-08:00
modified: 2025-01-08T09:16:36-08:00
---

# machine_learning.py

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model
