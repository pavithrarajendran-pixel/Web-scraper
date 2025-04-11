import streamlit as st
import pandas as pd
from gym_scraper import scrape_with_config, simulate_gym_data

st.set_page_config(page_title="Gym Scraper", layout="centered")
st.title("🏋️ Gym Web Scraper Dashboard")

# Option to toggle between real and simulated data
use_simulation = st.sidebar.checkbox("Use Simulated Data", value=False)

if use_simulation:
    df = simulate_gym_data()
    st.info("Using simulated gym data.")
else:
    try:
        df = scrape_with_config()
        st.success("Successfully scraped gym class data!")
    except Exception as e:
        st.error(f"Scraping failed: {e}")
        st.stop()

# Display data
st.subheader("📋 Class Information")
search = st.text_input("Search for a class name")
if search:
    df = df[df['Class Name'].str.contains(search, case=False)]
st.dataframe(df)

# Download option
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Data as CSV", csv, "gym_classes.csv", "text/csv")
