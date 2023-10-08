def chasto(string):
    string = string.replace(" ", "")
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    most_common = sorted_counter[:3]
    return most_common

old_string = input("Введите строку: ")
frequent_characters = chasto(old_string)
for char, count in frequent_characters:
    print("Символ:",char, "Количество:",count)