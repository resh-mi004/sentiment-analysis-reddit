import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load Reddit Sentiment Data
df = pd.read_csv("reddit_sentiment.csv")

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Apply VADER Sentiment Analysis
def get_vader_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)['compound']
    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["VADER Sentiment"] = df["Post Title"].apply(get_vader_sentiment)

# Save the new CSV file with VADER results
df.to_csv("reddit_vader_sentiment.csv", index=False)

print("VADER sentiment analysis completed! Data saved to 'reddit_vader_sentiment.csv'.")
