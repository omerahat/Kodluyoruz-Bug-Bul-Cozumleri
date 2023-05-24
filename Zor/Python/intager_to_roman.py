def intToRoman(num):
    symbols = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),         #roman harfleri ve karşılıklarını dictionary olarak tanımlıyoruz
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    
    roman = ''
    
    for symbol, value in symbols: 
        while num >= value: #inputtan küçük en büyük sayıyı alıyoruz
            roman += symbol #roman stringine karşılığını ekliyoruz
            num -= value    #inputtan alınan sayıyı güncelliyoruz
    
    return roman

print(intToRoman(3))        # Output: "III"
print(intToRoman(58))       # Output: "LVIII"
print(intToRoman(1994))     # Output: "MCMXCIV"
