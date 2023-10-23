import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Sample dataset
data = {
    'Age': [25, 45, 35, 20, 50, 65, 55, 30,35,26,70],
    'Income': ['High', 'Low', 'Medium', 'Low', 'Medium', 'High', 'Medium', 'Low','High', 'Medium', 'Low'],
    'Education': ['High', 'Low', 'Medium', 'Low', 'Medium', 'High', 'Medium', 'Low','High', 'Medium', 'Low'],
    'Vote': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No','Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Data Preprocessing
df = pd.get_dummies(df, columns=['Income', 'Education'], drop_first=True)
df['Vote'] = df['Vote'].map({'Yes': 1, 'No': 0})

# Train-Test Split
X = df.drop('Vote', axis=1)
y = df['Vote']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=38)

# Decision Tree Model
dtc = DecisionTreeClassifier(max_depth=3, random_state=42)
dtc.fit(X_train, y_train)

# Decision Tree Visualization
plt.figure(figsize=(11, 11))
tree.plot_tree(dtc, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()

