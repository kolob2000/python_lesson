src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [element for index, element in enumerate(src) if index != 0 and element > src[index - 1]]
print(result)
