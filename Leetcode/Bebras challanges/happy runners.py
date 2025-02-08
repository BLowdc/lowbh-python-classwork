def isHappy(score):
    for i in range(len(score)-1):
        if score[i] >= score[i+1]:
            return 0
    return 1

n = int(input()) 
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

num_happy = 0
for runner in a:
    num_happy += isHappy(runner)

print(num_happy)

            
