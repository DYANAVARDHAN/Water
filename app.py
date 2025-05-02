import streamlit as st
import joblib
import numpy as np

# Load the trained water quality model
model = joblib.load("water_quality_model.pkl")

# Streamlit UI
st.title("Water Quality Prediction 🚰")
st.markdown("### Enter the water quality parameters:")

# Input features
feature_names = [
    "pH", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic Carbon", "Trihalomethanes", "Turbidity"
]

input_data = []
for feature in feature_names:
    value = st.number_input(f"{feature}", min_value=0.0, format="%.2f")
    input_data.append(value)

# Fixed explanations
portable_explanation = """
✅ **LLM Explanation**: The water is safe to drink because the parameters are within recommended limits. It meets the criteria for potable water.
"""

not_portable_explanation = """
❌ **LLM Explanation**: The water is not safe to drink. One or more parameters are outside the acceptable range, indicating possible contamination or quality issues.
"""

# Predict button
if st.button("Check Water Quality"):
    try:
        if None in input_data:
            st.error("Please enter all required values before checking water quality.")
        else:
            input_array = np.array(input_data).reshape(1, -1)
            prediction = model.predict(input_array)

            if prediction[0] == 1:
                st.success("**Prediction:** ✅ Potable (Safe to Drink)")
                st.markdown(portable_explanation)
            else:
                st.error("**Prediction:** ❌ Not Potable (Unsafe)")
                st.markdown(not_portable_explanation)

    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.caption("Powered by Machine Learning 🚀")
