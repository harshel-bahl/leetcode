# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        note_hash = {}
        for letter in ransomNote:
            if letter not in note_hash.keys():
                note_hash[letter] = 0
            else:
                note_hash[letter] += 1

        magazine_hash = {}
        for letter in magazine:
            if letter not in magazine_hash.keys():
                magazine_hash[letter] = 0
            else:
                magazine_hash[letter] += 1
        
        for letter, value in note_hash.items():
            if letter in magazine_hash.keys() and value <= magazine_hash[letter]:
                pass
            else:
                return False
        
        return True

            
solution = Solution()

print(solution.canConstruct(ransomNote="aa", magazine="aab"))