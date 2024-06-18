# ############################
# ### Verwaltung Buchladen ###
# ############################

# ### MODULE

# ### FUNKTIONEN
# Funktion zum Hinzufügen eines Buchs
def book_add(inventory: list, title: str, author: str, price: float):
    inventory.append(dict({"title": title, "author": author, "price": price}))


# ### PROGRAMM
if __name__ == '__main__':
    pass
