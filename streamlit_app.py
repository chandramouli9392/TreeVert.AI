# streamlit_app.py
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

st.set_page_config(page_title="TreeVert", layout="centered")

st.title("🌿 TreeVert — AI Tree Emotion Predictor")

# --- Load model safely ---
MODEL_FILENAME = "tree_model.pkl"   # or tree_model.pkl / model.pkl - match your file name

model = None
if os.path.exists(MODEL_FILENAME):
    try:
        with open(MODEL_FILENAME, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        st.warning(f"Model exists but couldn't be loaded. Error: {e}")
        model = None
else:
    st.info("No model file found in repo. The app will use a simple rule-based fallback.")

# --- UI sliders ---
col1, col2 = st.columns(2)
with col1:
    temp = st.slider("Temperature (°C)", 20.0, 45.0, 30.0, step=0.5)
    humidity = st.slider("Humidity (%)", 10.0, 100.0, 60.0, step=0.5)
with col2:
    moisture = st.slider("Soil Moisture (%)", 0.0, 100.0, 50.0, step=0.5)
    light = st.slider("Light Intensity (Lux)", 0.0, 2000.0, 600.0, step=1.0)

if st.button("🌿 Predict Emotion"):
    # If ML model loaded, use it
    if model is not None:
        try:
            X = np.array([[temp, humidity, moisture, light]])
            # if model was trained with different feature order, adjust accordingly
            pred = model.predict(X)[0]
            proba = None
            if hasattr(model, "predict_proba"):
                try:
                    proba = model.predict_proba(X).max()
                except:
                    proba = None
            st.success(f"Predicted: **{pred}**" + (f" (confidence {proba:.2f})" if proba is not None else ""))
        except Exception as e:
            st.error(f"Error while predicting with model: {e}")
    else:
        # fallback rule-based prediction (same logic as your HTML example)
        if temp < 30 and moisture > 50 and humidity > 50:
            st.success("🌳 Happy — The tree feels calm and healthy!")
        elif moisture < 40:
            st.warning("💧 Thirsty — The tree needs water soon!")
        elif temp > 35 and light > 800:
            st.error("🔥 Heat Stress — Too much sunlight/heat!")
        else:
            st.info("🌿 Neutral — Conditions are acceptable.")

st.markdown("---")
st.caption("If you want the ML model to run, upload `tree_model.pkl` in the repo root or train & save it locally then push it.")
