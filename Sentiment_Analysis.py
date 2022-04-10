import tweepy
from textblob  import  TextBlob

consumer_key="qfP7jT7AgSRvalAk24L2sdafC"
consumer_sec="79Pa1IsdftBk48nuGBuMvSPGpNChhHJ5jXvV12F4Hzg1BsqWAp"

access_key="1300626045104578562-pQT6H7uGMoTcAYxiCsajHCiiOAHbBJ"
access_sec="kE2kZHFOAxmwZfV7ukg56iyidHtYYH1Xu1xiMe3D2uuGa"

first_auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

first_auth.set_access_token(access_key,access_sec)

storage_api_connect=tweepy.API(first_auth,timeout=2)

sea=input("Enter the word you want to search on twitter: ")
numm=int(input("Enter the no. of tweets you want: "))
#numm=numm+1
search_data=[sea]

list_of_tweets=[]

if  len(search_data) == 1 :
  for  tweetdata  in  tweepy.Cursor(storage_api_connect.search,q=search_data[0]+"  -filter:retweets",lang='en',result_type='recent').items(numm):
    list_of_tweets.append(tweetdata.text)
print("#####################################")
print("RESULTS:")
print("#####################################")
#for i in range(1,len(list_of_tweets)):
#  print("Tweet",i,": ",list_of_tweets[i-1])

search_sentiment=[sea]
#list_of_sentiment=[]
z=1
if  len(search_sentiment) >= 1 :
  for  i  in  tweepy.Cursor(storage_api_connect.search,q=search_sentiment[0]+"  -filter:retweets",lang='en',result_type='recent').items(numm):
    analyse=TextBlob(i.text)
    print("Tweet",z,": ",list_of_tweets[z-1])
    print("Its sentiment polarity:",analyse.sentiment.polarity)
    z=z+1
    print(" ")

#end of code
