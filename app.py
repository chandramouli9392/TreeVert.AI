from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import pickle
import os

app = Flask(__name__)

# ------------------------------
# 1️⃣ Load Dataset
# ------------------------------
df = pd.read_csv("Tree_Emotion_Dataset_Extended.csv")

# Dataset columns:
# tree_id, tree_name, location, timestamp, mean_voltage, entropy, temp,
# humidity, moisture, light, label

X = df[['temp', 'humidity', 'moisture', 'light']]
y = df['label']   # emotion label

# ------------------------------
# 2️⃣ Load or Train Model
# ------------------------------
MODEL_PATH = "tree_model.pkl"

def train_and_save_model():
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X, y)
    pickle.dump(model, open(MODEL_PATH, "wb"))
    print("✅ Model trained and saved as tree_model.pkl")
    return model

# Load model or train if missing
if os.path.exists(MODEL_PATH):
    try:
        model = pickle.load(open(MODEL_PATH, "rb"))
        print("✅ Model loaded successfully!")
    except Exception:
        print("⚠ Model corrupted! Retraining...")
        model = train_and_save_model()
else:
    print("⚠ No model found. Training...")
    model = train_and_save_model()

# ------------------------------
# 3️⃣ Serve the HTML UI
# ------------------------------
@app.route("/")
def home():
    with open("TreeVert.html", "r", encoding="utf-8") as file:
        return file.read()

# ------------------------------
# 4️⃣ ML Prediction API
# ------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    temp = float(data["temp"])
    humidity = float(data["humidity"])
    moisture = float(data["moisture"])
    light = float(data["light"])

    input_df = pd.DataFrame([[temp, humidity, moisture, light]],
                            columns=['temp', 'humidity', 'moisture', 'light'])

    pred = model.predict(input_df)[0]

    return jsonify({"emotion": pred})

# ------------------------------
# 5️⃣ Run Server
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
