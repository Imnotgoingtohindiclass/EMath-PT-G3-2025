import os
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

def load_interpretation(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    return "Interpretation file not found."

def main():
    st.title("📊 Data Visualization Viewer")
    
    # Sidebar with a styled selection box
    with st.sidebar:
        st.header("🔍 Select Visualization")
        options = [
            "Bar chart",
            "Box plot",
            "Scatter plot",
            "Stacked Bar Chart",
            "ANOVA Analysis",
            "Chi-Squared test",
            "Regression analysis"
        ]
        selected_option = st.selectbox("", options)
    
    selected_option = selected_option.lower().replace(" ", "_")
    
    st.markdown("---")
    st.subheader(f"📈 {selected_option.replace('_', ' ').title()} Visualization")
    
    if selected_option != "anova_analysis":
        # Special handling for chi-squared test
        if selected_option == "chi-squared_test":
            image_filename = "chi-squared_test_plot.png"
            text_filename = "chi-squared_test_interpretation.txt"
            dir_name = "chi-squared_test"
        else:
            image_filename = selected_option + ".png"
            text_filename = selected_option + "_interpretation.txt"
            dir_name = selected_option
        
        image_path = os.path.join("data_analysis", dir_name, image_filename)
        text_path = os.path.join("data_analysis", dir_name, text_filename)
        
        # Display image with better formatting
        if os.path.exists(image_path):
            st.image(image_path, caption=f"{selected_option.replace('_', ' ').title()} Visualization", use_container_width=True)
        else:
            st.warning("⚠️ Image not found.")
        
        # Display interpretation text
        interpretation = load_interpretation(text_path)
        with st.expander("📜 Interpretation", expanded=True):
            if selected_option == "regression_analysis":
                st.code(f"""{interpretation}""", language="text")
                st.warning("💡 This is rendered as a code block due to the formatting constraints of Streamlit's st.write() Method.")
            else:
                st.write(f"**{interpretation}**")
    
    elif selected_option == "anova_analysis":
        col1, col2 = st.columns(2)
        with col1:
            st.image(os.path.join("data_analysis", "anova_analysis", "anova_plot_ERvsUNI.png"), caption="ER vs UNI")
        with col2:
            st.image(os.path.join("data_analysis", "anova_analysis", "anova_plot_ERvsDC.png"), caption="ER vs DC")

if __name__ == "__main__":
    main()
