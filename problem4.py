def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest_palindrome = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if product > largest_palindrome and is_palindrome(product):
            largest_palindrome = product
print(largest_palindrome)
