import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# load dataset
df = pd.read_csv("dataset.csv")

X = df[["income", "expenses", "emi", "savings"]]
y = df["stress_score"]

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# save model
joblib.dump(model, "model.pkl")

print("Model trained and saved!")