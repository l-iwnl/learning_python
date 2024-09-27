# 2024.09.26
def closed_neighbourhood(entry):
    if len(entry) == 0:
        return "You cannot enter an empty entry"
    return entry[0] == entry[len(entry) - 1]


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(closed_neighbourhood(numbers_x))
print(closed_neighbourhood(numbers_y))
