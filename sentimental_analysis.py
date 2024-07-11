from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'
'''an article analysis'''
'''from newspaper import Article

url="https://www.ndtv.com/world-news/uk-woman-murdered-parents-lived-with-their-dead-bodies-for-several-years-6034977"
article=Article(url)
article.download()
article.parse()
article.nlp()

text=article.summary
text=article.summary
print(text)'''


'''read a file '''
with open("sentimental_analysis/mytext_s_a.txt", 'r') as f:
    text=f.read()

# blob=TextBlob(text)
# sentiment=blob.sentiment.polarity
print(analyze_sentiment(text))