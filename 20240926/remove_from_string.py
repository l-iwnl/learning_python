# 2024.09.26
def remove_from_string(word, count):
    if len(word) < count:
        return "You should give a bigger string"

    return word[count:]


print(remove_from_string("Palavra", 2))