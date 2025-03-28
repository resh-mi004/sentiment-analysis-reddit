import pandas as pd

# Load the existing sentiment analysis dataset
df = pd.read_csv("reddit_vader_sentiment.csv")

# Define IT-related keywords
tech_keywords = ["IT", "software", "hiring", "layoffs", "startup", "AI", "cloud", "India", "technology"]


# Filter posts that contain at least one of these keywords
df_filtered = df[df["Post Title"].str.contains("|".join(tech_keywords), case=False, na=False)]

# Save the filtered dataset
df_filtered.to_csv("filtered_IT_sentiment.csv", index=False)

print(f"Filtered dataset saved! Total IT-related posts: {len(df_filtered)}")
