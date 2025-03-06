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
    st.title("Data Visualization Viewer")
    
    options = [
        "Bar chart",
        "Box plot",
        "Scatter plot",
        "Stacked Bar Chart",
        "ANOVA Analysis",
        "Chi-Squared test",
        "Regression analysis"
    ]
    
    selected_option = st.selectbox("Select a visualization:", options)

    selected_option = selected_option.lower().replace(" ", "_")
    
    if selected_option != "anova_analysis":
        image_filename = selected_option.lower() + ".png"
        text_filename = selected_option.lower() + "_interpretation.txt"
        
        image_path = os.path.join("data_analysis", selected_option, image_filename)
        text_path = os.path.join("data_analysis", selected_option, text_filename)
        
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption=f"{selected_option} visualization", use_container_width=True)
        else:
            st.warning("Image not found.")
        
        interpretation = load_interpretation(text_path)
        if selected_option == "regression_analysis":
            st.code(f"""Interpretation: {interpretation}""", language="text")
            st.info("This is rendered as a code block as the formatting is not supported by Streamlit's st.write() method.")
        else:
            st.write(f"""**Interpretation:** {interpretation}""")

    elif selected_option == "anova_analysis":
        st.image(os.path.join("data_analysis", "anova_analysis", "anova_plot_ERvsUNI.png"))
        st.image(os.path.join("data_analysis", "anova_analysis", "anova_plot_ERvsDC.png"))

if __name__ == "__main__":
    main()
