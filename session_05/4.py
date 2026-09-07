sentence = (input("enter a sentence: "))
words = sentence.split()
most_word = words[0]
most_count = 0
for word in words:
    count = 0
    for word2 in words:
        if word2 == word:
            count += 1
    if count > most_count:
        most_count = count
        most_word = word
print(most_word,"-->",most_count)