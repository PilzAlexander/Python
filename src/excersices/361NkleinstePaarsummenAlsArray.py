"""
#361: n kleinste Paarsummen als Array
Gegeben sind 2 sortierte Arrays (arr1, arr2) gleicher oder unterschiedlicher Länge
und eine Zahl (n) welche die maximale Anzahl der kleinsten auszugebenden Paarsummen vorgibt.
Jedes Array kann 1 bis zu 10.000 Zahlen der Größe +-1.000.000 beinhalten.
Der Wert für n soll nicht weniger als 1 und nicht mehr als 1.000 betragen.

Ziel soll es sein, die n kleinsten aller möglichen Paarsummen als Array zurückzugeben.
"""


def smallestPairSum(arr1, arr2, n):

    pairs = []
    result = []

    if (n < 1 or n > 1000):
        print("Value for n out of range")
        return -1

    if (len(arr1) > 10000 or len(arr2) > 10000):
        print("Array too big")
        return -2
    
    if (len(arr1) == 0 or len(arr2) == 0):
        print("Array too small")
        return -3

    for element1 in arr1:
        for element2 in arr2:
                pairs.append([element1 + element2, element1, element2]) 
                pairs.sort()

    i = 0
    for pair in pairs:
        if i < n:
            result.append(pair[0])
            i+=1

    return result


arr1 = [1,2,3]
arr2 = [1,2,3,4,5,6]

result = smallestPairSum(arr1, arr2, 2)
print(result)