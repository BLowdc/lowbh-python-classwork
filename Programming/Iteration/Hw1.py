l = input()
low = l
up = l
for i in range(4):
    l = input()
    if l > up:
        up = l
    if l < low:
        low = l
print("largest:",up)
print("smallest:",low)