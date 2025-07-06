class Solution:
    def romanToInt(self, s: str) -> int:
        t = 0
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for a,b in zip(s,s[1:]):
            if roman[a] < roman[b]:
                t -= roman[a]
            else:
                t += roman[a]
        
        return t
    
s = 'IVXLCDMIV'
s = Solution(s)
print(s)

