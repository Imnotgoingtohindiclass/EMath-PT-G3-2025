import os

def create_folders(main_folder):
    subfolders = [
        "bar_chart",
        "box_plot",
        "scatter_plot",
        "stacked_bar_chart",
        "anova_analysis",
        "chi-squared_test",
        "regression_analysis"
    ]
    
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
    
    for folder in subfolders:
        path = os.path.join(main_folder, folder)
        os.makedirs(path, exist_ok=True)
        

if __name__ == "__main__":
    create_folders("data_analysis")
