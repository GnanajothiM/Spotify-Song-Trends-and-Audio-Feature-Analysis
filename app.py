import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Spotify Dashboard",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 Spotify Song Trends & Audio Feature Analysis")

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


st.sidebar.title("Filters")

genre = st.sidebar.multiselect(
    "Genre",
    sorted(spotify["playlist_genre"].dropna().unique()),
    default=sorted(spotify["playlist_genre"].dropna().unique())
)

spotify = spotify[spotify["playlist_genre"].isin(genre)]



st.subheader("Key Performance Indicators")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Total Songs", len(spotify))
kpi2.metric("Artists", spotify["track_artist"].nunique())
kpi3.metric("Albums", spotify["track_album_name"].nunique())
kpi4.metric("Average Popularity", round(spotify["track_popularity"].mean(),2))

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

    ax.set_xlabel("Number of Songs")

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

    ax.set_xlabel("Year")
    ax.set_ylabel("Songs")

    st.pyplot(fig)

with col4:

    st.subheader("Popularity vs Danceability")

    fig, ax = plt.subplots(figsize=(8,5))

    ax.scatter(
        spotify["danceability"],
        spotify["track_popularity"]
    )

    ax.set_xlabel("Danceability")
    ax.set_ylabel("Popularity")

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

    ax.set_xlabel("Average Popularity")

    st.pyplot(fig)
    
st.markdown("---")

st.subheader("Spotify Dataset")

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