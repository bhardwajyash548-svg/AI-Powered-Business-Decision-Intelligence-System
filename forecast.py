import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("data/cleaned_superstore.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Month_Number"] = range(len(monthly_sales))

X = monthly_sales[["Month_Number"]]
y = monthly_sales["Sales"]

model = LinearRegression()
model.fit(X, y)

future_month = [[len(monthly_sales)]]

prediction = model.predict(future_month)

print("Predicted Next Month Revenue:", prediction[0])

predicted_revenue = prediction[0]
