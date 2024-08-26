import praw
import pandas as pd
from datetime import datetime
import yaml

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

config = load_config()

reddit = praw.Reddit(
    client_id=config['reddit']['client_id'],
    client_secret=config['reddit']['client_secret'],
    user_agent=config['reddit']['user_agent']
)

def fetch_reddit_data(subreddit_name, time_filter='day', limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    # print(f"Fetching posts from r/{subreddit_name}...")
    # print(subreddit)
    for post in subreddit.top(time_filter=time_filter, limit=limit):
        posts.append({
            'title': post.title,
            'body': post.selftext,
            'score': post.score,
            'created_utc': datetime.fromtimestamp(post.created_utc)
        })
    return pd.DataFrame(posts)

def collect_data_from_subreddits():
    all_data = []
    for subreddit in config['subreddits']:
        data = fetch_reddit_data(
            subreddit,
            time_filter=config['analysis']['time_filter'],
            limit=config['analysis']['posts_limit']
        )
        data['subreddit'] = subreddit
        all_data.append(data)
    return pd.concat(all_data, ignore_index=True)

def fetch_data_from_url(url):
    submission = reddit.submission(url=url)
    post_data = {
        'title': submission.title,
        'body': submission.selftext,
        'score': submission.score,
        'created_utc': datetime.fromtimestamp(submission.created_utc),
        'subreddit': submission.subreddit.display_name,
        'url': url
    }
    
    comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments.append({
            'body': comment.body,
            'score': comment.score,
            'created_utc': datetime.fromtimestamp(comment.created_utc)
        })
    
    return pd.DataFrame([post_data]), pd.DataFrame(comments)