import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

base = pd.read_csv("../data/norm.csv")

y = base["value"]
del base["value"]
X = base

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

model = RandomForestRegressor(random_state=1, n_estimators=30)
model.fit(train_X, train_y)
print(base.head(40))

estimators = np.arange(10, 200, 10)
scores = []
for n in estimators:
    model.set_params(n_estimators=n)
    model.fit(train_X, train_y)
    scores.append(model.score(val_X, val_y))
plt.title("Effect of n_estimators")
plt.xlabel("n_estimator")
plt.ylabel("score")
plt.plot(estimators, scores)
plt.show()

best_estimator = np.array(scores).argmax()
best_estimator = estimators[best_estimator]

print("optimal n estimators:", best_estimator)

predictions = model.predict(val_X)
accuracy = model.score(val_X, val_y)

print("accuracy:", accuracy)