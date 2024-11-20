class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n, m = len(ransomNote), len(magazine)

        if n > m:
            return False
        
        magazineMapping = {}

        for char1 in magazine:
            if char1 not in magazineMapping.keys():
                magazineMapping[char1] = 1
            else:
                magazineMapping[char1] += 1
        
        for char2 in ransomNote:
            if char2 not in magazineMapping.keys():
                return False

            if char2 in magazineMapping.keys():
                magazineMapping[char2] -= 1
            
            if magazineMapping[char2] < 0:
                return False
        
        return True
            

"""
n, m = len(ransomNote), len(magazine)

if (n > m):
    return false

magazineMapping = {}

for character in magazine:
    if character not in magazineMapping.keys():
        magazineMapping[character] = 1
    else:
        magazineMapping[character] += 1

for char2 in ransomNote:
    if char2 in magazineMapping.keys():
        magazineMapping[char2] -= 1
    if magazineMapping[char2] < 0:
        return false

return true
"""
