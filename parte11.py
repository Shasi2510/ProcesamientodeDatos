from datasets import load_dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import GridSearchCV


dataset = load_dataset("mstz/hert_failure")

data = ['dataset']
df=pd.DataFrame['data']

plt.figure(figsize=(10,6))
plt.title('Distribución de Clases')
sns.countplot(data=df, x='age')
plt.show()

X = df.drop('age', axis=1)
y = df['age']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print('Best parameters:', best_params)

y_pred_best = grid_search.predict(X_test)
accuracy_best = accuracy_score(y_test)
