
def isValid(string):

    for x in range(len(string)//2): #çiftli eleme yapacağımız için stringin uzunluğunun yarısı kadar döndüreceğiz
            if string=='': #eğer string boşsa direkt True döndürür
                return True
            string = string.replace('()', '').replace('{}', '').replace('[]', '') # stringin herhangi bir yerinde (),{},[] görürse "" olarak değiştirir. Kısaca siler 
    return string=='' #En son string boş kalırsa True kalmazsa False Döndürür

print(isValid("()"))         # Output: True
print(isValid("()[]{}"))     # Output: True
print(isValid("(]"))         # Output: False
