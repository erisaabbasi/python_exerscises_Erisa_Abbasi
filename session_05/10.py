s1 = input("sentence 1: ")
s2 = input("sentence 2: ")
word1 = set(s1.split())
word2 = set(s2.split())
common = word1.intersection(word2)
for word in common:
    print(word)