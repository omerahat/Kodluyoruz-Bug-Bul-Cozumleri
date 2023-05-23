
def invert(array):
    for index in range(len(array)): #listenin uzunluğunu kadar dönecek for döngüsü tanımlıyoruz.
        array[index]=-array[index] #listenin elemanını toplamaya göre tersi olarak eşitliyoruz
    print(array)

invert([1,2,3,4,5]) # Output: [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) # Output: [-1,2,-3,4,-5]
invert([]) # Output: []

"""
Kısa çözüm:
def invert(array):
    return [-num for num in array]
"""