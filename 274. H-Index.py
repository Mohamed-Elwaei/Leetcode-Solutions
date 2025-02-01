class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #[3,0,6,1,5] => [6,5,3,1,0]
        #[6,5,3,1] we remove 0 and have 4 elements left. We can get h-index >= 0.
        #[6,5,3]   we remove 1 and have 3 elements left. We can get h-index >= 1.
        #[6,5]     we remove 3 and have 2 elements left. We can not get h-index >= 3

        #[100,19,18,7] h-index = 4.
        #[100,19,18] we remove 7 and have 3 elemens left. We cannot get h-index >= 7.

        #[100,19,18,2] h-index = 3
        #[100,19,18] we remove 2 and have 3 elements left. We can get h-index >= 2.

        #[3,3,3,3]
        # we remove 3 and have 3 elements left. We cannot get a higher h-index
        citations.sort(reverse = True)
        ans = 0
        while citations and citations[-1] < len(citations):
            ans = citations.pop()
        return len(citations)