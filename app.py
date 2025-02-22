import streamlit as st
import pandas as pd
import plotly.express as px

# ---- LOAD CLEANED DATA ----
carsDF = pd.read_csv("cleaned_vehicles_us.csv")

# ---- DATA CLEANING & PREPROCESSING ----
# Ensure 'days_listed' is numeric and fill missing values
carsDF["days_listed"] = carsDF["days_listed"].fillna(0).astype(int)

# Filter out extreme outliers for better visualization (Optional)
carsDF = carsDF[(carsDF["price"] > 500) & (carsDF["price"] < carsDF["price"].quantile(0.99))]
carsDF = carsDF[(carsDF["odometer"] < carsDF["odometer"].quantile(0.99))]

# ---- STREAMLIT APP TITLE ----
st.title("Car Sales Analysis Web App")
st.write("This interactive dashboard provides insights into car sales data.")

# ---- DATASET OVERVIEW ----
st.header("Dataset Overview")
st.write(carsDF.head())

# ---- BAR CHART: MOST POPULAR CARS ----
st.header("Most Popular Cars by Brand")
st.write("This chart shows the most listed car brands.")

# Dropdowns for filtering with "All" option
filter_options = ["model_year", "model", "condition", "cylinders", "fuel", "transmission", "type", "paint_color", "is_4wd"]
selected_filters = st.multiselect("Select filters to refine the chart:", filter_options)

# Apply filters dynamically with "All" option
filtered_data = carsDF.copy()
for col in selected_filters:
    options = sorted(filtered_data[col].dropna().unique().tolist())  # Get unique values
    options.insert(0, "All")  # Add "All" option at the top
    selected_values = st.multiselect(f"Select {col}:", options, default="All")

    if "All" not in selected_values:
        filtered_data = filtered_data[filtered_data[col].isin(selected_values)]

# Get brand counts and reset index
brand_counts = filtered_data["brand"].value_counts().reset_index()
brand_counts.columns = ["brand", "count"]  # Renaming columns for clarity

# Create the bar chart
bar_chart = px.bar(brand_counts, 
                   x="brand", 
                   y="count", 
                   labels={"brand": "Brand", "count": "Number of Listings"},
                   title="Most Popular Car Brands")

st.plotly_chart(bar_chart)

# ---- HISTOGRAM: DAYS LISTED ----
st.header("Days Listed Histogram")
st.write("This chart shows how long cars remain listed before being sold.")

# Dropdowns for filtering with "All" option
histogram_filters = ["brand", "cylinders", "model_year", "fuel", "transmission", "type"]
selected_histogram_filters = st.multiselect("Select filters for days listed histogram:", histogram_filters)

# Apply filters dynamically with "All" option
filtered_data_hist = carsDF.copy()
for col in selected_histogram_filters:
    options = sorted(filtered_data_hist[col].dropna().unique().tolist())  
    options.insert(0, "All")  
    selected_values = st.multiselect(f"Select {col}:", options, default="All")

    if "All" not in selected_values:
        filtered_data_hist = filtered_data_hist[filtered_data_hist[col].isin(selected_values)]

# Create histogram
histogram = px.histogram(filtered_data_hist, x="days_listed", nbins=30,
                         labels={"days_listed": "Days Listed"},
                         title="Distribution of Days Listed")
st.plotly_chart(histogram)

# ---- SCATTERPLOT: PRICE VS ODOMETER ----
st.header("Price vs. Mileage")
st.write("This scatterplot examines the relationship between price and mileage.")

# Create scatterplot
scatter_plot = px.scatter(carsDF, x="odometer", y="price", color="brand",
                          labels={"odometer": "Mileage (Odometer)", "price": "Price"},
                          title="Price vs. Mileage Scatterplot")
st.plotly_chart(scatter_plot)
