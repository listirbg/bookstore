# ############################
# ### Verwaltung Buchladen ###
# ############################

# ### MODULE

# ### FUNKTIONEN
# Hinzufügen eines Buchs
def book_add(inventory: list[dict], title: str, author: str, price: float):
    inventory.append(dict({"title": title, "author": author, "price": price}))


# Bücher nach Sortierung anzeigen
def book_list(inventory: list[dict], sort_condition: str = "title"):
    inventory_sorted: list[dict] = sorted(inventory, key=lambda book: book[sort_condition])
    for book_dict in inventory_sorted:
        print(f"{book_dict["title"]}, {book_dict['author']}, {book_dict['price']}")


# Suche nach einem Buchtitel
def book_search(inventory: list[dict], title: str) -> dict or None:
    for book in inventory:
        if book["title"] == title:
            return book
    return None


# Bücher nach Preis filtern
def book_filter_price(inventory: list[dict], max_price: float = 20.0) -> list[dict]:
    books_filtered: list[dict] = []
    for book in inventory:
        if book["price"] <= max_price:
            books_filtered.append(book)
    return books_filtered


# Gesamtwert des Bestands berechnen
def book_total_value(inventory: list[dict]) -> float:
    prices: list[float] = []
    for book in inventory:
        prices.append(book["price"])
    total_value: float = sum(prices)
    return total_value


# Buch löschen
def book_delete(inventory: list[dict], title: str):
    for book in inventory:
        if book["title"] == title:
            inventory.remove(book)


# ### PROGRAMM
if __name__ == '__main__':
    book_inventory: list[dict] = []
    title1 = "Das helle Buch"
    title2 = "Das schwere Buch"
    title3 = "Das alte Buch"
    author1 = "Der Sonnenschein"
    author2 = "Butter-Golem"
    author3 = "Opi"
    price1 = 14.99
    price2 = 49.99
    price3 = 29.99
    book_add(book_inventory, title1, author1, price1)
    book_add(book_inventory, title2, author2, price2)
    book_add(book_inventory, title3, author3, price3)
    print(book_inventory)
    book_list(book_inventory)
    print(book_search(book_inventory, title1))
    print(book_total_value(book_inventory))
    book_list(book_inventory, sort_condition="author")
