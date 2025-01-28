import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Set Streamlit page config
st.set_page_config(page_title="🏡 Apartment Recommender", page_icon="🏠", layout="wide")

# Load Data
property_data = pd.read_csv("datasets/appartments.csv")  # Load CSV with all property details
location_df = pickle.load(open('datasets/location_df_merge.pkl', 'rb'))
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

# 🎯 Function to Recommend Properties
def recommend_properties(property_name, w1=0.5, w2=0.8, w3=1, top_n=5):
    cosine_sim_matrix = w1 * cosine_sim1 + w2 * cosine_sim2 + w3 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [round(i[1], 3) for i in sorted_scores[1:top_n + 1]]  # Round scores
    top_properties = location_df.index[top_indices].tolist()
    links = property_data.set_index("PropertyName").loc[top_properties]["Link"].tolist()
    
    return pd.DataFrame({'Property Name': top_properties, 'Similarity Score': top_scores, 'Link': links})

# 🔷 Sidebar
with st.sidebar:
    st.image("datasets/banner image.jpg", use_container_width=True)
    st.title("🏡 Apartment Finder")
    st.markdown("Find the **best apartments** near your location based on multiple similarity measures. Adjust settings and explore!")
    st.markdown("---")
    st.markdown("👈 Use the sidebar to navigate!")

# 🏙️ Section: Location Search
st.markdown("## 📍 Find Nearby Apartments")
col1, col2 = st.columns(2)
with col1:
    selected_location = st.selectbox('🔍 Select Location:', sorted(location_df.columns.to_list()), help="Start typing to search")
with col2:
    radius = st.slider('📏 Radius (in Kms)', 1, 50, 5, 1)

if st.button('🔎 Search Apartments'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    st.success(f"Found **{len(result_ser)}** apartments within {radius} km of **{selected_location}**")
    for key, value in result_ser.items():
        st.markdown(f"🏠 **{key}** - {round(value / 1000, 2)} km")

# 🏡 Section: Apartment Recommendation
st.markdown("---")
st.markdown("## 🏡 Get Similar Apartment Recommendations")
selected_apartment = st.selectbox('🏠 Select an Apartment:', sorted(location_df.index.to_list()), help="Start typing to search")

# 🎛️ Adjust Similarity Weights
st.markdown("### ⚖️ Adjust Similarity Weights")
w1 = st.slider("🔹 Facilities Similarity", 0.0, 1.5, 0.5, 0.1)
w2 = st.slider("🔹 Pricing Similarity", 0.0, 1.5, 0.8, 0.1)
w3 = st.slider("🔹 Location Similarity", 0.0, 1.5, 1.0, 0.1)

if st.button('✨ Show Recommendations'):
    recommendation_df = recommend_properties(selected_apartment, w1, w2, w3)
    
    for i, row in recommendation_df.iterrows():
        st.markdown(f'''
        <div style="border-radius:10px; padding:15px; margin-bottom:10px; 
                    background-color:#1E3A5F; color:white; font-size:16px; 
                    box-shadow: 3px 3px 10px rgba(0,0,0,0.2);">
        <h4 style="margin:0; padding:5px;">🏠 {row['Property Name']}</h4>
        <p style="margin:0;">🔹 <b>Similarity Score:</b> {row['Similarity Score']}</p>
        <p style="margin:0;"><a href="{row['Link']}" target="_blank" style="color:#FFD700; font-weight:bold; text-decoration:none;">🔗 View Property</a></p>
        </div>
        ''', unsafe_allow_html=True)
