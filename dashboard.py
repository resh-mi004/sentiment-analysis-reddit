import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("reddit_vader_sentiment.csv")

# Page title
st.title("📊 Reddit Sentiment Analysis Dashboard")

# Show data preview
st.write("### Sample Data")
st.dataframe(df.head())

# Count sentiment categories
sentiment_counts = df["VADER Sentiment"].value_counts()

# Plot sentiment distribution
st.write("### Sentiment Distribution")
fig, ax = plt.subplots()
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, ax=ax, palette="viridis")
ax.set_xlabel("Sentiment")
ax.set_ylabel("Count")
st.pyplot(fig)

# Word Cloud (if text data exists)
from wordcloud import WordCloud

st.write("### Word Cloud of Reddit Posts")
text = " ".join(post for post in df["Post Title"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

st.write("🚀 **Project by Reshmika S** - Built using Python & Streamlit")
