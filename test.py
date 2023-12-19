from twickster import API
from time import sleep

if __name__ == '__main__':
    try:
        api = API()
        api.log('Starting Twitter API Engine')
        api.login() #login

        tweetid = api.getTweetID("https://twitter.com/user/status/1702750653842371060") #accept twitter url as string, returns id of tweet

        tweet = api.readTweet(tweetid) #read tweet, accept tweet id as string, returns object of tweet

        media = [] #initialize media
        medium = api.createMedia("temp.mp4", "tweet_video") #create twitter media, accept 2 parameters, file name path and file type tweet_image for picture and tweet_video for videos
        media.append(medium) #store media in array

        api.createTweet("i love it here!", media=media) #create tweet, accept up to 4 parameters, tweet text, in_reply_to_tweet_id if it is a reply, media array of media ids if it contains a media, attachment_url id of a tweet to quote in tweet
        api.deleteTweet(tweetid) #delete tweet, accept tweet id as string

        api.likeTweet(tweetid) #like tweet, accept tweet id as string
        api.unlikeTweet(tweetid) #unlike tweet, accept tweet id as string

        api.createRetweet(tweetid) #retweet tweet, accept tweet id as string
        api.deleteRetweet(tweetid) #delete retweet tweet, accept tweet id as string

        api.pinTweet(tweetid) #pin tweet to profile, accept tweet id as string
        api.unpinTweet(tweetid) #unpin tweet to profile, accept tweet id as string

        api.createBookmark(tweetid) #add tweet to bookmark, accept tweet id as string
        api.deleteBookmark(tweetid) #remove tweet from bookmark, accept tweet id as string

        api.follow("1324833791974744064") #follow a user, accept user id as string
        api.unfollow("1324833791974744064") #unfollow a user, accept user id as string

        lastfile = open("lastid.txt", "r")
        since_id = int(lastfile.readline())
        lastfile.close()
        while True:
            tweets, since_id = api.getNotifications(since_id)
            lastfile2 = open("lastid.txt", "w")
            lastfile2.write(str(since_id))
            lastfile2.close()
            sleep(10)
            api.log("Completed a batch")
    except Exception as error:
        print("Error", error)