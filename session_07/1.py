def analyze_text(text:str)->list:
    result = {"words":0,"letters":0,"digits":0,"most_common_letter":"","most_common_word":"","longest_word":"","shortest_word":"","palindrom_words":0,"upper_class_words":0,"lower_class_words":0}
    splited = text.split()
    # تعداد کلمات
    result["words"] = len(splited)
    for i in range(len(splited)):
        for j in range(len(splited[i])):
            # تعداد حروف
            if splited[i][j].isalpha():
                result["letters"] += 1
            elif splited[i][j].isdigit():
                # تعداد اعداد
                result["digits"] += 1
    # پر تکرار ترین کلمه
    words = {}
    for word in splited:
        words[word] = words.get(word,0) + 1
    max_count = 1
    for word in words:
        if  words[word] > max_count:
            result["most_common_word"] = word
    # پر تکرار ترین حرف
    letters = {}
    for word in splited:
        for letter in word:
            letters[letter] = letters.get(letter,0) + 1
    count = 1
    for letter in letters:
        if letters[letter] > count:
            result["most_common_letter"] = letter
    # کلمات palindrom
    for word in splited:
        if word == word[::-1]:
            result ["palindrom_words"] += 1
    #طولانی ترین کلمه
    wordss = {}
    for word in splited:
        wordss[word] = len(word)
    longest = 0
    for word in wordss:
        if longest < wordss[word]:
            long = wordss[word]
            result["longest_word"] = word
            # کوتاه ترین کلمه
            shortest = wordss[word]
            for word in wordss:
                if wordss[word] < shortest:
                    result["shortest_word"] = word
    # تعداد حروف بزرگ
    for word in splited:
        for letter in word:
            if letter.isupper():
                result["upper_class_words"] += 1
            elif letter.islower():
                result["lower_class_words"] += 1
    return result