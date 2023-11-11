my_list = []
def display_list():
    if not my_list:
        print("The list is empty.")
    else:
        print("List contents:")
        for item in my_list:
            print(item)
def add_item():
    item = input("Enter the item to add: ")
    my_list.append(item)
    print(f"{item} has been added to the list.")


def remove_item():
    item = input("Enter the item to remove: ")
    if item in my_list:
        my_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} not found in the list.")


def search_item():
    item = input("Enter the item to search for: ")
    if item in my_list:
        print(f"{item} is in the list.")
    else:
        print(f"{item} is not in the list.")


while True:
    print("\nList Application Menu:")
    print("1. Display List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        display_list()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        search_item()
    elif choice == '5':
        print("Thank You")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")