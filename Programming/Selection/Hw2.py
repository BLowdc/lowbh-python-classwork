temp = int(input())
humid = int(input())
window = input("open/closed")
if window == 'closed':
    if temp > 25 or humid > 50:
        print("open the window")
elif temp < 10 and humid < 50:
    print("close the window")
