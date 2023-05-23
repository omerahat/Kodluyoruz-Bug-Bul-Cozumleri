

def sum_two_smallest(array):
    small_1 = float('inf') #daha küçük bir değer olmaması için sonsuza yakın iki değişken oluşturuyoruz.
    small_2 = float('inf')
    for i in array:
        if i <= small_1:
            small_2 = small_1
            small_1 = i
        elif i <= small_2:
            small_2 = i
    return small_1 + small_2

           



print(sum_two_smallest([19, 5, 42, 2, 77]))  # Output: 7
print(sum_two_smallest([10, 343445353, 3453445, 3453545353453]))  # Output: 3453455


"""
Kısa Çözüm:
def sum_two_smallest(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]
"""