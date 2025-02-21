import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- STREAMLIT APP TITLE ----
st.title("Car Sales Analysis Web App")
st.write("Welcome to the car sales data dashboard.")

# ---- NOTEBOOK GOAL ----
st.header("Project Overview")
st.write("""
- **Clean** the dataset (check for duplicates, missing values, and ensure correct data types).
- **Perform statistical analysis** to find key metrics.
- **Visualize insights** using various plots.
""")

# ---- LOAD DATASET ----
st.header("Dataset Overview")

# Upload dataset option (for flexibility)
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    carsDF = pd.read_csv(uploaded_file)
else:
    # Default dataset location (update this path if needed)
    carsDF = pd.read_csv("vehicles_us.csv")

# Display the first few rows
st.write("### Raw Data Preview:")
st.write(carsDF.head())


# ---- FUNCTION FOR DATA ANALYSIS ----
def analyze_data(df):
    st.subheader("Basic Dataset Information")
    buffer = df.info(buf=None)
    st.text(buffer)  # Streamlit does not display df.info() directly, so we print it as text

    st.subheader("Missing Values:")
    st.write(df.isna().sum())

    st.subheader("Duplicate Entries:")
    st.write(df.duplicated().sum())

# ---- RUN DATA ANALYSIS ----
analyze_data(carsDF)


# ---- DATA CLEANING ----
st.header("Data Cleaning")
st.write("Correcting missing values and data types...")

# Data Corrections
carsDF[['model_year', 'cylinders', 'is_4wd', 'odometer']] = (
    carsDF[['model_year', 'cylinders', 'is_4wd', 'odometer']]
    .fillna(0)
    .astype(int)
)
carsDF['paint_color'] = carsDF['paint_color'].fillna('unknown')
carsDF['date_posted'] = pd.to_datetime(carsDF['date_posted'], format='%Y-%m-%d')

st.success("Data Cleaning Complete ✅")


# ---- VISUALIZATIONS ----
st.header("Data Visualizations")

# --- Price Distribution ---
st.subheader("Price Distribution (95th Quantile)")
fig, ax = plt.subplots(figsize=(10,5))
sns.histplot(carsDF['price'], bins=50, kde=True, ax=ax)
ax.set_xlim(0, carsDF['price'].quantile(0.95))
ax.set_xlabel("Price")
ax.set_ylabel("Count")
ax.set_title("Distribution of Car Prices (95th Quantile)")
st.pyplot(fig)

# --- Mileage vs. Price ---
st.subheader("Mileage vs. Price")
fig, ax = plt.subplots(figsize=(10,5))
sns.scatterplot(x=carsDF['odometer'], y=carsDF['price'], ax=ax)
ax.set_xlim(0, carsDF['odometer'].max())
ax.set_xlabel("Mileage (Odometer)")
ax.set_ylabel("Price")
ax.set_title("Mileage vs. Price")
st.pyplot(fig)

# --- Top 10 Most Common Car Brands ---
st.subheader("Top 10 Most Common Car Brands")
fig, ax = plt.subplots(figsize=(10,5))
carsDF['model'].value_counts().head(10).plot(kind='bar', ax=ax)
ax.set_xlabel("Brand")
ax.set_ylabel("Number of Listings")
ax.set_title("Top 10 Most Common Car Brands")
plt.xticks(rotation=45)
st.pyplot(fig)

st.success("Visualization Complete ✅")

# ---- END OF APP ----
st.write("### 🚀 Interactive dashboard ready! Explore the dataset above.")

