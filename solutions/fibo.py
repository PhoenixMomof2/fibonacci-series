def fibonacci(num):
    if num < 2:
        return num

    last_two = [0, 1]

    for i in range(num - 1):
        sum = last_two[0] + last_two[1]
        last_two = [last_two[1], sum]

    return last_two[1]
  
print(fibonacci(0))
print(fibonacci(2))
print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(20))