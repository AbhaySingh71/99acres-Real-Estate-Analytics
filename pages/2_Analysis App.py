import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Configure Streamlit Page
st.set_page_config(page_title="Real Estate Analytics", layout="wide", page_icon="🏡")

# Sidebar Navigation
st.sidebar.header("🔍 Dashboard Navigation")
section = st.sidebar.radio("Go to", ["🏡 Overview", "📊 Data Visualization", "🔍 Insights"])

# Load Data
new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

new_df['total_area'] = new_df['built_up_area']  # If you have other columns, you can sum them here

# Group Data for Map Visualization
group_df = new_df.groupby('sector').mean(numeric_only=True)[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]

# --- Overview Section ---
if section == "🏡 Overview":
    st.title("🏡 Real Estate Analytics Dashboard")
    
    # Display Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🏠 Total Properties", len(new_df))
    col2.metric("📍 Unique Sectors", new_df['sector'].nunique())
    col3.metric("💰 Avg Price (₹)", f"{new_df['price'].mean():,.0f}CR")
    col4.metric("📏 Avg Built-up Area", f"{new_df['built_up_area'].mean():,.0f} sq.ft")
    
    st.markdown("---")
    
    # Sector Price per Sqft Geomap
    st.subheader("🌍 Sector Price per Sqft Geomap")
    fig_map = px.scatter_mapbox(
        group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
        mapbox_style="carto-positron", width=1100, height=600, hover_name=group_df.index
    )
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Avg Price per Sector Bar Chart
    st.subheader("📊 Average Price per Sector")
    fig_bar = px.bar(group_df, x=group_df.index, y='price', color='price', title='Average Price per Sector',
                     color_continuous_scale='Viridis')
    st.plotly_chart(fig_bar, use_container_width=True)

    #3D Scatter Plot (Price vs Built-up Area vs Bedrooms) --- 
    st.subheader("🔍 3D Scatter Plot: Price, Built-up Area & Bedrooms")
    
    # Creating a 3D scatter plot using Plotly
    fig_3d = px.scatter_3d(new_df, x='built_up_area', y='price', z='bedRoom',
                           color='property_type', title="Price vs Built-up Area vs Bedrooms",
                           color_continuous_scale='Viridis')
    
    # Customizing layout for 3D plot
    fig_3d.update_layout(
        scene=dict(
            xaxis_title='Built-up Area (sq.ft)',
            yaxis_title='Price (₹)',
            zaxis_title='Bedrooms (BHK)'
        ),
        width=1000, height=700
    )
    
    # Show the plot
    st.plotly_chart(fig_3d, use_container_width=True)


    st.subheader("Sector-wise Property Price Trend Over Time ")
    new_df['month'] = (new_df.index % 12) + 1  # Cyclic months from 1 to 12

    # Group data by sector and month to calculate the average price trend
    price_trend = new_df.groupby(['sector', 'month'], as_index=False)['price'].mean()

    # Create Animated Line Chart
    fig_animated = px.line(
        price_trend, x="sector", y="price", color="sector",
        animation_frame="month", title="📈 Sector-wise Property Price Trend Over Time",
        labels={"price": "Avg Price (₹)", "sector": "Sector"},
        markers=True
    )

    # Show animation in Streamlit
    st.plotly_chart(fig_animated, use_container_width=True)

# --- Data Visualization Section ---
elif section == "📊 Data Visualization":
    st.title("📊 Data Visualization")
    
    st.markdown("---")
    
    # **Property Price Distribution by Property Type (Violin Plot)**
    st.subheader("🏡 Property Price Distribution by Property Type")
    fig_violin = px.violin(new_df, x='property_type', y='price', box=True, points="all", title="Property Price Distribution by Property Type")
    st.plotly_chart(fig_violin, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🏡 Price Distribution per Square Foot (Heatmap)")

    # Grouping data by sector and price per sqft for the heatmap
    price_heatmap_data = new_df.pivot_table(values="price_per_sqft", index="sector", columns="property_type", aggfunc="mean")

    # Create a Plotly heatmap
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=price_heatmap_data.values,
        x=price_heatmap_data.columns,
        y=price_heatmap_data.index,
        colorscale='Viridis',  # You can change this to any other colorscale
        colorbar=dict(title='Price per Sqft'),
    ))

    # Update layout for better aesthetics
    fig_heatmap.update_layout(
        title="Price Distribution per Square Foot",
        xaxis_title="Property Type",
        yaxis_title="Sector",
        height=600,
        width=1000,
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    st.markdown("---")
    
    # Property Price Distribution by Sector
    st.subheader("📊 Price Distribution by Sector")
    fig_box = px.box(new_df, x='sector', y='price', color='sector', title='Price Distribution Across Sectors')
    st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("---")
    
    # Price vs Built-up Area Scatter Plot
    st.subheader("📉 Price vs Built-up Area")
    fig_scatter = px.scatter(new_df, x="built_up_area", y="price", color="property_type", title="Price vs Built-up Area", trendline="ols")
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("---")
    
    # Price vs Number of Bedrooms (BHK)
    st.subheader("🛏️ Price vs Number of Bedrooms")
    fig_bhk_scatter = px.scatter(new_df, x="bedRoom", y="price", color="property_type", title="Price vs Number of Bedrooms", trendline="ols")
    st.plotly_chart(fig_bhk_scatter, use_container_width=True)
    
    st.markdown("---")
    
    # Price per Sqft vs Latitude/Longitude (Location Scatter)
    st.subheader("📍 Price per Sqft vs Location")
    fig_loc_scatter = px.scatter(new_df, x="longitude", y="latitude", color="price_per_sqft", size='built_up_area', hover_name="sector",
                                 title="Price per Sqft vs Latitude/Longitude", color_continuous_scale=px.colors.cyclical.IceFire)
    st.plotly_chart(fig_loc_scatter, use_container_width=True)

# --- Insights Section ---
elif section == "🔍 Insights":
    st.title("🔍 Insights")
    
    # BHK Price Comparison Box Plot
    st.subheader("💰 BHK Price Comparison")
    fig_bhk_price = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
    st.plotly_chart(fig_bhk_price, use_container_width=True)
    
    st.markdown("---")
    
    # Side by Side Property Type Price Distribution
    st.subheader("📈 Property Type Price Distribution")
    fig_distplot, ax = plt.subplots(figsize=(10, 4))
    sns.histplot(new_df[new_df['property_type'] == 'house']['price'], label='House', kde=True, color='blue', ax=ax)
    sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat', kde=True, color='red', ax=ax)
    ax.legend()
    st.pyplot(fig_distplot)
    
    st.markdown("---")
    
    # Average Price by Bedroom Count
    st.subheader("🏠 Average Price by BHK")
    avg_price_bhk = new_df.groupby('bedRoom')['price'].mean().reset_index()
    fig_avg_bhk = px.bar(avg_price_bhk, x='bedRoom', y='price', color='price', title='Average Price by BHK')
    st.plotly_chart(fig_avg_bhk, use_container_width=True)
    
    st.markdown("---")
    
    # Price per Sqft by Property Type
    st.subheader("🏡 Price per Sqft by Property Type")
    fig_price_sqft = px.box(new_df, x="property_type", y="price_per_sqft", color="property_type", title="Price per Sqft by Property Type")
    st.plotly_chart(fig_price_sqft, use_container_width=True)

    st.subheader("💡 Cluster Analysis: Price vs. Built-up Area across Sectors")

    # Create a bubble chart to show clusters of properties
    fig_bubble = px.scatter(
        new_df, x="built_up_area", y="price", size="price", color="sector",
        hover_name="sector", title="Property Price Clusters: Built-up Area vs. Price",
        labels={"built_up_area": "Built-up Area (sq.ft)", "price": "Price (₹)"},
        opacity=0.7, size_max=40
    )

    # Improve layout
    fig_bubble.update_layout(
        width=1000, height=600,
        xaxis_title="Built-up Area (sq.ft)",
        yaxis_title="Price (₹)",
        legend_title="Sector"
    )

    # Display the plot
    st.plotly_chart(fig_bubble, use_container_width=True)

    
