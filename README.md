🌿 TreeVert – AI Powered Tree Emotion Detection System
Predicting how plants “feel” using Machine Learning + IoT + Flask + HTML Dashboard
🌱 Overview

TreeVert is an AI + IoT system that predicts the emotional state of a tree based on environmental conditions collected through sensors.

Emotions include:

🌳 Happy

💧 Thirsty

🔥 Heat Stress

The system gathers real-time data from IoT sensors and passes them to an ML model that returns the tree’s emotional state. A beautiful animated TreeVert Web Dashboard shows the result visually.

🧠 Features

✔ Predict tree emotion using ML
✔ IoT-powered sensor data (Temp, Humidity, Moisture, Light)
✔ ESP32 + Sensors to collect real-time data
✔ Flask backend for ML prediction API
✔ Beautiful HTML Dashboard (TreeVert UI)
✔ Floating leaf animations 🌿
✔ Interactive slider-based simulator
✔ Works offline locally

🏗 Tech Stack
🔧 Hardware (IoT)

ESP32 WiFi Microcontroller

DHT22 (Temperature + Humidity)

Capacitive Soil Moisture Sensor

LDR Light Sensor + 10k Resistor

Breadboard + Jumper Wires

🧪 Software

Python

Flask API

scikit-learn (ML Model)

HTML/CSS/JS UI

Pickle model saving

Jupyter Notebook

📊 Dataset

The dataset contains:

🌡 temp — Temperature

💧 humidity — Humidity

🌱 moisture — Soil moisture

☀️ light — Light intensity

⚡ mean_voltage, entropy — Bio signals (simulated)

🏷 label — Tree emotion

CSV example:

tree_id, tree_name, location, temp, humidity, moisture, light, label
TREE_001, Mahogany, EcoGarden, 36.3, 47.2, 22.1, 966.5, Heat_Stress

🤖 Machine Learning

Model used:

RandomForestClassifier

Training steps:

Load dataset

Select feature columns

Train ML model

Save as tree_model.pkl

🌐 Web App Architecture
ESP32 Sensors → Flask API → ML Model → TreeVert Frontend UI

🔥 Routes
Route	Method	Purpose
/	GET	Loads TreeVert HTML UI
/predict	POST	Returns emotion prediction
🎨 TreeVert UI Preview

🌿 Fully animated
🍃 Floating leaves
💚 Glass-effect cards
🔘 Sliders for simulation
⚡ Instant prediction
🎯 Emotion-based color effects

▶ How to Run Locally
1️⃣ Install dependencies
pip install flask scikit-learn pandas numpy

2️⃣ Run the Flask app
python app.py

3️⃣ Open your browser
http://127.0.0.1:5000

🔗 File Structure
EMOVERT_TREE_PROJECT/
│── app.py
│── TreeVert.html
│── tree_model.pkl
│── Tree_Emotion_Dataset_Extended.csv
│── README.md

🛠 Future Enhancements

Real plant electrophysiology sensors

Cloud dashboard (Firebase / AWS)

Live camera + plant image health check

Automatic watering system

Mobile app

❤️ Created By

Cherry ⚡
Inspiration: Protecting trees using AI + IoT 🌳💚
Project Name: TreeVert

⭐ Support this project

🌟 Star this repo if you like the idea!
🌿 Let's make plant communication smarter.

If you want, I can also generate:

✅ GitHub repo description
✅ Commit messages
✅ LICENSE file
✅ Banner image for your repo (SVG / PNG)
Just say “Make banner” or “Add license” ⚡
