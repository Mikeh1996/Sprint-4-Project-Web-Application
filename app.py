import streamlit as st
import pandas as pd
import plotly.express as px

# ---- LOAD CLEANED DATA ----
carsDF = pd.read_csv("cleaned_used_car_data.csv")

# ---- STREAMLIT APP TITLE ----
st.title("Car Sales Analysis Web App")
st.write("This interactive dashboard provides insights into car sales data. Every chart is filtered by metric for example: Brand or Brand and type.")

# ---- DATASET OVERVIEW ----
st.header("Dataset Overview")
st.write(carsDF.head())

# ---- BAR CHART: MOST POPULAR CARS ----
st.header("Most Popular Cars")
st.write("This chart shows the most listed cars by metric.")

# Checkbox to filter out outliers (unique key)
remove_outliers_bar = st.checkbox("Remove outliers for this chart", value=False, key="outlier_bar")

# Dropdowns for filtering with "All" option
filter_options = ["model_year", "model", "condition", "cylinders", "fuel", "transmission", "type", "paint_color", "is_4wd"]
selected_filters = st.multiselect("Select filters to refine the chart:", filter_options)

# Apply filters dynamically
filtered_data = carsDF.copy()

# Apply outlier removal if checked
if remove_outliers_bar:
    filtered_data = filtered_data[(filtered_data["price"] > 500) & (filtered_data["price"] < filtered_data["price"].quantile(0.99))]

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

# Checkbox to filter out outliers (unique key)
remove_outliers_hist = st.checkbox("Remove outliers for this chart", value=False, key="outlier_hist")

# Dropdowns for filtering with "All" option
histogram_filters = ["brand", "cylinders", "model_year", "fuel", "transmission", "type"]
selected_histogram_filters = st.multiselect("Select filters for days listed histogram:", histogram_filters)

# Apply filters dynamically
filtered_data_hist = carsDF.copy()

# Apply outlier removal if checked
if remove_outliers_hist:
    filtered_data_hist = filtered_data_hist[filtered_data_hist["days_listed"] < filtered_data_hist["days_listed"].quantile(0.99)]

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

# Checkbox to filter out outliers (unique key)
remove_outliers_scatter = st.checkbox("Remove outliers for this chart", value=False, key="outlier_scatter")

# Dropdown to select brand (with "All" option)
brand_options = sorted(carsDF["brand"].dropna().unique().tolist())  # Get unique brands
brand_options.insert(0, "All")  # Add "All" option at the top
selected_brand = st.selectbox("Select a brand:", brand_options)

# Apply filters dynamically
filtered_scatter = carsDF.copy()

# Apply outlier removal if checked
if remove_outliers_scatter:
    filtered_scatter = filtered_scatter[(filtered_scatter["price"] > 500) & (filtered_scatter["price"] < filtered_scatter["price"].quantile(0.99))]
    filtered_scatter = filtered_scatter[filtered_scatter["odometer"] < filtered_scatter["odometer"].quantile(0.99)]

if selected_brand != "All":
    filtered_scatter = filtered_scatter[filtered_scatter["brand"] == selected_brand]

# Create scatterplot
scatter_plot = px.scatter(filtered_scatter, x="odometer", y="price", color="brand",
                          labels={"odometer": "Mileage (Odometer)", "price": "Price"},
                          title=f"Price vs. Mileage ({selected_brand if selected_brand != 'All' else 'All Brands'})")
st.plotly_chart(scatter_plot)
