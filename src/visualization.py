import matplotlib.pyplot as plt

def visualize_sentiment_distribution(data):
    sentiment_counts = data['sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
    plt.title("Overall Sentiment Distribution")
    plt.savefig('data/sentiment_distribution.png')
    plt.close()

def visualize_sentiment_by_subreddit(data):
    sentiment_by_subreddit = data.groupby('subreddit')['sentiment'].value_counts(normalize=True).unstack()
    sentiment_by_subreddit.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title("Sentiment Distribution by Subreddit")
    plt.xlabel("Subreddit")
    plt.ylabel("Proportion")
    plt.legend(title="Sentiment")
    plt.savefig('data/sentiment_by_subreddit.png')
    plt.close()