reds = []
with open("AoC2025\\Day9\\test.txt", "r") as f:
    for line in f:
        reds.append(
            tuple([int(coord) for coord in line.strip().split(",")])
        )
reds = tuple(reds)

# main

# n = len(reds)
# max = -1

# for i in range(n):
#     for j in range(i + 1, n):
#         width = abs(reds[i][0] - reds[j][0]) + 1
#         height = abs(reds[i][1] - reds[j][1]) + 1
#         area = width * height
#         if area > max:
#             max = area

# print(max)
