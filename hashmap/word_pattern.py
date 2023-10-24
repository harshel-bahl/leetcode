# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:

        hash = {}
        split_s = s.split(" ")
        
        if len(split_s) != len(pattern):
            return False

        for patternI in range(len(pattern)):

            letter = pattern[patternI]
            word = split_s[patternI]
            
            if letter not in hash.keys() and word not in hash.values():
                hash[letter] = word

            elif letter in hash.keys() and hash[letter] == word:
                pass
                
            else: 
                return False
            
        return True

solution = Solution()

print(solution.wordPattern(pattern="abba", s="dog dog dog dog"))