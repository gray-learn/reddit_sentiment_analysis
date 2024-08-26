import argparse
from src.data_collection import collect_data_from_subreddits, fetch_data_from_url
from src.data_preprocessing import prepare_data
from src.sentiment_analysis import process_data
from src.visualization import visualize_sentiment_distribution, visualize_sentiment_by_subreddit

def analyze_subreddits():
    # Collect data
    print("Collecting data from Reddit...")
    data = collect_data_from_subreddits()
    
    # Preprocess data
    print("Preprocessing data2...")
    data = prepare_data(data)
    
    # Perform sentiment analysis
    print("Analyzing sentiment...")
    data = process_data(data)
    
    # Visualize results
    print("Generating visualizations...")
    visualize_sentiment_distribution(data)
    visualize_sentiment_by_subreddit(data)
    
    # Save results
    data.to_csv('data/sentiment_results.csv', index=False)
    print("Analysis complete. Results saved in the data directory.")

def analyze_url(url):
    # Fetch data from URL
    print(f"Fetching data from {url}...")
    post_data, comments_data = fetch_data_from_url(url)
    
    # Preprocess data
    print("Preprocessing data1...")
    post_data = prepare_data(post_data)
    comments_data = prepare_data(comments_data)
    
    # Perform sentiment analysis
    print("Analyzing sentiment...")
    post_data = process_data(post_data)
    comments_data = process_data(comments_data)
    
    # Print results
    print("\nPost Sentiment:")
    print(post_data[['title', 'sentiment', 'explanation']])
    
    print("\nComments Sentiment Summary:")
    print(comments_data['sentiment'].value_counts(normalize=True))
    
    # Save results
    post_data.to_csv('data/post_sentiment.csv', index=False)
    comments_data.to_csv('data/comments_sentiment.csv', index=False)
    print("Analysis complete. Results saved in the data directory.")

def main():
    parser = argparse.ArgumentParser(description="Reddit Sentiment Analysis")
    parser.add_argument("--url", help="Analyze a specific Reddit post URL")
    args = parser.parse_args()

    if args.url:
        analyze_url(args.url)
    else:
        analyze_subreddits()

if __name__ == "__main__":
    main()