import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download NLTK data (only needs to be done once)
nltk.download('vader_lexicon')

# Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Load survey data
def load_data(file_path):
    """Load survey feedback from a CSV or Excel file."""
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
        else:
            print("Unsupported file format. Use CSV or Excel.")
            return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# Analyze sentiment
def analyze_sentiment(feedback):
    """Analyze sentiment of feedback text."""
    sentiments = []
    for comment in feedback:
        if pd.notna(comment):  # Ignore NaN values
            sentiment = sia.polarity_scores(comment)
            sentiments.append(sentiment)
        else:
            sentiments.append({'pos': 0, 'neu': 0, 'neg': 0, 'compound': 0})
    return pd.DataFrame(sentiments)

# Create word cloud
def generate_wordcloud(feedback):
    """Generate a word cloud from feedback text."""
    text = ' '.join(comment for comment in feedback if pd.notna(comment))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Feedback")
    plt.show()

# Main function
def main():
    file_path = input("Enter the path to your survey data (CSV/Excel): ")
    data = load_data(file_path)

    if data is not None:
        # Assume there's a 'Feedback' column in the data
        feedback_column = input("Enter the column name for feedback text: ")
        if feedback_column in data.columns:
            feedback = data[feedback_column]

            # Analyze sentiment
            sentiment_results = analyze_sentiment(feedback)
            data = pd.concat([data, sentiment_results], axis=1)

            # Display summary
            print("\nSentiment Analysis Summary:")
            print(data[['Feedback', 'pos', 'neu', 'neg', 'compound']].head())

            # Generate word cloud
            generate_wordcloud(feedback)

            # Save results
            save_path = input("Enter file name to save results (e.g., 'results.xlsx'): ")
            data.to_excel(save_path, index=False)
            print(f"Results saved to {save_path}")
        else:
            print(f"Column '{feedback_column}' not found in the data.")
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()
