# Verwaltung Buchladen
Ein Programm zur Verwaltung eines Buchladens.

Alle Fließkommazahlen müssen mit einem "." statt einem "," eingegeben werden!

### Folgende Funktionen gibt es:
- book_add
  - Parameter:
    - inventory (Liste der Bücher)
    - title (Titel des Buchs, Text)
    - author (Autor des Buchs, Text)
    - price (Preis des Buchs, Fließkommazahl)
  - Parameter title, author und price werden der Liste inventory als Dict angefügt

- book_list
  - Parameter:
    - inventory (Liste der Bücher)
  - Zeigt die Titel aller Bücher an

- book_search
  - Parameter:
    - inventory (Liste der Bücher)
    - title (Titel, nach dem gesucht wird, Text)
  - Sucht das Buch mit dem übergebenen Titel und gibt das Dict dieses Buches oder None (falls das Buch nicht gefunden wurde) zurück

- book_filter_price
  - Parameter:
    - inventory (Liste der Bücher)
    - max_price (maximaler Preis der gefilterten Bücher, Fließkommazahl mit Standardwert 20.0)
  - Filtert die Bücher nach dem eingegebenem maximalen Preis und gibt alle passenden Bücher als Dict zurück
- book_total_value
  - Parameter:
    - inventory (Liste der Bücher)
  - Berechnet den Gesamtpreis aller Bücher im Bestand und gibt den Wert als Fließkommazahl zurück