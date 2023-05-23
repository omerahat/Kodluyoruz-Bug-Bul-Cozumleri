def intToRoman(num):
    symbols = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    
    roman = ''
    
    for symbol, value in symbols:
        while num >= value:
            roman += symbol
            num -= value
    
    return roman

print(intToRoman(3))        # Output: "III"
print(intToRoman(58))       # Output: "LVIII"
print(intToRoman(1994))     # Output: "MCMXCIV"
