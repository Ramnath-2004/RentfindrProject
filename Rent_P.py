import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv("Districts.csv")

# Preprocess the 'Sqft' column
data['Sqft'] = data['Sqft'].str.replace(',', '').astype(float)

# Perform one-hot encoding for the 'District' column
data_encoded = pd.get_dummies(data, columns=['District'])

# Split the dataset into features (X) and target variable (y)
X = data_encoded.drop(columns=["Price", "Address", "Predicted Price"])
y = data_encoded["Price"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the Random Forest Regression model with hyperparameter tuning
rf_model = RandomForestRegressor(n_estimators=700, max_depth=10, min_samples_split=5, min_samples_leaf=2, random_state=42)  

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = rf_model.predict(X_test)
print("Predicted Prices:")
for sqft_value, predicted_price in zip(data_encoded['Sqft'], predicted_prices):
    print(f"Square Footage: {sqft_value}, Predicted Price: {predicted_price}")
# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)
print("Accuracy:", rf_model.score(X_test, y_test))

# Create a new column for predicted prices in the dataset
data_encoded['Predicted Price'] = rf_model.predict(X)

# Save the updated dataset to a new CSV file
data_encoded.to_csv("updated_dataset.csv", index=False)
