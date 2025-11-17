from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load Linear Regression model
lr = joblib.load("linear_model.joblib")

@app.route("/")
def home():
    return "Linear Regression API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    X = np.array(data).reshape(1, -1)
    pred = lr.predict(X)[0]
    return jsonify({"prediction": float(pred)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
