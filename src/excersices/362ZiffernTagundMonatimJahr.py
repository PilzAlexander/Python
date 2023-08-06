"""
#359: Ziffern Tag und Monat im Jahr
Ermittle für die Jahre 2001 bis 2022 jedes Datum, in dem die Ziffern der Felder Tag und Monat mit dem Feld Jahr übereinstimmen.
Die Lösung für das Jahr 2001 lautet:
"""


import datetime as dt

def numInDayandMonthinYear(startDate, endDate):

    matches = []
    allYears = list(range(startDate, endDate +1))
 
    for year in allYears:

        startDate = dt.date(year, 1, 1)
        endDate = dt.date(year,12, 31)

        sortYear = list(str(year))
        sortYear.sort()
        sortYearStr = " ".join(sortYear)

        while startDate < endDate:

            compareDayYear = list(str(startDate.strftime("%d%m")))
            compareDayYear.sort()
            compareDayYearstr = " ".join(compareDayYear)

            if sortYearStr == compareDayYearstr:
                print(startDate.strftime("%d.%m") + " -> " + str(year))
                matches.append(startDate.strftime("%d.%m"))

            startDate = startDate + dt.timedelta(days=1)

numInDayandMonthinYear(2001, 2022)
