scores = {'A': 1,'B': 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7,
          'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
          'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21,
          'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

string = input()
s = 0

for char in string:
    s += scores[char]

def findCombo(target, nums, index, diff) -> list:
    combo = []
    if diff < target:
        diff += nums[index]
        combo.append(nums[index])
    


