hrs = int(input())
min = int(input())
x = input()
if x == 'am':
    print(hrs*60+min)
elif x == 'pm':
    print(hrs*60+min+12*60)