# 2024.09.26
def multiplication_table(x):
    for i in range(1, x + 10):
        if x == 0:
            print("table of " + str(i))
            for j in range(0, x + 10):
                print(str(i) + " times " + str(j) + " = " + str(i * j), end=" ")
                print("\t\t")
        else:
            print(str(i) + " times " + str(x) + " = " + str(i * x))


multiplication_table(0)
