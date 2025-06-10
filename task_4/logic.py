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