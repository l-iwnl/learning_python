# 2024.09.26
def product_or_sum(first_number, second_number):
    limit = 1000
    product = first_number * second_number
    return product if product <= limit else first_number + second_number


cases = [
    [
        20,
        30
    ],
    [
        40,
        30
    ]
]

for case in cases:
    print(product_or_sum(*case))
