def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    result = "Contact updated."
    if name in contacts.keys():
        contacts.update({name:phone})
    else:
        result ='No contact found'
    return result

def show_phone(args, contacts):
    name = args[0]
    result = 'No such contact'
    if name in contacts.keys():
        result = contacts[name]
    return result

def show_all(contacts):
    #return contacts.items()
    for name, number in contacts.items():
        print(f'{name}: {number}')

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) 
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case 'phone':
                print(show_phone(args, contacts))
            case 'all':
                show_all(contacts)
            case _:
                print("Invalid command.")
if __name__ == "__main__":
    main()
