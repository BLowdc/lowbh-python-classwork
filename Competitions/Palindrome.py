n = int(input())
def palindrome(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False
print(palindrome(n))