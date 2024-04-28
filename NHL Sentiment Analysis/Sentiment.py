from textblob import TextBlob
import sys
import pandas as pd
from Posts import fetch_posts

def analyze_sentiments(posts):
    results = []
    for post in posts:
        analysis = TextBlob(post)
        sentiment = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        results.append((post, sentiment, subjectivity))
    return results

def create_dataframe(analyzed_posts):
    df = pd.DataFrame(analyzed_posts, columns=['Post', 'Sentiment', 'Subjectivity'])
    return df

def create(subreddit_name, limit):
    try:
        posts = fetch_posts(subreddit_name, limit)
    except:
        print("Error fetching posts.")        
    try:
        analyzed_posts = analyze_sentiments(posts)
    except: 
        print("Error analyzing sentiments.")
        
    df = create_dataframe(analyzed_posts)
    return df
    