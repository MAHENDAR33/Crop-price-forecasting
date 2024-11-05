import streamlit as st
import pandas as pd

# Load predictions from the CSV file
predictions_df = pd.read_csv('predictions2.csv')

# Build the Streamlit app
st.title("Crop Price Predictions (2025-2030)")

# Load the image file from a path or URL
image_path = 'https://krishimaratavahini.karnataka.gov.in/storage/slids/1581406024.jpg'

# Display the image
st.image(image_path, caption='MSP - Department of Agricultural Marketing', use_column_width=True)

col1, col2 = st.columns(2)

# English text in the first column
with col1:
    st.write("""
    This web application predicts the future Minimum Support Price (MSP) of crops from 2024 to 2030 using machine learning models. 
    It provides valuable insights to farmers, traders, and policymakers, enabling them to make informed decisions. 
    """)

# Kannada text in the second column
with col2:
    st.write("""
    ಈ ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್ 2024 ರಿಂದ 2030 ರವರೆಗೆ ಬೆಳೆಗಳ ಕನಿಷ್ಠ ಬೆಂಬಲ ಬೆಲೆಯ (MSP) ಭವಿಷ್ಯವನ್ನು ಯಾಂತ್ರಿಕ ಅಧ್ಯಯನ ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ನುಡಿಸುತ್ತದೆ. 
    ಇದು ರೈತರು, ವ್ಯಾಪಾರಿಗಳು, ಮತ್ತು ನೀತಿಮಾಕರ್ಗಳು ತೀರ್ಮಾನಗಳನ್ನು ಎತ್ತಿಕೊಳ್ಳಲು ಮುಖ್ಯವಾದ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸುತ್ತದೆ.
    """)

# Dropdown to select a crop
selected_crop = st.selectbox("Select a Crop", predictions_df['Crop'].unique())

# Dropdown to select a year
selected_year = st.selectbox("Select a Year", predictions_df['Year'].unique())

# Filter the DataFrame based on selected crop and year
filtered_df = predictions_df[(predictions_df['Crop'] == selected_crop) & (predictions_df['Year'] == selected_year)]

# Display the prediction for the selected crop and year
if not filtered_df.empty:
    predicted_price = filtered_df['Predicted Price'].values[0]
    st.write(f"Predicted price for {selected_crop} in {selected_year}: {predicted_price}")
else:
    st.write("No data available for the selected crop and year.")
