"""
#360: Ziffern durch Kleinbuchstaben ersetzen (right-shifting)
Gegeben ist ein String (Text) bestehend aus Kleinbuchstaben und den Ziffern 0 bis 9.
Die Buchstaben stehen an den geraden und die Ziffern an den ungeraden Stellen (zero-based).
Ziel soll es sein, jede Ziffer durch einen Buchstaben zu ersetzen, indem der vorangestellte Buchstabe
um den Wert der Ziffer gemäß Alphabet nach rechts verschoben wird (right-shifting).
Die Buchstaben bleiben dabei erhalten.
Bei der Erstellung des Ausgangs-Strings soll darauf geachtet werden, dass das Verschieben nicht über 'z' hinausgeht.
"""


def rightShifting(string):
    
    result = ""

    for i in range(1, len(string), 2):
        result += (string[i-1])
        result += chr((ord(string[i - 1]) + int(string[i]) - 97) % 26 + 97)

    

    return result





string = "a4b2c1d5"


result = rightShifting(string)
print(result)