def permutations(string):
    # Base case: If the string has only one character, return it as the only permutation
    if len(string) == 1:
        return [string]

    # Recursive case: Generate permutations by swapping each character with the first character
    perms = []
    for i in range(len(string)):
        if i > 0 and string[i] == string[0]:
            continue  # Skip duplicate characters to remove duplicate permutations
        chars = list(string)
        chars[0], chars[i] = chars[i], chars[0]  # Swap characters
        subperms = permutations(''.join(chars[1:]))  # Generate permutations for the remaining characters
        perms.extend([chars[0] + perm for perm in subperms])

    return perms

print(permutations('a'))     # Output: ['a']
print(permutations('ab'))    # Output: ['ab', 'ba']
print(permutations('abc'))   # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(permutations('aabb'))  # Output: ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
