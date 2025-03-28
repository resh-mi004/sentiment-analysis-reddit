import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("reddit_vader_sentiment.csv")

# Count the occurrences of each sentiment
sentiment_counts = df["VADER Sentiment"].value_counts()

# Plot a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Analysis of Reddit Posts")
plt.show()
