# from flask import Flask, request, jsonify
# import joblib
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for React frontend

# # Load trained model & scaler
# model = joblib.load(r"C:\Users\MAYUR\Desktop\mental_health_prediction\backend\mental_random_forest.pkl")  # Ensure correct path
# scaler = joblib.load(r"C:\Users\MAYUR\Desktop\mental_health_prediction\backend\scaler.pkl")

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get JSON data from request
#         data = request.json
#         features = np.array(data["features"]).reshape(1, -1)  # Convert input to numpy array
        
#         # Scale features
#         features_scaled = scaler.transform(features)

#         # Predict mental health condition
#         prediction = model.predict(features_scaled)[0]

#         # Return prediction result
#         return jsonify({"mental_health_condition": int(prediction)})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# OPTIMIZED CODE 


# from flask import Flask, request, jsonify
# import joblib
# import numpy as np
# from flask_cors import CORS
# import os

# app = Flask(__name__)
# CORS(app)  # Enable CORS for React frontend

# # Load trained model & scaler safely
# MODEL_PATH = r"C:\Users\MAYUR\Desktop\mental_health_prediction\backend\mental_random_forest.pkl"
# SCALER_PATH = r"C:\Users\MAYUR\Desktop\mental_health_prediction\backend\scaler.pkl"

# if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
#     raise FileNotFoundError("Model or Scaler file not found. Check paths!")

# model = joblib.load(MODEL_PATH)
# scaler = joblib.load(SCALER_PATH)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get JSON data from request
#         data = request.json
#         if not data or "features" not in data:
#             return jsonify({"error": "Missing 'features' in request"}), 400

#         features = np.array(data["features"]).reshape(1, -1)  # Convert input to NumPy array
        
#         # Scale features
#         features_scaled = scaler.transform(features)

#         # Predict mental health condition
#         prediction = model.predict(features_scaled)[0]

#         # Return prediction result
#         return jsonify({"mental_health_condition": int(prediction)})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import joblib
# import numpy as np
# from flask_cors import CORS
# import os
# import logging

# # Set up logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)

# app = Flask(__name__)
# CORS(app)  # Enable CORS for React frontend

# # Load trained model & scaler safely
# MODEL_PATH = r"C:\Users\MAYUR\Desktop\mental_health_prediction\backend\mental_random_forest.pkl"
# SCALER_PATH = r"C:\Users\MAYUR\Desktop\mental_health_prediction\backend\scaler.pkl"

# # Validate file existence
# if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
#     raise FileNotFoundError("Model or Scaler file not found. Check paths!")

# try:
#     model = joblib.load(MODEL_PATH)
#     scaler = joblib.load(SCALER_PATH)
#     logger.info("Model and scaler loaded successfully")
# except Exception as e:
#     logger.error(f"Error loading model or scaler: {e}")
#     raise

# @app.route('/health', methods=['GET'])
# def health():
#     """Health check endpoint"""
#     return jsonify({"status": "healthy", "model_loaded": True})

# @app.route('/predict', methods=['POST'])
# def predict():
#     """
#     Predict mental health condition based on input features.
#     Expected input format: {"features": [f1, f2, ..., fn]}
#     """
#     try:
#         # Get JSON data from request
#         data = request.json
#         if not data or "features" not in data:
#             return jsonify({"error": "Missing 'features' in request"}), 400

#         features = data["features"]
        
#         # Validate features is a list
#         if not isinstance(features, list):
#             return jsonify({"error": "Features must be a list"}), 400

#         # Convert input to NumPy array
#         features = np.array(features).reshape(1, -1)
        
#         # Validate feature count
#         expected_features = model.n_features_in_
#         if features.shape[1] != expected_features:
#             return jsonify({
#                 "error": f"Expected {expected_features} features, got {features.shape[1]}"
#             }), 400

#         # Scale features
#         try:
#             features_scaled = scaler.transform(features)
#         except Exception as e:
#             logger.error(f"Error during feature scaling: {e}")
#             return jsonify({"error": "Error scaling features. Check feature values."}), 400

#         # Predict mental health condition
#         prediction = model.predict(features_scaled)[0]
        
#         # Get prediction probabilities for confidence scores
#         probabilities = model.predict_proba(features_scaled)[0].tolist()

#         # Log successful prediction
#         logger.info(f"Successful prediction made: {prediction}")

#         # Return prediction result with confidence scores
#         return jsonify({
#             "mental_health_condition": int(prediction),
#             "confidence_scores": probabilities,
#             "status": "success"
#         })

#     except ValueError as ve:
#         logger.error(f"ValueError in prediction: {ve}")
#         return jsonify({"error": "Invalid feature values provided"}), 400
#     except Exception as e:
#         logger.error(f"Unexpected error in prediction: {e}")
#         return jsonify({"error": "An unexpected error occurred"}), 500

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
#     app.run(host='0.0.0.0', port=port, debug=debug_mode)

from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS
import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load trained model & scaler safely
MODEL_PATH = r"C:\Users\Admin\Desktop\mentaal-Health-prediction-frontend-backend\backend\mental_random_forest.pkl"
SCALER_PATH = r"C:\Users\Admin\Desktop\mentaal-Health-prediction-frontend-backend\backend\scaler.pkl"

# Validate file existence
if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
    raise FileNotFoundError("Model or Scaler file not found. Check paths!")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    logger.info("Model and scaler loaded successfully")
except Exception as e:
    logger.error(f"Error loading model or scaler: {e}")
    raise

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "model_loaded": True})

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict mental health condition based on input features.
    Expected input format: {"features": [f1, f2, ..., fn]}
    """
    try:
        # Get JSON data from request
        data = request.json
        if not data or "features" not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400

        features = data["features"]
        
        # Validate features is a list
        if not isinstance(features, list):
            return jsonify({"error": "Features must be a list"}), 400

        # Convert input to NumPy array
        features = np.array(features).reshape(1, -1)
        
        # Validate feature count
        expected_features = model.n_features_in_
        if features.shape[1] != expected_features:
            return jsonify({
                "error": f"Expected {expected_features} features, got {features.shape[1]}"
            }), 400

        # Scale features
        try:
            features_scaled = scaler.transform(features)
        except Exception as e:
            logger.error(f"Error during feature scaling: {e}")
            return jsonify({"error": "Error scaling features. Check feature values."}), 400

        # Predict mental health condition
        prediction = model.predict(features_scaled)[0]

        # Log successful prediction
        logger.info(f"Successful prediction made: {prediction}")

        # Return prediction result (without confidence field)
        return jsonify({
            "mental_health_condition": int(prediction),
            "status": "success"
        })

    except ValueError as ve:
        logger.error(f"ValueError in prediction: {ve}")
        return jsonify({"error": "Invalid feature values provided"}), 400
    except Exception as e:
        logger.error(f"Unexpected error in prediction: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
