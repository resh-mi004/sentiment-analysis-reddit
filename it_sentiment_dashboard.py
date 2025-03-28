import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the IT-related sentiment data
df = pd.read_csv("IT_sentiment_analysis.csv")

# Title
st.title("📊 Reddit Sentiment Analysis in Tech")

# Pie Chart for Sentiment Distribution
st.subheader("🔹 Sentiment Distribution (Pie Chart)")
sentiment_counts = df["VADER Sentiment"].value_counts()
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=sns.color_palette("viridis", len(sentiment_counts)))
ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Word Cloud
st.subheader("🔹 Word Cloud of IT Posts")
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(df["Post Title"]))
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Display raw data
st.subheader("🔹 IT-Related Posts")
st.dataframe(df)
