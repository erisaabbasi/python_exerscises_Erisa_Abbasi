for i in range(1,11):
    if i % 2 == 0:
        answer = i * 5
        print(f"{i} * 5 = {answer}")
    elif i % 2 != 0:
        answer = i + 5
        print(f"{i} + 5 = {answer}")