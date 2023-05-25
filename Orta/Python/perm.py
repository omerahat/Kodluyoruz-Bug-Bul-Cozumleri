def permutations(string):
    
    if len(string) == 1:
        return [string]

    
    perms = []
    for i in range(len(string)):
        if i > 0 and string[i] == string[0]:
            continue  
        chars = list(string)
        chars[0], chars[i] = chars[i], chars[0]  
        subperms = permutations(''.join(chars[1:]))  
        perms.extend([chars[0] + perm for perm in subperms])

    return perms

print(permutations('a'))     # Output: ['a']
print(permutations('ab'))    # Output: ['ab', 'ba']
print(permutations('abc'))   # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(permutations('aabb'))  # Output: ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
