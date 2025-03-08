import os
import streamlit as st
from PIL import Image

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
    | **Descriptive Statistics** | • Mean<br>• Median<br>• Standard deviation<br>• Range | Basic statistical measures to understand data distribution |
    | **Inferential Statistics** | • ANOVA<br>• Chi-square tests<br>• Regression analysis | • Compare employment rates by university and degree<br>• Analyse relationships between university and employment status<br>• Study relationship between degree and salary |
    | **Tools** | • Python<br>• Excel | • Statistical analysis and plotting<br>• Data organisation and charts |
    
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
                border: 1px solid transparent;
                border-radius: 5px;
                transition: background-color 0.3s, color 0.3s, border-color 0.3s;  /* Ensure transition for background, color, and border */
            }
            div.stButton > button:hover {
                background-color: #f0f2f6;
                border-color: #f0f2f6;
                color: #333; /* Change text color for visibility */
            }
            div.stButton > button:active {
                background-color: #e0e2e6;
                border-color: #e0e2e6;
                color: #333; /* Change text color for visibility */
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

        if 'page' not in st.session_state:
            st.session_state.page = "Introduction"

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
            options = [
                "Bar chart",
                "Box plot",
                "Scatter plot",
                "Stacked Bar Chart",
                "ANOVA Analysis",
                "Chi-Squared test",
                "Regression analysis"
            ]
            selected_option = st.selectbox("Choose visualisation", options, label_visibility="collapsed")
        
        selected_option = selected_option.lower().replace(" ", "_")
        
        st.markdown("---")
        st.subheader(f"{selected_option.replace('_', ' ').title()} Visualisation")
        
        if selected_option == "anova_analysis":
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
        
        else:
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
                st.image(image_path, caption=f"{selected_option.replace('_', ' ').title()} Visualisation", use_container_width=True)
            else:
                st.warning("Image not found.")
            
            # Display interpretation text
            interpretation = load_interpretation(text_path)
            with st.expander("Interpretation", expanded=True):
                if selected_option == "regression_analysis":
                    st.code(f"""{interpretation}""", language="text")
                    st.warning("This is rendered as a code block due to the formatting constraints of Streamlit's st.write() Method.")
                else:
                    st.write(f"**{interpretation}**")
    
    # Footer
    st.markdown("---")
    st.caption("Designed using Streamlit")

if __name__ == "__main__":
    main()