"""
Edge Cases
1. What if a user posts the same tweetId twice?
- My interpretation: It will be in the users feed twice,
but time posted will be different

"""
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        All the tweets user posted + all tweets from people
        they are following.
        """
        all_tweets = []
        for tweet in self.tweets[userId]:
            all_tweets.append(tweet)
        for user in self.following[userId]:
            for t in self.tweets[user]:
                all_tweets.append(t)
        all_tweets = sorted(all_tweets, reverse = True, key=lambda x: x[0])
        res = []
        for num in range(10):
            if num +1 > len(all_tweets):
                return res
            res.append(all_tweets[num][1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
