def are_anagrams(s1: str, s2: str):
    m = {
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29,
        "k": 31,
        "l": 37,
        "m": 41,
        "n": 43,
        "o": 47,
        "p": 53,
        "q": 59,
        "r": 61,
        "s": 67,
        "t": 71,
        "u": 73,
        "v": 79,
        "w": 83,
        "x": 89,
        "y": 97,
        "z": 101,
    }
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    n1 = 1
    n2 = 1
    for char in s1:
        n1 *= m[char]
    for char in s2:
        n2 *= m[char]

    if n1 == n2:
        return True
    else:
        return False


print(are_anagrams("Racecar", "carrace"))
