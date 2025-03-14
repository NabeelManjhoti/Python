import streamlit as st
from forex_python.converter import CurrencyRates # type: ignore

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    }
    return value * length_units[to_unit] / length_units[from_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274
    }
    return value * weight_units[to_unit] / weight_units[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    if from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

def convert_currency(value, from_currency, to_currency):
    c = CurrencyRates()
    return c.convert(from_currency, to_currency, value)

# Streamlit UI
st.title("Unit Converter By Nabeel Ali")

unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature", "Currency"])

if unit_type == "Length":
    from_unit = st.selectbox("From", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
    to_unit = st.selectbox("To", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
    value = st.number_input("Enter Value", min_value=0.0, step=0.1)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "Weight":
    from_unit = st.selectbox("From", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
    to_unit = st.selectbox("To", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
    value = st.number_input("Enter Value", min_value=0.0, step=0.1)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value", step=0.1)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif unit_type == "Currency":
    from_currency = st.text_input("From (Currency Code, e.g., USD, EUR, PKR)").upper()
    to_currency = st.text_input("To (Currency Code, e.g., USD, EUR, PKR)").upper()
    value = st.number_input("Enter Value", min_value=0.0, step=0.1)
    if st.button("Convert"):
        try:
            result = convert_currency(value, from_currency, to_currency)
            st.success(f"{value} {from_currency} = {result:.2f} {to_currency}")
        except Exception as e:
            st.error("Error fetching exchange rates. Check currency codes and try again.")