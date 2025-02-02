class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        
        if n < 3: return False
        
        hasVowels = hasConsonants = False
        
        for c in word:
            if c.lower() in 'aeiou':
                hasVowels = 1
                
            elif c.lower() in 'bcdfghjklmnopqrstvwxyz':
                hasConsonants = 1
            
            elif c not in '0123456789':
                return False
        return hasConsonants and hasVowels