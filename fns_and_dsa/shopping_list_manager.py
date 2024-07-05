def display_menu():
    print ("Shopping List Manager")
    print ("1. Add Item")
    print ("2. Remove Item")
    print ("3. View List")
    print ("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input ("Enter your choice: ")

        if choice == "1":
            item = ("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list")
        elif choice == "2":
            item = ("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print (item, "removed from list")
            else:
                print(item, "not found in the list")
        elif choice == "3":
            print (shopping_list)
        elif choice == "4":
            return()
        else:
            print ("Not a valid choice")
main()
