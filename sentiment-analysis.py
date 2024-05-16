import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('average_perceptron_tagger')
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

tweets = [
    'I am eating a sandwich',
    'Tesla is awesome!',
    'Starbucks is not good anymore...'
]

scores = []

for tweet in tweets:
    scores.append({ 'tweet': tweet, 'score': sia.polarity_scores(tweet)['compound'] })

print(scores)
