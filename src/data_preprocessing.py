import re

def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

def prepare_data(df):
    print(df.columns)
    if 'title' in df.columns:
        df['processed_text'] = df['title'] + " " + df['body']
    else:
        df['processed_text'] = df['body']

    # Apply the preprocessing function
    df['processed_text'] = df['processed_text'].apply(preprocess_text)
    return df