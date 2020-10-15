from textblob import TextBlob
from vader_sentiment.vader_sentiment import SentimentIntensityAnalyzer


def get_sentiment(sentence):
    sentence = str(sentence)
    blob = TextBlob(sentence)
    return blob.sentiment


def get_sentiment_vader(sentence):
    if sentence is None or sentence == "":
        vs = {"pos": 0, "neg": 0, "neu": 0}
    else:
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(sentence)
    return vs