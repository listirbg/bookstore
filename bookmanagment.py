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


# ### PROGRAMM
if __name__ == '__main__':
    pass
