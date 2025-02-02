from math import ceil

def rabinKarp(pattern, text):
    """
    Uses the Rabin-Karp algorithm to check if pattern is a substring of text.
    """
    S = len(pattern)
    T = len(text)
    p = 31
    m = int(1e9 + 7)

    # Precompute powers of p
    p_pow = [1] * max(S, T)
    for i in range(1, max(S, T)):
        p_pow[i] = (p_pow[i-1] * p) % m

    # Compute hash of the pattern
    h_pattern = 0
    for i in range(S):
        h_pattern = (h_pattern + (ord(pattern[i]) - ord('a') + 1) * p_pow[i]) % m

    # Compute hashes of text substrings
    h_text = [0] * (T + 1)
    for i in range(T):
        h_text[i+1] = (h_text[i] + (ord(text[i]) - ord('a') + 1) * p_pow[i]) % m

    # Compare pattern hash with text substring hashes
    for i in range(T - S + 1):
        cur_h = (h_text[i + S] - h_text[i] + m) % m
        if cur_h == (h_pattern * p_pow[i] % m):
            if text[i:i+S] == pattern:
                return True
    return False

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        Our solution must be at least ceil(len(b) / len(a)). 
        a must be repeated enough times to be at least as long as b.
        The answer is either ceil(len(b) / len(a)) or ceil(len(b) / len(a)) + 1.
        """
        A = len(a)
        B = len(b)

        # Determine the minimum number of repetitions needed
        min_repeats = ceil(B / A)
        
        # Check if b is a substring of the repeated a
        repeated_a = a * min_repeats
        if rabinKarp(b, repeated_a):
            return min_repeats

        # Check one more repetition
        repeated_a += a
        if rabinKarp(b, repeated_a):
            return min_repeats + 1

        return -1