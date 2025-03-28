from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Load the IT-filtered dataset
df = pd.read_csv("filtered_IT_sentiment.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Compute sentiment scores
df["Sentiment Score"] = df["Post Title"].apply(lambda x: analyzer.polarity_scores(x)["compound"])

# Categorize sentiment
df["Sentiment"] = df["Sentiment Score"].apply(lambda x: "Positive" if x > 0.05 else "Negative" if x < -0.05 else "Neutral")

# Save results
df.to_csv("IT_sentiment_analysis.csv", index=False)
print("IT market sentiment analysis completed! Results saved to 'IT_sentiment_analysis.csv'")
