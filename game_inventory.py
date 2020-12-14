def display_inventory(inventory):
    for key, value in inventory.items(): 
        print(f'{key}, {value}')


def add_to_inventory(inventory, added_items):
    for element in added_items:
        if element in inventory.keys():
            inventory[element] += 1
        else:
            inventory[element] = 1


def remove_from_inventory(inventory, removed_items):
    for element in removed_items:
        if element in inventory.keys():
            inventory[element] -= 1
            if inventory[element] <= 0:
                del inventory[element]


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass


if __name__ == "__main__":
    inventory = {'rope': 1, 'torch': 6, 'blanket': 3}
    
    remove_from_inventory(inventory, ['blanket', 'torch', 'rope', 'torch', 'blanket'])
    display_inventory(inventory)