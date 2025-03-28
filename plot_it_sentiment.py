import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load analyzed sentiment data
df = pd.read_csv("IT_sentiment_analysis.csv")

# Plot sentiment distribution
sns.countplot(x="Sentiment", data=df, palette="coolwarm")
plt.title("Reddit Sentiment Analysis For Tech")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
