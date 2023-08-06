"""
#359: Stände von Koordinaten (Standort) im Umkreis von x km ermitteln
Erstelle eine Funktion, eventuell mit Hilfe einer Datenbank, welche über die Parameter Location (Latitude & Longitude) und Radius in Kilometer alle Städte in dem Umkreis mit den Koordinaten ausgibt.

Oder eine Liste mit den Koordinaten in diesem Umkreis. Somit können dann die Städte in einer GeoDatenbank ermittelt werden. 
"""


import sqlite3
from geopy import distance as di

con = sqlite3.connect("359_DB.db")

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS city(cityname, latitude, longitude)")


cur.execute("INSERT INTO city VALUES ('Vohburg', 48.76834911848562, 11.61956401821461)")
cur.execute("INSERT INTO city VALUES ('Ingolstadt', 48.766607027881086, 11.4229098015022)")
cur.execute("INSERT INTO city VALUES ('Kösching', 48.811670613489085, 11.504027049500781)")
cur.execute("INSERT INTO city VALUES ('Großmehring', 48.76568720620593, 11.536663940378322)")
cur.execute("INSERT INTO city VALUES ('München', 48.13518032370526, 11.58028602562508)")
cur.execute("INSERT INTO city VALUES ('Würzburg', 49.79114437174501, 9.952641179531684)")
cur.execute("INSERT INTO city VALUES ('Berlin', 52.52219068159123, 13.395885822117378)")           
            
con.commit()
con.close()


def distance(lat, long, radius, database):

    con = sqlite3.connect(database)
    cur = con.cursor()
    

    data = cur.execute("""SELECT * FROM city""")
    
    print("Folgende Orte sind von", "lat", lat, "lon", long, "weniger als", radius, "km entfernt:", "\n")
    for row in data:
        cityname = row[0]
        lati = row[1]
        longi = row[2]
        origin = (lat, long)
        target = (lati, longi)
        distance = di.distance(origin, target)

        if distance < radius:
            print(cityname, "=", distance)

    
    cur.execute("DROP TABLE city")
    con.close()

    return 0

lat = 48.76694646711988
long = 11.42634302906503
radius = 20
database = "359_DB.db"

distance(lat, long, radius, database)
