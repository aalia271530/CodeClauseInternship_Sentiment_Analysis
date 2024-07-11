from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

'''read a file '''
with open("sentimental_analysis/mytext_s_a.txt", 'r') as f:
    text=f.read()
    
print(analyze_sentiment(text))
