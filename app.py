import os
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Configure the page layout
st.set_page_config(page_title="Graduate Employment Analysis", layout="wide")

# this function loads the interpretation text
def load_interpretation(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    return "Interpretation file not found."

def show_introduction():
    st.title("1. Introduction")
    st.markdown("""
    ### 1.1 Purpose and Rationale
    
    In a world filled with uncertainty, students face the reality of changing trends in the market, with 40% 
    of students having no clear career plan (OECD, 2024). One such trend is artificial intelligence, which 
    is well on track to replace humans, especially in routine-based sectors such as manufacturing and 
    data entry. This makes a future-proof job like a needle in a haystack to have. Consequently, securing 
    such a job is ever more pertinent.

    Thus, with the increase and decline in popularity and demand of specific industries, their related 
    degree courses would follow suit, having a statistically significant impact on students' employment. 
    We aim to uncover which degrees have the most significant impact using descriptive statistics, 
    inferential statistics, and Python to analyse the data, whether positive or negative, on the employment 
    of students.
    
    ### 1.2 Guiding Questions
    
    To what extent does the choice of degree impact their employment? Which degree fields have the 
    highest and lowest employment rates? Is there a significant relationship between degree type and 
    employment status? By addressing these questions, we aim to provide insights to help students make 
    informed decisions about their education and career paths, improving their employability in an 
    increasingly competitive job market.
    """)

def show_problem_statement():
    st.title("2. Problem Statement")
    
    st.markdown("""
    ### GRASPS Framework
    
    | Component | Description |
    |-----------|-------------|
    | **Goal** | Your task is to analyse the impact of the university and degree course on the employment rates of their graduates in Singapore. The goal is to identify trends and relationships that can guide students into make informed decisions about their education and future careers. |
    | **Role** | You are a statistician working for MOE. You have been asked to analyse graduate employment outcomes from Singapore universities. Your job is to perform statistical analysis and present findings through a report and poster. |
    | **Audience** | The target audience is students. With the ever-changing industry, finding a future safe job will become more and more difficult as you do not know the industries that will rise and the industries that will fall. You need to convince them to use your data-driven insights to help choose degree programmes. |
    | **Situation** | The context you find yourself in is the changing job market in Singapore. The challenge involves dealing with analysing large datasets, identifying patterns, and ensuring that the insights are accurate and meaningful. |
    | **Product** | You will create a report and poster in order to summarise your findings. |
    | **Standards** | Your analysis must include descriptive statistics and inferential statistics (ANOVA, chi-square tests, and regression analysis). Your graphical representations must be clear and well-labelled. Your final product should be well-organised, visually appealing, and have no errors. |
    """)

def show_methodology():
    st.title("3. Methodology")
    
    st.markdown("""
    ### Variable Description
    
    | Independent Variables | Dependent Variables | Relationship Analysis |
    |---------------------|-------------------|---------------------|
    | **University** | **Overall employment rate** | Compare employment rates across universities for same degree programmes |
    | **University** | **Full-time employment rate** | Analyse impact of university choice on full-time employment prospects |
    | **University** | **Mean monthly salary** | Evaluate salary differences between universities for similar programmes |
    | **Degree course** | **Overall employment rate** | Compare employment rates between different degree programmes |
    | **Degree course** | **Full-time employment rate** | Analyse which degrees lead to better full-time employment |
    | **Degree course** | **Mean monthly salary** | Evaluate salary potential across different degree programmes |
    
    ### Statistical Methods and Tools
    
    | Category | Methods/Tools | Purpose |
    |----------|---------------|----------|
    | **Descriptive Statistics** | • Mean • Median  • Standard deviation  • Range | Basic statistical measures to understand data distribution |
    | **Inferential Statistics** | • ANOVA  • Chi-square tests  • Regression analysis | • Compare employment rates by university and degree  • Analyse relationships between university and employment status  • Study relationship between degree and salary |
    | **Tools** | • Python  • Excel | • Statistical analysis and plotting  • Data organisation and charts |
    
    ### Assumptions
    
    | Assumption | Details |
    |------------|----------|
    | **Data Quality** | The data used is accurate and unbiased |
    | **External Factors** | Other factors, such as personal connections, may influence employment but are not explicitly measured |
    """)

def main():
    # Add a navigation menu in the sidebar
    with st.sidebar:
        st.title("Navigation")
        
        # Custom CSS to style the buttons
        st.markdown("""
            <style>
            div.stButton > button {
                width: 100%;
                text-align: left;
                padding: 10px 15px;
                margin-bottom: 10px;
                background-color: transparent;
                font-size: 16px;
                border: none;
                border-radius: 5px;
                transition: background-color 0.3s color 0.3s
            }
            div.stButton > button:hover {
                background-color: #f0f2f6;
                border-color: #f0f2f6;
                transition: background-color 0.3s color 0.3s
            }
            div.stButton > button:active {
                background-color: #e0e2e6;
                border-color: #e0e2e6;
            }
            </style>
        """, unsafe_allow_html=True)
        
        # Navigation buttons
        if st.button("Introduction"):
            st.session_state.page = "Introduction"
        if st.button("Problem Statement"):
            st.session_state.page = "Problem Statement"
        if st.button("Methodology"):
            st.session_state.page = "Methodology"
        if st.button("Data Visualisations"):
            st.session_state.page = "Data Visualisations"
        
        # Initialize session state if not exists
        if 'page' not in st.session_state:
            st.session_state.page = "Introduction"
    
    # Display the selected page
    if st.session_state.page == "Introduction":
        show_introduction()
    elif st.session_state.page == "Problem Statement":
        show_problem_statement()
    elif st.session_state.page == "Methodology":
        show_methodology()
    else:  # Data Visualizations
        # Original visualization code
        st.title("Data Visualisation Viewer")
        
        # Sidebar with a styled selection box
        with st.sidebar:
            st.header("Select Visualisation")
            
            # Create categories for visualizations
            visualization_categories = {
                "Descriptive Analysis": [
                    "Bar chart - Employment by Degree",
                    "Box plot - Salary by Degree",
                    "Scatter plot - Employment vs Salary",
                    "Stacked Bar - Employment Types",
                    "University Salary - Comparison",
                    "Uni × Degree - Salary Heatmap",
                    "Employment - By University",
                    "Uni vs Degree - Salary Impact"
                ],
                "Inferential Analysis": [
                    "ANOVA - Employment Rate Differences",
                    "Chi-Squared - Employment Distribution",
                    "Regression - Employment vs Salary"
                ]
            }
            
            # First, select the category
            category = st.radio("Select Analysis Type:", list(visualization_categories.keys()))
            
            # Then, select the visualization within that category
            selected_option = st.selectbox(
                "Choose visualisation:", 
                visualization_categories[category],
                label_visibility="collapsed"
            )
            
            # Extract the base name without the description
            base_option = selected_option.split(" - ")[0]
            
            # Get the description part
            description = selected_option.split(" - ")[1] if " - " in selected_option else ""
            
        # Convert the selected option to the format used in file paths
        selected_option_path = base_option.lower().replace(" ", "_")
        
        st.markdown("---")
        st.subheader(f"{base_option} Visualisation")
        st.caption(f"Investigating: {description}")
        
        # Map the new option names to the original file paths
        option_to_path = {
            "bar_chart": "bar_chart",
            "box_plot": "box_plot",
            "scatter_plot": "scatter_plot",
            "stacked_bar": "stacked_bar_chart",
            "university_salary": "university_salary_comparison",
            "uni_×_degree": "university_×_degree_salary_heatmap",
            "employment": "employment_by_university",
            "uni_vs_degree": "university_vs_degree_impact",
            "anova": "anova_analysis",
            "chi-squared": "chi-squared_test",
            "regression": "regression_analysis"
        }
        
        # Get the correct path for the selected option
        file_path = option_to_path.get(selected_option_path, selected_option_path)
        
        if file_path == "anova_analysis":
            col1, col2 = st.columns(2)
            
            with col1:
                anova1_path = os.path.join("data_analysis", "anova_analysis", "anova_plot_ERvsUNI.png")
                if os.path.exists(anova1_path):
                    st.image(anova1_path, caption="ANOVA: ER vs UNI", use_container_width=True)
                else: 
                    st.warning("Image not found.")
            
            with col2:
                anova2_path = os.path.join("data_analysis", "anova_analysis", "anova_plot_ERvsDC.png")
                if os.path.exists(anova2_path):
                    st.image(anova2_path, caption="ANOVA: ER vs DC", use_container_width=True)
                else:
                    st.warning("Image not found.")
        
        # Handle new visualization types
        elif file_path == "university_salary_comparison":
            image_path = os.path.join("data_analysis", "bar_chart", "university_salary_comparison.png")
            text_path = os.path.join("data_analysis", "bar_chart", "university_salary_interpretation.txt")
            
            if os.path.exists(image_path):
                st.image(image_path, caption="Mean Salary by University", use_container_width=True)
            else:
                st.warning("University salary comparison image not found. Please run the code to generate this visualization first.")
            
            # Display interpretation text
            interpretation = load_interpretation(text_path)
            with st.expander("Interpretation", expanded=True):
                st.write(f"**{interpretation}**")
                
        elif file_path == "university_×_degree_salary_heatmap":
            image_path = os.path.join("data_analysis", "heatmap", "university_degree_salary_heatmap.png")
            text_path = os.path.join("data_analysis", "heatmap", "university_degree_salary_heatmap_interpretation.txt")
            
            if os.path.exists(image_path):
                st.image(image_path, caption="Mean Salary by University and Degree Category", use_container_width=True)
            else:
                st.warning("University × Degree salary heatmap image not found. Please run the code to generate this visualization first.")
            
            # Display interpretation text
            interpretation = load_interpretation(text_path)
            with st.expander("Interpretation", expanded=True):
                st.write(f"**{interpretation}**")
                
        elif file_path == "employment_by_university":
            image_path = os.path.join("data_analysis", "bar_chart", "university_employment_breakdown.png")
            text_path = os.path.join("data_analysis", "bar_chart", "university_employment_interpretation.txt")
            
            if os.path.exists(image_path):
                st.image(image_path, caption="Employment Breakdown by University", use_container_width=True)
            else:
                st.warning("Employment by university image not found. Please run the code to generate this visualization first.")
            
            # Display interpretation text
            interpretation = load_interpretation(text_path)
            with st.expander("Interpretation", expanded=True):
                st.write(f"**{interpretation}**")
                
        elif file_path == "university_vs_degree_impact":
            image_path = os.path.join("data_analysis", "bar_chart", "university_vs_degree_salary_impact.png")
            text_path = os.path.join("data_analysis", "bar_chart", "university_vs_degree_salary_impact_interpretation.txt")
            
            if os.path.exists(image_path):
                st.image(image_path, caption="University vs Degree Impact on Salary", use_container_width=True)
            else:
                st.warning("University vs Degree impact image not found. Please run the code to generate this visualization first.")
            
            # Display interpretation text
            interpretation = load_interpretation(text_path)
            with st.expander("Interpretation", expanded=True):
                st.write(f"**{interpretation}**")
        
        else:
            # Special handling for chi-squared test
            if file_path == "chi-squared_test":
                image_filename = "chi-squared_test_plot.png"
                text_filename = "chi-squared_test_interpretation.txt"
                dir_name = "chi-squared_test"
            elif file_path == "stacked_bar_chart":
                image_filename = "stacked_bar_chart.png"
                text_filename = "stacked_bar_chart_interpretation.txt"
                dir_name = "stacked_bar_chart"
            else:
                image_filename = file_path + ".png"
                text_filename = file_path + "_interpretation.txt"
                dir_name = file_path
            
            image_path = os.path.join("data_analysis", dir_name, image_filename)
            text_path = os.path.join("data_analysis", dir_name, text_filename)
            
            # Display image with better formatting
            if os.path.exists(image_path):
                st.image(image_path, caption=f"{base_option} Visualisation", use_container_width=True)
            else:
                st.warning("Image not found.")
            
            # Display interpretation text
            interpretation = load_interpretation(text_path)
            with st.expander("Interpretation", expanded=True):
                if file_path == "regression_analysis":
                    st.code(f"""{interpretation}""", language="text")
                    st.warning("This is rendered as a code block due to the formatting constraints of Streamlit's st.write() Method.")
                else:
                    st.write(f"**{interpretation}**")
    
    # Footer
    st.markdown("---")
    st.caption("Designed using Streamlit")

if __name__ == "__main__":
    main()