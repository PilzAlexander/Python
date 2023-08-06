"""
#358: String abwechselnd neu anordnen
Gegeben ist ein String (Text) bestehend aus Kleinbuchstaben und Ziffern. Ziel ist es diesen String neu anzuordnen,
sodass sich Kleinbuchstaben und Ziffern abwechseln.
"""

import string

def stringFormat(string):

    formattedString = ""
    alphasDistribution = 0
    decimalDistribution = 0
    alphas = ""
    decimal = ""
    stringLength = len(string)

    if (stringLength % 2 == 0):
        for element in range(0, stringLength):
            if string[element].isalpha():
                alphasDistribution += 1
                alphas += string[element]

            elif string[element].isdecimal():
                decimalDistribution +=1
                decimal += string[element]
    else:
        print("String has an uneven amount of characters!")
        return formattedString

    if ((alphasDistribution % 2) == 0) and ((decimalDistribution % 2) == 0) and (alphasDistribution !=0) and (decimalDistribution != 0):
        for i in range(0, int(stringLength / 2)-1):
            formattedString += alphas[i] + decimal[i]
    else:
        print("String has an uneven distribution of letters and numbers!")
        return formattedString

    return formattedString


string = "abcde12345"


result = stringFormat(string)
print(result)
