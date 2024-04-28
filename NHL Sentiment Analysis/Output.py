import pandas as pd
from Sentiment import create

def feeling(team='leafs', posts=5):
    df = create(team, posts)
    if df['Sentiment'].mean() > 0 and df['Subjectivity'].mean() > 0.5:
        print("Leafs Fans are happy and delusional today!")
    elif df['Sentiment'].mean() > 0 and df['Subjectivity'].mean() < 0.5:
        print("Leafs Fans are happy and realistic today!")
    elif df['Sentiment'].mean() < 0 and df['Subjectivity'].mean() > 0.5:
        print("Leafs Fans are sad and delusional today!")
    elif df['Sentiment'].mean() < 0 and df['Subjectivity'].mean() < 0.5:
        print("Leafs Fans are sad and realistic today!")
    else:
        print("Leafs Fans are don't know how to feel today!")