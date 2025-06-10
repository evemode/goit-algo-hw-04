def parse_input(user_input):
    '''parsing user's input'''
    cmd, *args = user_input.split() #separates command from users additional info -  name, number
    cmd = cmd.strip().lower() 
    return cmd, *args

def add_contact(args, contacts):
    '''adds contact to contacts. Check main.py'''
    name, phone = args
    contacts[name] = phone  #adding itself
    return "Contact added."

def change_contact(args, contacts):
    '''changes contact according to the info provided by user'''
    name, phone = args
    result = "Contact updated."
    if name in contacts.keys(): #checks if contact exists
        contacts.update({name:phone})
    else:
        result ='No contact found'
    return result

def show_phone(args, contacts):
    '''show contact :P'''
    name = args[0]
    result = 'No such contact'
    if name in contacts.keys(): #checks if contact exists
        result = contacts[name]
    return result

def show_all(contacts):
    '''shows all contacts user has'''
    for name, number in contacts.items():
        print(f'{name}: {number}')