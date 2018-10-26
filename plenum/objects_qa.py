

while True:
    value = input("Write some input:")
    if value == "q":
        break
    result = eval(value)
    print(result, type(result))
