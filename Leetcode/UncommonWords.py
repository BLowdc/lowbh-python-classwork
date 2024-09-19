s1 = "this apple is sweet"
s2 = "this apple is sour"
s1_words = []
s2_words = []
space = 0
space2 = 0

for i in range(len(s1)):
    if s1[i] == ' ':
        word = s1[space:i]
        s1_words.append(word)
        space = i + 1
s1_words.append(s1[space:])

for i in range(len(s2)):
    if s2[i] == ' ':
        word2 = s2[space2:i]
        s2_words.append(word2)
        space2 = i + 1
s2_words.append(s2[space2:])

unique = []
for i in range(len(s1_words)):
    unique.append(s1_words[i])

for j in range(len(s2_words)):
    if s2_words[j] in unique:
        unique.remove(s2_words[j])
    else:
        unique.append(s2_words[j])

print(unique)