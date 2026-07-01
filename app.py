import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import openpyxl as opx  
from pathlib import Path

st.set_page_config(
    page_title="Spotify Dashboard",
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background-color:#F5F7FA;
}

h1{
color:#191414;
font-weight:bold;
}

h2,h3{
color:#1DB954;
}

div[data-testid="stMetric"]{
background:white;
padding:18px;
border-radius:15px;
box-shadow:0px 3px 12px rgba(0,0,0,0.15);
border-left:8px solid #1DB954;
}

section[data-testid="stSidebar"]{
background:#191414;
}

section[data-testid="stSidebar"] *{
color:white;
}

</style>
""", unsafe_allow_html=True)
col1, col2 = st.columns([1,8])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg",
        width=80
    )

with col2:
    st.title("Spotify Analytics Dashboard")
    st.caption("Music Trends & Audio Feature Analysis")

st.caption(
    f"Last Updated : {pd.Timestamp.now().strftime('%d-%b-%Y %I:%M %p')}"
)

from pathlib import Path

@st.cache_data
def load_data():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(
        BASE_DIR,
        "dataset",
        "spotify_songs.xlsx"
    )

    df = pd.read_excel(file_path)

    df["track_name"] = df["track_name"].astype(str).str.replace("$", "", regex=False)
    df["track_artist"] = df["track_artist"].astype(str)
    df["track_album_name"] = df["track_album_name"].astype(str)
    df["playlist_genre"] = df["playlist_genre"].astype(str)

    if "language" in df.columns:
        df["language"] = df["language"].astype(str)

    df["track_album_release_date"] = pd.to_datetime(
        df["track_album_release_date"],
        errors="coerce"
    )

    df["Year"] = df["track_album_release_date"].dt.year

    return df


spotify = load_data()


st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg",
    width=100
)

st.sidebar.title("Spotify Analytics")

st.sidebar.markdown("---")

st.sidebar.header("Filters")

genre = st.sidebar.multiselect(
    "Genre",
    sorted(spotify["playlist_genre"].dropna().unique()),
    default=sorted(spotify["playlist_genre"].dropna().unique())
)

spotify = spotify[spotify["playlist_genre"].isin(genre)]



st.subheader("Key Performance Indicators")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("🎵 Total Songs", len(spotify))
kpi2.metric("🎤 Artists", spotify["track_artist"].nunique())
kpi3.metric("💿 Albums", spotify["track_album_name"].nunique())
kpi4.metric("⭐ Avg Popularity", round(spotify["track_popularity"].mean(),2))

st.markdown("---")



col1, col2 = st.columns(2)

with col1:

    st.subheader("Top 10 Artists")

    artist = (
        spotify.groupby("track_artist")["track_name"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(8,5))

    ax.barh(artist.index, artist.values)

    ax.set_xlabel("Number of Songs",fontsize=12,fontweight="bold")

    st.pyplot(fig)

with col2:

    st.subheader("Top Genres")

    genre = spotify["playlist_genre"].value_counts()

    fig, ax = plt.subplots(figsize=(6,5))

    ax.pie(
        genre.values,
        labels=genre.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)



col3, col4 = st.columns(2)

with col3:

    st.subheader("Songs Released Per Year")

    yearly = (
        spotify.groupby("Year")["track_name"]
        .count()
    )

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        yearly.index,
        yearly.values,
        marker="o"
    )

    ax.set_xlabel("Year",fontsize=12,fontweight="bold")
    ax.set_ylabel("Songs",fontsize=12,fontweight="bold")

    st.pyplot(fig)

with col4:

    st.subheader("Popularity vs Danceability")

    fig, ax = plt.subplots(figsize=(8,5))

    ax.scatter(
        spotify["danceability"],
        spotify["track_popularity"]
    )

    ax.set_xlabel("Danceability",fontsize=12,fontweight="bold")
    ax.set_ylabel("Popularity",fontsize=12,fontweight="bold")

    st.pyplot(fig)



col5, col6 = st.columns(2)

with col5:

    st.subheader("Average Energy by Genre")

    energy = (
        spotify.groupby("playlist_genre")["energy"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(
        energy.index,
        energy.values
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

with col6:

    st.subheader("Top 10 Albums")

    album = (
        spotify.groupby("track_album_name")["track_popularity"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(8,5))

    ax.barh(
        album.index,
        album.values
    )

    ax.set_xlabel("Average Popularity",fontsize=12,fontweight="bold")

    st.pyplot(fig)
    
# ==============================
# BUSINESS INSIGHTS
# ==============================

st.markdown("---")
st.subheader("📊 Business Insights")

top_artist = (
    spotify.groupby("track_artist")["track_name"]
    .count()
    .sort_values(ascending=False)
    .idxmax()
)

top_genre = spotify["playlist_genre"].value_counts().idxmax()

top_album = (
    spotify.groupby("track_album_name")["track_popularity"]
    .mean()
    .sort_values(ascending=False)
    .idxmax()
)

highest_energy = (
    spotify.groupby("playlist_genre")["energy"]
    .mean()
    .sort_values(ascending=False)
    .idxmax()
)

avg_popularity = round(spotify["track_popularity"].mean(), 2)

st.info(f"""
### Key Findings

🎤 **Top Artist:** **{top_artist}** has the highest number of songs in the dataset.

🎼 **Most Popular Genre:** **{top_genre}** contains the largest number of tracks.

💿 **Highest Rated Album:** **{top_album}** has the highest average popularity.

⚡ **Highest Energy Genre:** **{highest_energy}** has the highest average energy.

⭐ **Average Song Popularity:** **{avg_popularity}**

📈 Songs released after **2015** dominate the dataset, indicating increased digital music production.

💃 Danceability and popularity show a moderate positive relationship, suggesting danceable songs are generally more popular.
""")

st.markdown("---")

# ==============================
# DATASET
# ==============================

st.subheader("📄 Spotify Dataset")

st.dataframe(
    spotify,
    use_container_width=True
)

csv = spotify.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Dataset",
    csv,
    "spotify.csv",
    "text/csv"
)
st.markdown("---")

st.caption(
"""
Developed by **Gnana Jothi**

Spotify Song Trends & Audio Feature Analysis

Python • Pandas • Streamlit • Matplotlib
"""
)