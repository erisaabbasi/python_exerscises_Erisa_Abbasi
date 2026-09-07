text = input("text:")
words = text.split()
letters = 0
digits = 0
spaces = 0
upper = 0
lower = 0
char_count = {}
for i in text:
    if i.isalpha():
        letters += 1
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
        if i.isupper():
            upper += 1
        else:
            lower += 1
    elif i.isdigit():
        digits += 1
    elif i == " ":
        spaces += 1
word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
longest = words[0]
shortest = words[0]
for i in words:
    if len(i) > len(longest):
        longest = i
    if len(i) < len(shortest):
        shortest = i
most_char = words[0][0]
most_char_count = 0
for i in char_count:
    if char_count[i] > most_char_count:
        most_char_count = char_count[i]
        most_char = i
most_word = words[0]
most_word_count = 0
for i in word_count:
    if word_count[i] > most_word_count:
        most_word_count = word_count[i]
        most_word = i
print("Total characters: ",len(text))
print("Total words: ",len(words))
print("Total letters: ",letters)
print("Total digits: ",digits)
print("Total spaces: ",spaces)
print("Total uppercase: ",upper)
print("Total lowercase: ",lower)
print("Longest word: ",longest)
print("shortest word: ",shortest)
print("Most repeated character: ",most_char)
print("Most repeated word: ",most_word)