users = [
    ("Ali",25,"Python"),
    ("Sara",30,"Java"),
    ("Reza",22,"Python"),
    ("Mina",28,"C++"),
    ("John",35,"Python"),
    ("David",30,"Java")
]
# گزوه بتدی
languages = {}
ages = []
for user in users:
    user_name = user[0]
    user_language = user[2]
    if user_language in languages:
        languages[user_language].append(user_name)
    else:
        languages[user_language] = [user_name]
print(languages)
# میانگین سن هر زبان
for language in languages:
    total = 0
    count = 0
    for user in users:
        if user[2] == language:
            total += user[1]
            count += 1
    average = total / count
    print(language,": ",average)
# مسن ترین
for language in languages:
    oldest_name = ""
    oldest_age = 0
    for user in users:
        if user[2] == language:
            if user[1] > oldest_age:
                oldest_age = user[1]
                oldest_name = user[0]
    print(language,": ",oldest_name,oldest_age)
#زبان دارای بیشترین کاربر
best_language = ""
max_user = 0
for language in languages:
    if len(languages[language]) > max_user:
        max_user = len(languages[language])
        best_language = language
print("Most popular language: ", best_language)
# تمام زبان ها
x = []
for language in languages:
    x.append(language)
print("languages: ",x)