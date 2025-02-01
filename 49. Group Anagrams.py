class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord("a")]+=1
            freq = tuple(freq)
            anagrams[freq] = [word] if freq not in anagrams else anagrams[freq]+[word]
        ret = []
        for freq, words in anagrams.items():
            ret.append(words)
        return ret
        