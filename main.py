from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Sample training data
df = pd.DataFrame({
    'Square_Feet': [1500, 2000, 2500, 3000],
    'Bedrooms': [3, 4, 3, 5],
    'Bathrooms': [2, 2, 3, 4],
    'Proximity_to_City': [1, 0, 1, 0],
    'Price': [300000, 400000, 350000, 500000]
})

# Prepare the features (X) and target (y)
X = df[['Square_Feet', 'Bedrooms', 'Bathrooms', 'Proximity_to_City']]
y = df['Price']

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Define the prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from the incoming request (expects JSON)
        data = request.get_json()

        # Extract values from the data (squareFeet, bedrooms, bathrooms, proximity)
        square_feet = data.get("squareFeet", 0)
        bedrooms = data.get("bedrooms", 0)
        bathrooms = data.get("bathrooms", 0)
        proximity = data.get("proximity", 0)

        # Validate input values (ensure they are numbers)
        if not all(isinstance(v, (int, float)) for v in [square_feet, bedrooms, bathrooms, proximity]):
            return jsonify({"error": "Invalid input. All values must be numbers."}), 400

        # Make the prediction using the model
        prediction = model.predict([[square_feet, bedrooms, bathrooms, proximity]])[0]

        # Return the prediction as JSON
        return jsonify({"price": round(prediction)})

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
