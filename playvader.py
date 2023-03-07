# Import the necessary libraries
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import nltk
nltk.download('vader_lexicon')

# Create a new instance of the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Load the CSV file into a pandas dataframe
df = pd.read_csv('vader.csv', encoding='ISO-8859-1')

# Check if 'text' column exists in the dataframe
if 'text' in df.columns:

    # Define a function to calculate sentiment scores for a given text
    def get_sentiment_scores(text):
        if isinstance(text, str):
            scores = analyzer.polarity_scores(text)
        else:
            scores = {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
        return pd.Series(scores)

    # Apply the sentiment analysis function to each cell in the 'text' column of the dataframe
    sentiment_df = df['text'].apply(get_sentiment_scores)

    # Combine the original dataframe with the sentiment scores dataframe
    result_df = pd.concat([df, sentiment_df], axis=1)

    # Export the results to a new Excel file
    result_df.to_excel('vader_output.xlsx', index=False)
else:
    print("Error: 'text' column not found in the input CSV file.")
