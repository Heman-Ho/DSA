from collections import deque
import heapq
class Twitter:

    def __init__(self):
        self.queues = [None] * 500
        self.following = [None] * 500
        self.global_clock = 0
        for i in range(500):
            self.following[i] = set()
            self.following[i].add(i+1)
            self.queues[i] = deque()
        
        

    def postTweet(self, userId: int, tweetId: int) -> None: # Add to own queue of size 10 (O(1))

        if len(self.queues[userId-1]) >= 10:
            self.queues[userId-1].popleft()
        self.queues[userId-1].append((self.global_clock, tweetId))
        self.global_clock += 1
        


    def getNewsFeed(self, userId: int) -> List[int]: # Time complexity O(Followers*10*log(F))
        min_heap = []
        
        # For everyone you follow

        for user in self.following[userId-1]:
            # insert their most recent 10 posts into a master min heap based on time posted
            for item in self.queues[user-1]:
                heapq.heappush(min_heap, item)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        ret = [0] * len(min_heap)
        # return the posts in the min_heap
        i = len(ret) - 1
        while min_heap:
            ret[i] = heapq.heappop(min_heap)[1]
            i -= 1
        return ret


    def follow(self, followerId: int, followeeId: int) -> None: # O(1) add to set
        if self.following[followerId - 1] == 0:
            self.following[followerId - 1] = set()
        self.following[followerId - 1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: # O(1) remove from set
        if followeeId in self.following[followerId - 1] and followerId != followeeId:
            self.following[followerId - 1].remove(followeeId)
