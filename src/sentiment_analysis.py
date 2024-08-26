import ollama
from src.utils import load_config

config = load_config()

def analyze_sentiment(text):
    prompt = f"Analyze the sentiment of the following text. Classify it as positive, negative, or neutral, and provide a brief explanation:\n\n{text}"
    response = ollama.generate(model=config['ollama']['model'], prompt=prompt)
    
    # Simple parsing of the response
    if 'positive' in response.lower():
        sentiment = 'positive'
    elif 'negative' in response.lower():
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment, response

def process_data(df):
    df['sentiment'], df['explanation'] = zip(*df['processed_text'].apply(analyze_sentiment))
    return df