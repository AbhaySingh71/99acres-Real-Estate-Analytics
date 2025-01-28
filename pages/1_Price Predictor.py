import streamlit as st
import pickle
import pandas as pd
import numpy as np
import gzip

# Page Configuration
st.set_page_config(page_title="Real Estate Price Prediction", page_icon="🏠", layout="wide")

# Sidebar - Logo and App Info
st.sidebar.image("datasets/front image.png", use_container_width=True)  # Add an image in the sidebar

st.sidebar.title("📌 About This App")
st.sidebar.info(
    "This **Real Estate Price Prediction** app helps users estimate property prices "
    "based on various parameters such as location, property type, built-up area, and amenities. "
)


# Custom CSS for Better UI
st.markdown("""
    <style>
    .stTextInput, .stSelectbox, .stNumberInput {
        margin-bottom: 20px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 12px 28px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stMarkdown {
        font-size: 18px;
        font-weight: bold;
        color: #2E8B57;
    }
    .stHeader {
        color: #00796B;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Load pre-trained models
with open('datasets/df.pkl', 'rb') as file:
    df = pickle.load(file)

#with open('datasets/pipeline.pkl', 'rb') as file:
#    pipeline = pickle.load(file)

with gzip.open('pipeline1.pkl.gz', 'rb') as file:
    pipeline = pickle.load(file)    

# Header
st.header("🏠 **Real Estate Price Prediction**")
st.markdown("Enter the details below to predict the price of the property.")

# Property Type and Inputs Layout
input_columns = st.columns(2)

with input_columns[0]:
    property_type = st.selectbox('Property Type', ['flat', 'house'])
    sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
    bedrooms = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
    bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
    balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

with input_columns[1]:
    property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
    built_up_area = float(st.number_input('Built Up Area (in sq.ft)', min_value=100.0, step=10.0))
    servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
    store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
    furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
    luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
    floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# Predict Button with Enhancements
if st.button('🔍 **Predict Price**'):
    # Create a DataFrame from the inputs
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']
    
    one_df = pd.DataFrame(data, columns=columns)

    # Predict price using the pipeline
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # Enhanced Prediction Text
    st.markdown(f"### 🏡 **The estimated price of the property is between ₹{low:,.2f} Cr and ₹{high:,.2f} Cr.**")

    # Display Property Details in a Grid Layout
    st.markdown("#### 📋 **Property Details**")

    # Create a 2-column layout for property details
    details_columns = st.columns(2)

    with details_columns[0]:
        st.markdown(f"**Property Type**: {property_type.capitalize()}")
        st.markdown(f"**Sector**: {sector.capitalize()}")
        st.markdown(f"**Bedrooms**: {bedrooms}")
        st.markdown(f"**Bathrooms**: {bathroom}")
        st.markdown(f"**Balconies**: {balcony}")
        st.markdown(f"**Property Age**: {property_age} years")

    with details_columns[1]:
        st.markdown(f"**Built-up Area**: {built_up_area} sq.ft")
        st.markdown(f"**Servant Room**: {servant_room}")
        st.markdown(f"**Store Room**: {store_room}")
        st.markdown(f"**Furnishing Type**: {furnishing_type.capitalize()}")
        st.markdown(f"**Luxury Category**: {luxury_category.capitalize()}")
        st.markdown(f"**Floor Category**: {floor_category.capitalize()}")

    st.markdown("---")
    st.info("Note: The price prediction is based on the provided features and is an estimation only.")
    st.info("Note: To get the most accurate results, please provide **reliable and precise input values**. This model performs best with accurate and detailed information.")
