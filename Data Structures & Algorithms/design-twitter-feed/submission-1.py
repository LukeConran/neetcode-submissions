class ItemWrapper:
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        return self.item[1] > other.item[1]

class Twitter:

    def __init__(self):
        self.followGraph = {}
        self.postGraph = {}
        self.count = 1
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.postGraph:
            self.postGraph[userId].append((tweetId, self.count))
        else:
            self.postGraph[userId] = [(tweetId, self.count)]
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        pos_tweets = []
        if userId in self.followGraph:
            following = self.followGraph[userId]
            following.add(userId)
        else:
            following = set([userId])
        for idol in following:
            if idol in self.postGraph:
                pos_tweets += self.postGraph[idol]
        
        #heapify pos_tweets using tuple[1]
        maxHeap = [ItemWrapper(tweet) for tweet in pos_tweets]
        heapq.heapify(maxHeap)
        # print(maxHeap)

        #return top 10 elements
        res = []
        for i in range(min(10, len(maxHeap))):
            item_wrapper = heapq.heappop(maxHeap)
            res.append(item_wrapper.item[0])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        #might need to put in checks to not allow a user to follow themselves
        if followerId in self.followGraph:
            self.followGraph[followerId].add(followeeId)
        else:
            self.followGraph[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #same checks here
        self.followGraph[followerId].discard(followeeId)
