number = 600851475143
i = 2
while i * i <= number:
    if number % i:
        i += 1
    else:
        number //= i
print(number)
