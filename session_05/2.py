text = input("text: ")
result = ""
for i in text:
    if i not in result:
        result += i
print(result)