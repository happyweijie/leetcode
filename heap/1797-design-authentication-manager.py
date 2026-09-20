import heapq

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.pq = []
        self.tokens = {}
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        """
        Time: log(n), where n is the number of tokens in the priority queue.
        """
        self.tokens[tokenId] = currentTime + self.timeToLive
        heapq.heappush(self.pq, (self.tokens[tokenId], tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        """
        Time: log(n), where n is the number of tokens in the priority queue.
        """
        if tokenId not in self.tokens:
            return

        if self.tokens[tokenId] <= currentTime:
            self.tokens.pop(tokenId)
            return

        self.tokens[tokenId] = currentTime + self.timeToLive
        heapq.heappush(self.pq, (self.tokens[tokenId], tokenId))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        """
        Time: n * log(n), where n is the number of tokens in the priority queue.
        """
        self.removeExpiredTokens(currentTime)

        return len(self.tokens)
        
    def removeExpiredTokens(self, currentTime: int) -> None:
        while self.pq:
            time, token_id = self.pq[0]

            if time > currentTime:
                break

            heapq.heappop(self.pq)

            if token_id in self.tokens and time == self.tokens[token_id]:
                self.tokens.pop(token_id)

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)