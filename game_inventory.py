def display_inventory(inventory):
    for key, value in inventory.items(): 
        print(f'{key}: {value}')


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


def print_table(inventory, order=None):
    print("""-----------------
item name | count
-----------------""")
    if order == 'count,asc' or order == 'count,desc':
        list_of_tuples = sorted(inventory.items(), key=lambda x: x[1])
    if order == 'count,asc':
        for tuple in list_of_tuples: 
            print(str.rjust(str(tuple[0]), 9), "|", str.rjust(str(tuple[1]), 5))
    elif order == 'count,desc':
        for i in range(len(list_of_tuples)-1, -1, -1):
            print(str.rjust(str(list_of_tuples[i][0]), 9), "|", str.rjust(str(list_of_tuples[i][1]), 5))
    else:
        for key, value in inventory.items():
            print(str.rjust(str(key), 9), "|", str.rjust(str(value), 5))
    print("""-----------------""")


def import_inventory(inventory, filename="import_inventory.csv"):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    else:
        content_of_file_as_list = f.read().split(",")
        add_to_inventory(inventory, content_of_file_as_list)
        f.close()


def export_inventory(inventory, filename="export_inventory.csv"):
    try:
        f = open(filename, "w")
    except IOError:
        print(f'You don\'t have permission creating file \'{filename}\'!')
    else:
        f = open(filename, "w")
        f.write('')
        f.close()
        f = open(filename, "a")
        inventory_list = []
        for key, value in inventory.items():
            for i in range(value):
                inventory_list.append(key)
        inventory_string = ",".join(inventory_list)
        f.write(inventory_string)
        f.close()


if __name__ == "__main__":
    inventory = {'rope': 1, 'torch': 6, 'blanket': 3, 'gold coin': 2}
    import_inventory(inventory, "not_exists.csv")