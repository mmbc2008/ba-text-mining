import json

file = open('Tweets.txt', 'r')
tweets_data = [line.strip() for line in file]
file.close()

while '' in tweets_data:
    tweets_data.remove('')
for i in range(len(tweets_data)):
    if tweets_data[i].isspace():
        tweets_data.remove(tweets_data[i])

text_data = tweets_data[::3]
hyperlinks = tweets_data[1::3]
sentiment = tweets_data[2::3]

for ind, sent in enumerate(sentiment):
    if sent == 'P':
        sentiment[ind] = 'positive'
    elif sent == 'N':
        sentiment[ind] = 'negative'
    elif sent == 'NL':
        sentiment[ind] = 'neutral'
    else:
        print('error')

for ind,link in enumerate(hyperlinks):
    hyperlinks[ind] = link[link.find('http'):link.find(">")-1]




with open('my_tweets.json', 'r') as f:
    file_data = json.load(f)
    for i in range(1,51):
        file_data[str(i)]["text_of_tweet"] = text_data[i-1]
        file_data[str(i)]["tweet_url"] = hyperlinks[i-1]
        file_data[str(i)]["sentiment_label"] = sentiment[i-1]

with open('my_tweets.json', "w") as outfile:
    json.dump(file_data, outfile)

f.close()
outfile.close()

