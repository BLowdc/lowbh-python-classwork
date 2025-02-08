def palindrome(str) -> bool:
    list1 = list(str)
    list1c = list(str)
    list2 = []
    while len(list1c):
        list2.append(list1c.pop())
    if list1 == list2:
        return True
    else:
        return False

myString = input("Enter string: ")
print(palindrome(myString))
