clock = int(input("what time is it? "))
if 0 <= clock <= 3:
    print("mid night")
elif 4 <= clock <= 11:
    print("morning")
elif 12 <= clock <= 13:
    print("noon")
elif 14 <= clock <= 17:
    print("afternoon")
elif 18 <= clock <= 20:
    print("evening")
elif 20 <= clock <= 23:
    print("night")
else:
    print("invalid number")