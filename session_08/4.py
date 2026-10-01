def get_values():
    """recives numbers of values from user and retuns them as a list"""
    count = int(input("How many values you want to enter: "))
    values = []
    for i in range(count):
        value = input("Enter: ")
        values.append(value)
    return values
def add_unique(value,unique_list,positions,position):
    """
    *checks if value is repetitive or not
    *if it was new returs True
    *if it wasnt new returns False and prints its location
    """
    lower_value = value.lower()
    for i in range(len(unique_list)):
        if unique_list[i].lower() == lower_value:
            print(f"repetitive value {position[i]},has been added ---> {value}")
            return False
    unique_list.append(value)
    positions.append(position)
    print(f"new value has been added ---> {value}")
    return True
def process_values(values):
    """checks all values and returns final informations"""
    unique_list = []
    positions = []
    unique_count = 0
    duplicate_count = 0
    for i in range(len(values)):
        value = values[i]
        position = i + 1
        if value == "":
            print("empty value has been enterred and it would be ignored")
            continue
        is_new = add_unique(value,unique_list,positions,position)
        if is_new:
            unique_count += 1
        else:
            duplicate_count += 1
    return unique_list,positions,unique_count,duplicate_count
def show_report(unique_list,positions,unique_count,duplicate_count):
    """prints final report"""
    print()
    print(f"final report: ")
    print(f"\tunique values: {unique_list}")
    print(f"\tnumber of unique values: {unique_count}")
    print(f"\tnumber of duplicate values: {duplicate_count}")
    print("first locations:")
    for i in range(len(unique_list)):
        print(f"{unique_list[i]} ---> {positions[i]}")
