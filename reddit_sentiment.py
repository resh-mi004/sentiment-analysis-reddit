import praw
import pandas as pd
from textblob import TextBlob
from config import client_id, client_secret, user_agent
reddit = praw.Reddit(
    client_id = "WjX0IzpE3iButfYh7jkf2g",
    client_secret = "LwA_kMpRuIBFwKMg7S7Ytp9iHa5YdA",
    user_agent = "SentimentAnalysisApp/1.0 by Large_Relative1430"

) 
    


subreddit_name = "technology"
subreddit = reddit.subreddit(subreddit_name)

posts=[]
for post in subreddit.hot(limit=50):
    analysis = TextBlob(post.title)
    sentiment_score = analysis.sentiment.polarity
    sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"

    posts.append([post.title, sentiment_score, sentiment_label])
df = pd.DataFrame(posts, columns=["Post Title","Sentiment Score", "Sentiment Label"])
df.to_csv("reddit_sentiment.csv",index=False)
print("Reddit sentiment analysis completed! Data saved to 'reddit_sentiment.csv'.")