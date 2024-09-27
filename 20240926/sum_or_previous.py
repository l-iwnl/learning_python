# 2024.09.26
max_count = 10
for i in range(max_count):
    previous = 0 if i <= 0 else i - 1
    print(
        "Current Number " + str(i) +
        " Previous Number " + str(previous) +
        " Sum: " + str(i + previous)
    )
