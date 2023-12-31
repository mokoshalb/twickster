# [twickster](#)

<samp>

Unofficial Python Twitter API.

## Why twickster ?

I used the official Twitter API frequently before Elon barricaded the basic access, now we have to pay a shit load of benjamens to hook up the access. So I decided to make something else that still makes the API accessing to me, hence twickster (twitter+trickster morphword).
So if you dont have enough money to use the official twitter API, then this is for you.

### Installation

You need to have twickster installed on your machine to start using it which can either be done directly from **GitHub** or using **pip**.

#### Installing directly

You first need to clone or download the repo to your local directory and then move into the project directory as shown in the example and then run the command below;

```bash
git clone https://github.com/mokoshalb/twickster
cd twickster
twickster > python setup.py install 
....
```

#### Installing from pip

```bash
pip install twickster --upgrade
```

## How to use twickster?


```python
from twickster import API

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

    except Exception as error:
        print("Error", error)
```


Well! thats all for now from the package, to request new feature make an issue.

## Contributions

**twickster** is an open-source package, so contributions are warmly welcome.

When contributing to code please make an issue for that before making your changes so that we can have a discussion before implementation.

## Issues

If you're facing any issue or difficulty with the usage of the package just raise one so that we can fix it as soon as possible.

**Please, be as much comprehensive as possible!** Use as many screenshots and detailed description sets as possible; this will save us some time that we'd dedicate on asking you for "a more detailed descriptiton", and it'll make your request be solved faster.

## Give it a star

Was this useful to you ? Then give it a star so that more people can manke use of this.
</samp>
