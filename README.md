# Sprint-4-Project-Web-Application
Car Sales Analysis Web App
## Inspiration
This project is inspired by my passion for data analysis, digital marketing, and financial markets. Through this project, I aim to refine my Python skills, enhance my ability to manipulate data effectively, and develop a web application that visualizes trends in car sales advertisements.

This project also serves as practice in software engineering tasks, including working with Streamlit, handling datasets, and deploying applications to a cloud service.

## Problem Statement
The used car market is vast, and making sense of trends such as pricing patterns, mileage distribution, and popular car brands can be challenging. This project aims to analyze a dataset of car advertisements, extract key insights, and visualize them interactively through a web-based dashboard.

By doing this, we seek to answer:

* What factors influence a car’s selling price?
* How do mileage and age affect car valuation?
* Which car brands and models are most popular?

## What I leanred from this project
I truly enjoyed learning how to use GitHub, Streamlit, and Render to build and deploy an interactive web application. This project has been an incredible experience, allowing me to apply my skills in a real-world setting. Seeing my work come to life as a fully functional app has been both rewarding and something I’m really proud of.

## Project Execution
1. Setting Up the Environment
Dependencies
To run this project, install the following Python packages:
sh
pip install pandas streamlit plotly altair seaborn numpy

### Data Collection
The dataset used contains real car sales data with attributes like price, model, mileage, and year.
The data is cleaned, structured, and formatted for analysis.

### Exploratory Data Analysis (EDA)
Visualizing key trends using histograms, scatter plots, and bar charts.
Identifying missing values and outliers in the dataset.

### Building the Web App
A Streamlit dashboard is developed to allow interactive exploration of the dataset.
Users can filter and visualize data based on various criteria (e.g., price range, mileage, brand).

### Deployment
The web app is deployed on Render, making it accessible online.
How to Run the Project Locally

Clone the repository:
sh
git clone https://github.com/YOUR-USERNAME/sprint4-project.git
cd sprint4-project

Create a virtual environment and install dependencies:
sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Run the application:
sh
streamlit run app.py
