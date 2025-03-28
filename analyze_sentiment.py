import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reddit_sentiment.csv")
print("First 5 rows of the dataset:")
print(df.head())
print("\nSentiment distribution:")
print(df["Sentiment Label"].value_counts())
print("\nMost Positive Post:")
print(df.loc[df["Sentiment Score"].idxmax()])

print("\nMost Negative Post:")
print(df.loc[df["Sentiment Score"].idxmin()])

df["Sentiment Label"].value_counts().plot(kind="bar", color=["green", "red", "blue"])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

df["Sentiment Score"].hist(bins=20, edgecolor="black")
plt.title("Distribution of Sentiment Scores")
plt.xlble("Sentiment Score")
plt.ylabel("Frequency")
plt.show()
