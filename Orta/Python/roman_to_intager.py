def romanToInt(s):
    symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    n = len(s)
    
    for i in range(n):
        if i < n - 1 and symbol_values[s[i]] < symbol_values[s[i + 1]]:
            result -= symbol_values[s[i]]
        else:
            result += symbol_values[s[i]]
    
    return result

print(romanToInt("III"))      # Output: 3
print(romanToInt("LVIII"))    # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
