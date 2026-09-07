sentence = input("enter a sentence: ")
words = sentence.split()
forbidden = ["hack","fraud","scam","password","attack"]
for f in forbidden:
    count = words.count(f)
    if count > 0:
        print(f,"--> ",count)
