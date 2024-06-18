# Verwaltung Buchladen
Ein Programm zur Verwaltung eines Buchladens.

Alle Fließkommazahlen müssen mit einem "." statt einem "," eingegeben werden!

### Folgende Funktionen gibt es:
- book_add: Fügt ein Buch zum Inventar hinzu
- book_list: Zeigt alle Bücher in sortierter (standardmäßig nach Titel) Reihenfolge an
- book_search: Sucht ein Buch und gibt dessen Werte zurück
- book_filter_price: Filtert die Bücher nach einem maximalen Preis und gibt sie zurück
- book_total value: Berechnet Gesamtwert des Inventars und gibt diesen zurück
- book_delete: Löscht ein Buch anhand seines Titels

### Erklärung der Funktionen
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
    - sort_condition (Bedingung, nach der die Bücher sortiert werden, Standardwert title)
  - Sortiert die Bücher nach der übergebenen Bedingung (standardmäßig Titel) und zeigt Titel, Autor und Preis an

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

- book_delete
  - Parameter:
    - inventory (Liste der Bücher)
    - title (Titel des Buchs, das gelöscht werden soll)
  - Löscht das Buch mit dem eingegebenen Titel
