import random
import json


# Haal de raw JSON data uit steam.json en convert het naar een list van dicts
# Returns: list van dicts
def load_json():
    with open('steam.json') as json_file:
        return json.load(json_file)


data = random.sample(range(100000), 5000)  # Maakt een lijst van 10 random nummers onder de 100 zonder herhaling


# Een class om een node van de BST te representeren.
class Node:
    def __init__(self, value, key):
        self.value = value          # De waarde opgeslagen in de node
        self.key = key              # De key waarop gesorteerd wordt
        self.left = None            # De linker kind
        self.right = None           # De rechter kind

    def insert(self, value):                        # Voeg een bepaalde waarde toe aan de BST
        if value[self.key] < self.value[self.key]:  # Als de waarde kleiner is dan de waarde van de node
            if self.left is not None:               # Als de huidige node een linker kind heeft
                self.left.insert(value)             # Run de insert functie van de linker kind en geef dezelfde waarde door
            else:                                   # Anders (als de huidige node links geen kind heeft)
                self.left = Node(value, self.key)   # Voeg links een nieuwe node toe met de waarde erin opgeslagen
        else:                                       # Anders (als de waarde groter is dan de waarde van de huidige node)
            if self.right is not None:              # Als de huidige node een rechter kind heeft
                self.right.insert(value)            # Run de insert functie van de rechter kind en geef dezelfde waarde door
            else:                                   # Anders (als de huidige node recht geen kind heeft)
                self.right = Node(value, self.key)  # Voeg rechts een nieuwe node toe met de waarde erin opgeslagen

    def search(self, value):                            # Zoek of een bepaalde waarde in de BST zit
        if value[self.key] == self.value[self.key]:     # Als de waarde van deze node de gezochte waarde is
            return True
        if value[self.key] < self.value[self.key]:      # Als de waarde van de gezochte key kleiner is dan de waarde van deze node
            if self.left is None:                       # Als deze node geen linker kind heeft
                return False
            return self.left.search(value)              # Run de search functie van de linker kind en geef de gezochte waarde door
        if self.right is None:                          # Als deze node geen rechter kind heeft
            return False
        return self.right.search(value)                 # Run de search functie van de rechter kind en geef de gezochte waarde door

    def collapse(self):                         # Produceer een gesorteerde lijst van deze node en al zijn nakomelingen
        result = []
        if self.left is not None:               # Als deze node een linker kind heeft
            result += self.left.collapse()      # Collapse de linker kind en voeg deze toe aan het resultaat
        result += [self.value]                  # Voeg de waarde van deze node toe aan het resultaat
        if self.right is not None:              # Als deze node een rechter kind heeft
            result += self.right.collapse()     # Collapse de rechter kind en voeg deze toe aan het resultaat
        return result


def createbst(lst, key):        # Returnt een Binary Search Tree van een lijst, gesorteerd op basis van key
    root = Node(lst[0], key)    # Neem de eerste element van de lijst, dit is de root van de tree
    for i in lst[1:]:           # Voor elke element in de lijst (behalve de eerste element)
        root.insert(i)          # Voeg dit element toe aan aan de tree
    return root




def draw(node):
    left = "none" if node.left is None else node.left.value[node.key]
    right = "none" if node.right is None else node.right.value[node.key]
    print(f"This is node #{node.value[node.key]} | left: {left} | right: {right}")
    if node.left is not None:
        draw(node.left)
    if node.right is not None:
        draw(node.right)


# for i in random.sample(range(100), 10):
#     print(f"The number {i} is {'' if root.search(i) else 'not '}in the tree")
