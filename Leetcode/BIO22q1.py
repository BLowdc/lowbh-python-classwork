letters = ['null','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
string = input("   Enter encrypted string: ")
prev_index = letters.index(string[0])
ogString = [string[0]]
for i in range(1,len(string)):
    sum = letters.index(string[i]) - prev_index
    if sum <= 0:
        sum += 26
    #end if
    prev_index = letters.index(string[i])
    ogString.append(letters[sum])
#next i
for letter in ogString:
    print(letter, end='')
#end letter
