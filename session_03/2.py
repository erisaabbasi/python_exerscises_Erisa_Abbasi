record = 0
for i in range(10):
    new_record = int(input("what is your new record?:"))
    if new_record > record:
        record = new_record
        print("the new record is saved! ", record)
    else:
        print("this record is already saved!")