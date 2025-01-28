import streamlit as st

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏙️",
    layout="wide"
)

# Centered Title and Introduction with Animation Effect
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color:#004080; font-size: 48px; font-family: 'Arial', sans-serif; animation: fadeIn 2s;">🏡 Gurgaon Real Estate Analytics App</h1>
        <h3 style="color:#008080; font-size: 30px; animation: fadeIn 3s;">🔍 Your AI-Powered Guide to Smart Real Estate Decisions</h3>
        <p style="color:grey; font-size:18px; font-style: italic;">Explore property recommendations, market trends, and price predictions, all in one place. Stay ahead of the curve in Gurgaon real estate!</p>
    </div>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """, unsafe_allow_html=True
)

# 🖼️ Add an Attractive Image
st.image("datasets/front image.png", width=800, caption="Start your real estate journey in Gurgaon today!")

# 📌 Introduction with Icons for Sections
st.markdown(
    """
    ---
    ## 📢 **Why Use This App?**
    In the rapidly growing **Gurgaon real estate market**, making informed decisions is crucial.  
    Whether you are a **homebuyer**, **investor**, or **analyst**, this tool empowers you to:
    - 🏠 **Find the best properties** based on advanced recommendation algorithms.
    - 📊 **Analyze real estate trends** with interactive visualizations.
    - 🤖 **Predict property prices** using AI and machine learning models.
    - 🛠️ **Customize recommendations** by adjusting similarity weights.

    🌟 With this app, you will have an all-in-one solution for making smarter real estate decisions!

    ---
    """
)

# 🎯 **Guide Users on How to Use with Bullet Points and Clear Steps**
st.markdown(
    """
    ## 🚀 **How to Get Started?**
    Getting started is easy! Here's what you need to do:
    
    1. **Navigate through the sidebar** to explore different modules.
    2. **Choose the feature that suits your needs:**
       - 🏡 **Apartment Recommendation**: Personalized property suggestions based on location and facilities.
       - 📈 **Market Analytics**: View Gurgaon’s real estate trends through interactive visualizations.
       - 💰 **Price Prediction**: Estimate future property prices using AI-driven models.
    3. **Interact with the tool** to get valuable insights instantly and make informed decisions!

    🎯 All tools are powered by advanced AI algorithms and real-time data, making your decision-making easier and faster.
    
    ---
    """
)

# 🏆 **Highlight Features with Icons and Bulleted List**
st.markdown(
    """
    ## 🌟 **Key Features at a Glance**
    - ✅ **AI-Powered Apartment Recommendations**  
      - Get personalized suggestions based on location, pricing, and facilities.  
    - ✅ **Data-Driven Market Insights**  
      - View real estate trends through interactive visualizations.  
    - ✅ **Smart Price Prediction**  
      - Estimate future property prices with machine learning models.  
    - ✅ **Customizable Search and Filters**  
      - Adjust similarity weights to fine-tune property recommendations.

    🎯 These features are designed to help you make smarter real estate decisions with confidence!

    ---
    """
)

# 📌 Sidebar Call-to-Action with Additional Information
st.sidebar.success("👈 **Select a module from the sidebar to get started!** \nDiscover recommendations, insights, and predictions.")

# 🔥 **Final Call to Action with Smaller Image**
st.markdown(
    """
    <div style="text-align: center;">
        <h3 style="color:#004080; font-size: 28px; font-family: 'Arial', sans-serif; font-weight: bold; animation: fadeIn 3s;">🎯 Ready to Explore? Select a module from the sidebar! 🎯</h3>
    </div>
    """, unsafe_allow_html=True
)

# Display the image using Streamlit's st.image() instead of HTML, and add a call-to-action
st.image("datasets/banner image.jpg", width=700, caption="Explore Gurgaon Real Estate with Confidence!")

# Add additional footer with contact information or additional CTA
st.markdown(
    """
    ---
    ## 📬 **Contact Us**
    Have questions or need support? Reach out to us at:
    - 📧 Email: **abhaysingh71711@gmail.com**

    --- 
    ## 🔗 **Follow Us on Social Media**  
    Stay updated with the latest new projects, trends, and data science listings:
    - 📱 **Instagram**: @ezatom_
    - 💼 **LinkedIn**: https://www.linkedin.com/in/abhay-singh-050a5b293/
    - 🐦 **Twitter**: https://x.com/AbhaySingh71711

    """
)
