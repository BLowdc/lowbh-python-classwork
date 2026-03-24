def Solution(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    for col in matrix:
        for row in col:
            if not (1 <= row <= n):
                return False
    
    return True

a = [[1,1,1],
 [1,1,1],
 [1,1,1]]
print(Solution(a))