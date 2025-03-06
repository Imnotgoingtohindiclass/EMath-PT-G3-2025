import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data (modify this based on your notebook's content)
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

data = load_data()

# Sidebar for user selection
st.sidebar.title("Graph Selector")
graph_option = st.sidebar.selectbox("Choose a graph type:", ["Line Graph", "Bar Chart", "Scatter Plot"])

# Function to generate graphs
def plot_graph(option):
    fig, ax = plt.subplots()
    if option == "Line Graph":
        ax.plot(data["X"], data["Y"], marker='o', linestyle='-')
        st.write("This is a line graph showing trends over time.")
    elif option == "Bar Chart":
        ax.bar(data["X"], data["Y"], color='blue')
        st.write("This bar chart represents categorical data distribution.")
    elif option == "Scatter Plot":
        ax.scatter(data["X"], data["Y"], color='red')
        st.write("This scatter plot visualizes the relationship between variables.")
    
    st.pyplot(fig)

# Display selected graph
st.title("Interactive Graph Viewer")
st.write("Select a graph type from the sidebar to visualize the data.")
plot_graph(graph_option)