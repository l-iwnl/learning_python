# 2024.09.26
def is_odd(num):
    return num % 2 == 0


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_list = []

for item in list1:
    if not is_odd(item):
        result_list.append(item)

for item in list2:
    if is_odd(item):
        result_list.append(item)

print(result_list)
