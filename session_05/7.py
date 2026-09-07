text = input("text: ")
result = ""
count = 1
for i in range(1,len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        if count > 1:
            result += text[i-1] + str(count)
        else:
            result += text[i-1]
        count = 1
if count > 1:
    result += text[i-1] + str(count)
else:
    result += text[-1]
print(result)
