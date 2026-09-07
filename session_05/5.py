sentence = input("enter a sentence: ")
words = sentence.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
print("length: ",len(longest))