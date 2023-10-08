def new_str(old_string):
    new_string = ""
    total = 0
    while total < len(old_string):
        char = old_string[total]
        count = ""
        total += 1
        while total < len(old_string) and old_string[total].isdigit():
            count += old_string[total]
            total += 1

        count = int(count) if count else 1
        new_string += char * count
    return new_string

old_string = input("Введите строку: ")
result = new_str(old_string)
print("Новая строка:",  result)