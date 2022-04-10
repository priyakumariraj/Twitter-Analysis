import tweepy #An easy-to-use Python library for accessing the Twitter API.
from textblob  import  TextBlob #library which supports complex analysis and operations on textual data.

consumer_key="qfP7jT7AgSRvalAk24L2sdafC" #API key of consumer
consumer_sec="79Pa1IsdftBk48nuGBuMvSPGpNChhHJ5jXvV12F4Hzg1BsqWAp" #API secret key of consumer

access_key="1300626045104578562-pQT6H7uGMoTcAYxiCsajHCiiOAHbBJ" #access token key of consumer
access_sec="kE2kZHFOAxmwZfV7ukg56iyidHtYYH1Xu1xiMe3D2uuGa" #access token secret key of consumer

first_auth=tweepy.OAuthHandler(consumer_key,consumer_sec) # first_auth is a variable in which we store a data which authenticate the consumer key and consumer secret key

first_auth.set_access_token(access_key,access_sec) #in first_auth variable we set access token key and access token secret key.

storage_api_connect=tweepy.API(first_auth,timeout=2) #in this we should relate in  between code and API and timeout=2 is nothing but the time limit to wait on the page

sea=input("Enter the word you want to search on twitter: ") #just a input that we want to search
numm=int(input("Enter the no. of tweets you want: ")) #no. of tweets we want to see we can enter in this integer input
#numm=numm+1 
search_data=[sea] #in search_data varible we store the sea variable in which we search the data 

list_of_tweets=[]#empty list in which we store data later

if  len(search_data) == 1 :#statement only happens when search_databis equal to 1 otherwise not
  for  tweetdata  in  tweepy.Cursor(storage_api_connect.search,q=search_data[0]+"  -filter:retweets",lang='en',result_type='recent').items(numm):
      #for tweetdata in xyz means----we write in other program like----for i in range(5)---so whatever the meaning of i here is the same meaning of tweetdata there
      #
    list_of_tweets.append(tweetdata.text)#after fullfilling all the above condition the variable gets added in empty list that islist of tweet
print("#####################################")
print("RESULTS:")
print("#####################################")
#for i in range(1,len(list_of_tweets)):
#  print("Tweet",i,": ",list_of_tweets[i-1])

search_sentiment=[sea] #just a variable in which we store sea input to find the sentiments of tweets
#list_of_sentiment=[]
z=1
if  len(search_sentiment) >= 1 : #statement only happens when search_sentiments greater than or equal to zero
  for  i  in  tweepy.Cursor(storage_api_connect.search,q=search_sentiment[0]+"  -filter:retweets",lang='en',result_type='recent').items(numm):
    analyse=TextBlob(i.text)
    print("Tweet",z,": ",list_of_tweets[z-1])
    print("Its sentiment polarity:",analyse.sentiment.polarity)#analyse.sentiment.polarity gives the analysis of sentiment polarity of tweets like if its value come 1 or greater than 1 means that tweet have positive effect and if it come 0 it means equal positive and negative sentiments on that tweet like wise for neative also.and
    z=z+1 
    print(" ")

#end of code
