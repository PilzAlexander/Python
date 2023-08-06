"""
#357: String-Vergleich mit Rücktaste/Backspace
Gegeben sind zwei Strings (Texte) bestehend aus einer Anzahl (<100) Kleinbuchstaben (a-z) und
Backspaces (Rücktastenzeichen) welche hier als Hashtag/Raute (#) dargestellt werden.
Dabei können die Strings unterschiedlicher Länge sein.
Ziel soll es sein zu überprüfen, ob die beiden Strings (s1, s2) identisch sind.
"""

import string

def removeBack(string1):
    formattedString1 = ""
    for element in range(0,len(string1)):
        if string1[element] != "#":
            formattedString1 += string1[element]
        elif len(formattedString1) > 0:
            formattedString1 = formattedString1[:-1]
        else:
            continue
    return formattedString1

def stringCompare(string1, string2):

    formattedString1 = ""
    formattedString2 = ""
    result = False

    if(len(string1) > 100 or len(string2) > 100):
        print("At least one string is over 100 characters!")
        return result
    elif(string1.isdigit() or string2.isdigit()):
        print("At least one string is contains numbers!")
        return result
  
    formattedString1 = removeBack(string1)
    formattedString2 = removeBack(string2)

    if formattedString1 == formattedString2:
        return True

    return result

print(stringCompare("ab#c", "ae#c"))
print(stringCompare("ab##", "e#f#"))
print(stringCompare("a#c", "ac#"))
print(stringCompare("####", "###a#"))
print(stringCompare("abcdefg", "abcder#fr#g"))
print(stringCompare("abcde#fgh#ijklmno", "ab#cdef#gh"))
