
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


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
    """Remove from the inventory dictionary a list of items from removed_items."""
    pass


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
    display_inventory(inventory)
    add_to_inventory(inventory, ['dagger', 'shield', 'bread', 'torch', 'dagger'])
    display_inventory(inventory)