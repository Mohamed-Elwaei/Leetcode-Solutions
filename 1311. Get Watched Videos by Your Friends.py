import heapq
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        group = set()
        
        visited = set()
        queue = deque([(id,0)])
        while queue:
            curr,currLvl= queue.popleft()
            visited.add(curr)
            if currLvl == level:
                group.add(curr)
            else:
                for friend in friends[curr]:
                    if friend not in visited:
                        queue.append((friend,currLvl + 1))
                        visited.add(friend)
        freq = dict()

        for guy in group:
            for video in watchedVideos[guy]:
                freq[video] = freq.get(video,0) + 1
        
        answer = []
        heap = []
        for video in freq:
            heapq.heappush(heap, (freq[video],video))
        while heap:
            answer.append(heapq.heappop(heap)[1])
        return answer