# importing modules required for tweets scraping
import re
import string
import snscrape.modules.twitter as twitterScraper

# Function to scrape tweets from twitter with the help of snscrape
def getTweets():
    # Query to search for tweets
    query = "कोरोना OR कोभिड OR कोभिड१९ OR भेरोसेल OR कोभिशिल्ड OR फाइजर -filter:links -filter:replies geocode:28.3949,84.1240,1km"
    tweets = []
    limit = 30000
    # Calling the twitter scraper function
    scrapedTweets = twitterScraper.TwitterSearchScraper(query).get_items()
    # Iterating over the scraped tweets and passing them to the initialProcess function
    for i, tweet in enumerate(scrapedTweets):
        if i == limit:
            break
        tweets = initialProcess(tweet.content, tweets)
    return tweets
tweets = getTweets()

# Exporting the tweets to a csv file
with open('1.2-scraped-tweets.csv', 'w', encoding="utf-8") as f:
    for tweet in tweets:
        f.write(tweet + "\n")

# Gets the tweets and tweet from the getTweets function and passes them to the removeImojis and removePunctuation functions and appends them to the tweets list
def initialProcess(tweet, tweets):
    tweet = removeImojis(tweet)
    tweet = removeUnnecessaryContant(tweet)
    if tweet:
        tweets.append(tweet.strip())
    return tweets
       
# defining function to remove emojis nd special characters
def removeImojis(tweet):
    emojiPattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002500-\U00002BEF"  # chinese char
                            u"\U00002702-\U000027B0"
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U0001f926-\U0001f937"
                            u"\U00010000-\U0010ffff"
                            u"\u2640-\u2642" 
                            u"\u2600-\u2B55"
                            u"\u200d"
                            u"\u23cf"
                            u"\u23e9"
                            u"\u231a"
                            u"\ufe0f"  # dingbats
                            u"\u3030"
                           "]+", flags=re.UNICODE)
    return emojiPattern.sub(r'', tweet)

# defining function to remove punctuation
def removeUnnecessaryContant(tweet):
    tweet = tweet.translate(str.maketrans('', '', string.punctuation)).replace('…', '').replace('।', '')
    tweet=re.sub(r"[a-zA-z.'#0-9@,:?'\u200b\u200c\u200d!/&~-]",'',tweet)
    tweet=re.sub(r'[""“”()’:;]…','',tweet)
    tweet=' '.join(tweet.split())
    return tweet




