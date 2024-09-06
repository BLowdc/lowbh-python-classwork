hrs = int(input())
mins = int(input())
x = input()
if x == 'am':
    print(hrs * 60 + mins)
elif x == 'pm':
    print(hrs * 60 + mins + 12 * 60)
