def new_str(string):
    new_string = ""
    total = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            total += 1
        else:
            new_string += string[i - 1] + (str(total) if total > 1 else "")
            total = 1
    new_string += string[-1] + (str(total) if total > 1 else "")
    return new_string

old_string = input("Введите строку: ")
result = new_str(old_string)
print("Сжатый формат:", result)