f = open("c:\\AOC24\\corrupt.txt","r")
s = f.read()
string_ls = []
num_ls = []
total = 0
search = True

c = 0

for i in range(3,len(s)):
    if "don't()" in s[(i-7):i]:
        search = False
    if "do()" in s[(i-4):i]:
        search = True
    if s[(i-3):i] == "mul" and search:
        string = ''
        while s[i] in '1234567890(),':
            string += s[i]
            i += 1
        #end while
        string_ls.append(string)
    #end if
#next i

print(string_ls)

for string in string_ls:
    if ('(' not in string) or (')' not in string):
        continue
    for char in string:
        if char not in '0123456789':
            string = string.replace(char,' ')
        #endif
    #next char
    num_ls.append(string)
#next string

for numbers in num_ls:
    num = [int(i) for i in numbers.split() if i.isdigit()]
    print(num)
    if len(num) == 2:
        total += num[0] * num[1]
    #end if
#next numbers

print(total)