# Spotify Song Trends & Audio Feature Analysis

A Python-based data analytics project that analyzes Spotify song data to discover music trends, artist performance, genre popularity, album performance, and audio features. The project includes an interactive Streamlit dashboard with KPIs, filters, business insights, and visualizations.

---

# Project Overview

This project focuses on exploring Spotify song data using Python. It demonstrates the complete data analytics workflow including:

- Data Cleaning
- Data Processing
- Exploratory Data Analysis (EDA)
- Business Insights
- Interactive Dashboard Development

The dashboard enables users to interactively explore Spotify data through filters, charts, KPIs, and downloadable datasets.

---

# Features

### Dashboard

- Professional Spotify-themed UI
- Interactive Sidebar Filters
- KPI Cards
- Business Insights
- Responsive Layout

### Filters

- Genre Filter

### Key Performance Indicators (KPIs)

- 🎵 Total Songs
- 🎤 Total Artists
- 💿 Total Albums
- ⭐ Average Popularity

### Charts

- Top 10 Artists by Number of Songs
- Genre Distribution
- Songs Released Per Year
- Popularity vs Danceability
- Average Energy by Genre
- Top 10 Albums by Popularity

### Dataset

- Interactive Data Table
- Download Dataset as CSV

---
# Dashboard Screenshots

## Dashboard Home

Displays the dashboard title, KPIs, and business overview.

<p align="center">
  <img src="output/dashboard_home.png" width="50%">
</p>

---

##  Sidebar Filters

Users can filter songs by genre, and all charts update automatically.

<p align="center">
  <img src="output/Sidebar Filters.png" width="35%">
</p>

---

## 📈 Top Artists & Genre Distribution

Shows the Top 10 Artists by number of songs and the distribution of playlist genres.

<p align="center">
  <img src="output/Top Artists & Genre Distribution.png" width="50%">
</p>

---

## 📉 Release Trend & Popularity Analysis

Shows the number of songs released each year and the relationship between Danceability and Popularity.

<p align="center">
  <img src="output/Release Trend & Popularity Analysis.png" width="50%">
</p>

---

## 🎵 Energy & Album Analysis

Displays the average energy by genre and the Top 10 Albums based on average popularity.

<p align="center">
  <img src="output/Energy & Album Analysis.png" width="50%">
</p>

# 📊 Business Insights

- Queen has the highest number of songs in the dataset.
- Pop is the most popular playlist genre.
- Song releases increased significantly after 2010.
- Danceability has only a moderate relationship with popularity.
- EDM genre has the highest average energy level.
- Popular albums consistently achieve higher average popularity scores.

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- OpenPyXL

---

# 📂 Project Structure

```
Spotify-Song-Trends-and-Audio-Feature-Analysis
│
├── dataset
│   └── spotify_songs.xlsx
│
├── output
│   ├── dashboard_home.png
│   ├── sidebar.png
│   ├── charts_1.png
│   ├── charts_2.png
│   └── charts_3.png
│
├── source
│   └── spotify_songs.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Spotify-Song-Trends-and-Audio-Feature-Analysis.git
```

Move into the project folder

```bash
cd Spotify-Song-Trends-and-Audio-Feature-Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📈 Future Enhancements

- Artist Filter
- Album Filter
- Language Filter
- Release Year Filter
- Dark/Light Theme Toggle
- Plotly Interactive Charts
- Predict Song Popularity using Machine Learning
- Deploy Dashboard on Streamlit Cloud

---

# 👨‍💻 Developed By

**Gnana Jothi M**

Aspiring Data Analyst
