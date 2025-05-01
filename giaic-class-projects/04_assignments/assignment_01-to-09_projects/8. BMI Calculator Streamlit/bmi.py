import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.markdown(
        """
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stButton>button { background-color: #007BFF; color: white; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("⚖️ Professional BMI Calculator")
st.write("👨‍💻 Developed by: **Nabeel Ali**")
st.markdown("---")

height_unit = st.radio("📏 Select Height Unit:", ["Centimeters (cm)", "Meters (m)", "Feet (ft)"])

if height_unit == "Centimeters (cm)":
    height = st.number_input("📏 Enter your Height in cm:", min_value=50, max_value=250, value=170)
    height_m = height / 100
elif height_unit == "Meters (m)":
    height = st.number_input("📏 Enter your Height in meters:", min_value=0.5, max_value=2.5, value=1.7)
    height_m = height
else:
    height = st.number_input("📏 Enter your Height in feet:", min_value=2.0, max_value=8.0, value=5.6)
    height_m = height * 0.3048

weight = st.number_input("⚖️ Enter your Weight (kg):", min_value=10, max_value=300, value=70)

if st.button("🚀 Calculate BMI"):
    bmi = round(weight / (height_m ** 2), 2)

    if bmi < 18.5:
        category = "🔵 Underweight (🥦 Eat healthy!)"
        color = "blue"
    elif 18.5 <= bmi < 24.9:
        category = "🟢 Normal Weight (💪 Keep it up!)"
        color = "green"
    elif 25 <= bmi < 29.9:
        category = "🟠 Overweight (🏃 Time to move!)"
        color = "orange"
    else:
        category = "🔴 Obese (⚠️ Health Alert!)"
        color = "red"

    st.markdown("---")
    st.subheader(f"📊 Your BMI: **{bmi}**")
    st.markdown(f"<h3 style='color: {color};'>{category}</h3>", unsafe_allow_html=True)
    st.success("✅ Maintain a balanced diet and exercise regularly for a healthy BMI! 🏋️‍♂️🥗")

st.markdown("---")
st.write("💡 **BMI Calculation Formula:** `BMI = Weight (kg) ÷ (Height (m)²)`")
st.write("📌 This tool provides a general health indication based on BMI values. 🚑")
st.write("🛠️ Built with ❤️ using **Streamlit**")