# ############################
# ### Verwaltung Buchladen ###
# ############################

# ### MODULE

# ### FUNKTIONEN
# Hinzufügen eines Buchs
def book_add(inventory: list, title: str, author: str, price: float):
    inventory.append(dict({"title": title, "author": author, "price": price}))


# Auflisten aller Bücher
def book_list(inventory: list):
    for book in inventory:
        print(book["title"])


# Suche nach einem Buchtitel
def book_search(inventory: list, title: str) -> dict or None:
    for book in inventory:
        if book["title"] == title:
            return book
    return None


# ### PROGRAMM
if __name__ == '__main__':
    pass
