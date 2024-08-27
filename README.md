# Reddit Sentiment Analysis using LLMs

This project uses Large Language Models (LLMs) to perform sentiment analysis on Reddit posts and comments. It can analyze multiple subreddits or a specific Reddit post URL.

## Features

- Collect data from multiple subreddits or a specific Reddit post
- Preprocess text data
- Perform sentiment analysis using locally run LLMs via Ollama
- Visualize sentiment distribution
- Save results to CSV files

## Setup

1. Clone the repository:
   git clone git clone https://github.com/gray-learn/reddit_sentiment_analysis.git
   cd reddit_sentiment_analysis

2. Install required packages:
   pip install -r requirements.txt

   3. Set up Ollama on your local machine with the desired model.

3. Update the `config/config.yaml` file with your Reddit API credentials and desired settings.

## Usage

1. To analyze configured subreddits:
   python main.py

2. To analyze a specific Reddit post URL:

python main.py --url "https://www.reddit.com/r/AskReddit/comments/example_post_id/example_post_title/"

## Output

- Sentiment analysis results are saved in the `data/` directory as CSV files.
- Visualization plots are saved as PNG files in the `data/` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## test

    python main.py --url "https://www.reddit.com/r/askTO/comments/1aocio8/your_toronto_food/"
