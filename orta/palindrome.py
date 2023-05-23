def is_palindrome(num):
    # Convert the number to a string and check if it reads the same forwards and backwards
    return str(num) == str(num)[::-1]

def largest_palindrome():
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= largest_palindrome:
                # No need to continue if the product is smaller than the largest palindrome found so far
                break
            if is_palindrome(product) and product > largest_palindrome:
                # Update the largest palindrome if a larger one is found
                largest_palindrome = product
    return largest_palindrome

# Call the function to find the largest palindrome
result = largest_palindrome()
print(result)
