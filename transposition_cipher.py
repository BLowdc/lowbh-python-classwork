cipher = input("Ciphertext: ")
cipher = cipher.replace("\n", "")
cols = int(input("Length: "))
keyword = input("Keyword: ")
rows = len(cipher) // cols + 1
matrix = []
for i in range(rows):
    if (i + 1) * cols > len(cipher):
        end = len(cipher)
    else:
        end = (i + 1) * cols

    matrix.append(list(cipher[i * cols:end]))

newMatrix = []
for row in matrix:
    newRow = []
    for r in range(len(keyword)):
        if int(keyword[r])-1 < len(row):
            newRow.append(row[int(keyword[r])-1]) 
    newMatrix.append(newRow)

for row in newMatrix:
    for char in row:
        print(char, end="")
