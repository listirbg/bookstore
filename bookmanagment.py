# ############################
# ### Verwaltung Buchladen ###
# ############################

# ### MODULE

# ### FUNKTIONEN
# Hinzufügen eines Buchs
def book_add(inventory: list[dict], title: str, author: str, price: float):
    inventory.append(dict({"title": title, "author": author, "price": price}))


# Auflisten aller Bücher
def book_list(inventory: list[dict]):
    for book in inventory:
        print(book["title"])


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


# ### PROGRAMM
if __name__ == '__main__':
    pass
