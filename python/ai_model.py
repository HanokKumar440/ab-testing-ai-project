import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_excel("data/ab_testing_dataset.xlsx")  
df["activity_level"] = df["activity_level"].map({
    "low": 0,
    "medium": 1,
    "high": 2
})

df["group"] = df["group"].map({
    "A": 0,
    "B": 1
})

X = df[["age", "activity_level", "time_spent", "group", "clicked"]]
y = df["converted"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))