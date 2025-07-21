import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("CArbon Emissions in Kenya Over the Years")

# Upload CSV
uploaded_file = st.file_uploader("C:\\Users\\hi\\Downloads\\cleaned_energy_dataset_final.csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File successfully uploaded!")

    # Show dataset
    st.subheader("Raw Dataset")
    st.write(df)
    df["year"] = df["year"].astype(str).str.replace('"', '').str.strip()
    df["year"] = pd.to_numeric(df["year"], errors='coerce')
    df = df.dropna(subset=["year"])
    df["year"] = df["year"].astype(int)

    # Filter by Year Range
    years = df["year"]
    min_year, max_year = int(years.min()), int(years.max())
    start_year, end_year = st.slider("Select Year Range", min_value=min_year, max_value=max_year, value=(min_year, max_year))

    filtered_df = df[(df["year"] >= start_year) & (df["year"] <= end_year)]

    # Line Chart
    st.subheader("GHG Emissions Trend")
    fig, ax = plt.subplots()
    ax.plot(filtered_df["year"], filtered_df["ghg_emissions"], marker='o')
    ax.set_xlabel("year")
    ax.set_ylabel("CARBON Emissions")
    ax.set_title("CARBON EMISSIONS vs year")
    st.pyplot(fig)

    # Download Filtered Data
    st.download_button("Download Filtered Data", filtered_df.to_csv(index=False), file_name="filtered_emissions.csv")
