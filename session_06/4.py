employees = {
    "E01" : {"name" : "Ali","age" : 28,"salary" : 3000},
    "E02" : {"name" : "Sara","age" : 32,"salary" : 4500},
    "E03" : {"name" : "Reza","age" : 25,"salary" : 2800}
}
# بیشترین حقوق
max_salary = 0
for x in employees:
    if employees[x]["salary"] > max_salary:
        max_salary = employees[x]["salary"]
        max_name = employees[x]["name"]
print("highest salary ---> ",max_name)
# میانگین
avg = sum(employees[x]["salary"] for x in employees) / len(employees)
print("average salary ---> ",avg)
# حقوق بیشتر از 3000
print("salary over 3000: ")
for x in employees:
    if employees[x]["salary"] > 3000:
        print("*",employees[x]["name"])
#کمترین حقوق
min_salary = 900000000
for x in employees:
    if employees[x]["salary"] < min_salary:
        min_salary = employees[x]["salary"]
        min_name = employees[x]["name"]
print("lowest salary ---> ",min_name)