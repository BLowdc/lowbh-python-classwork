def find(n: int) -> list:
    num = 0
    diff = 1
    rows = []
    while num < n * n // 2:
        num += diff
        diff += 1
        rows.append(num)

    return rows


def reduced(rows: list, n: int) -> int:
    return len(rows) * len(rows) + 1 - n


def findRow(rows: list, n: int) -> int:
    for i in range(len(rows)):
        if n <= rows[i]:
            return i + 1


size = int(input())
start = int(input())
end = int(input())

r = find(size)
mid = r[-1]

if start > mid:
    start_row = 2 * size - findRow(r, reduced(r, start))
else:
    start_row = findRow(r, start)

if end > mid:
    end_row = 2 * size - findRow(r, reduced(r, end))
else:
    end_row = findRow(r, end)

print(abs(start_row - end_row))
