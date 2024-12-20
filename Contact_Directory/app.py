import json


class Contact():
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

        
    def __str__(self):
        return f'Name: {self.name} \nPhone: {self.phone} \nEmail: {self.email} \nAddress: {self.address}\n'
    
    
    def update_contact(self, new_name=None, new_phone=None, new_email=None, new_address=None):
        #TODO: Update to break name & address up by first and last, then address, city, state, zip code
        if new_name:
            self.name = new_name
        if new_phone:
            self.phone = new_phone
        if new_email:
            self.email = new_email
        if new_address:
            self.address = new_address
        
   
class Phonebook():
    def __init__(self, filename="conatcts.json"):
        self.contacts = {}
        self.filename = filename
        self.load_from_file()
        
    def add_contact(self, contact: Contact):
        self.contacts[contact.name] = contact
        self.save_to_file()
        
    
    def update_contact(self, name, new_name=None, new_phone=None, new_email=None, new_address=None):
        contact = self.search_contact(name)
        if contact:
            contact.update_contact(new_name, new_phone, new_email, new_address)
            
            if new_name and new_name != name:
                self.contacts[new_name] = self.contacts.pop(name)
            self.save_to_file()
            return True
        else:
            return False
    
    def search_contact(self, name):
        return self.contacts.get(name)
    
    def display_all(self):
        if not self.contacts:
            print("\nContacts list is empty\n")
        else:
            for name, contact in self.contacts.items():
                print(name)
                
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_to_file()
            print(f"\nContact '{name}' has been deleted successfully.\n")
            return True
        return False
    
    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(
                {name: vars(contact) for name, contact in self.contacts.items()}, 
                file,
                indent=4
            )
    
    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)
                self.contacts = {
                    name: Contact(**details) for name, details in contacts_data.items()
                }
        except FileNotFoundError:
            print("\n***ERROR: File not found.***\n")
        
def main():

    contacts_book = Phonebook()
    characters = ["~", "!", "@", "#", "$", '"',"%", "^", "&", "*", "(", ")", "_", "+", ":", "'", "[","]", "<", ">", ".", ",", "/", "?", "|"]
    
    while True:
        print("\n\n\nWelcome to your contact database!")
        print("Please choose from the following selections:\n\n")
        print("1. Search contact by name")
        print("2. Display all contacts")
        print("3. Add a new contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice here: ")
        while True:
            if choice == "1":
                print("\n***Contact search***")
                search = input("\nEnter contact name to search: ")
                contact = contacts_book.search_contact(search)
                if search.isdigit():
                    print("\nsearch does not accept numerical values.")
                    print("Please use alphabetical characters only.")
                    continue
                elif any (char in characters for char in search):
                    print("\nSearch does not accept these characters.")
                    print("Please use alphabetical characters only.")
                    continue
                elif contact:
                    print(f'\n{contact}')
                else:
                    print("\n***ERROR: Contact not found.***\n")
                search_more = input("Would you like to search another name?y/n: ")
                if search_more.lower() == 'y':
                    continue
                elif search_more.lower() == 'n':
                    break
                else:
                    print("Invalid input. Please try again.")
                    continue
                
            elif choice == "2":
                    print("\n***Display all contacts***")
                    contacts_book.display_all()
                    break
                    
            elif choice == "3":
                    print("\n***Add new contact***")
                    name = input("Enter the First and Last name: ")
                    phone = input("Enter the phone number: ")
                    email = input("Enter the email address: ")
                    address = input("Enter the address: ")
                    contact = Contact(name, phone, email, address)
                    contacts_book.add_contact(contact)
                    print("Contact was added successfully\n")
    
                    add_more = input("Would you like to add another contact? y/n: ")
                    if add_more == 'y':
                        continue
                    elif add_more == 'n':
                        break
                    else:
                        print("Invalid input. Please try again.")
                        
            elif choice == "4":
                print("\nUpdate contact information")
                name_contact = input("Enter the name of the contact you wish to update: ")
                contact = contacts_book.search_contact(name_contact)
                if contact:
                    new_name = input("Enter the new name (leave blank to keep current): ")
                    new_phone = input("Enter the new phone number (leave blank to keep current): ")
                    new_email = input("Enter the new email address (leave blank to keep current): ")
                    new_address = input("Enter the new address (leave blank to keep current): ")
                    contacts_book.update_contact(name_contact, new_name, new_phone, new_email, new_address)
                    print("Contact information was updated successfully\n")
                else:
                    print("\n***ERROR: Contact not found.***\n")

                while True:
                    new_update = input("Do you wish to update another contact? (y/n): ").lower()
                    if new_update == 'y':
                        break
                    elif new_update == 'n':
                        break 
                    else:
                        print("Invalid input. Please try again.")
                if new_update == 'n':
                    break
                     
            if choice == "5":
                print("\n***Delete a contact***")
                name = input("Enter the name of the contact you wish to delete: ")
                if contacts_book.delete_contact(name):
                    print("Contact was deleted successfully\n")
                else:
                    print("***ERROR: Contact not found.***\n")
                    delete_new = input("Would you like to delete another? y/n: ")
                    if delete_new.lower() == 'y':
                        continue
                    elif delete_new.lower() == 'n':
                        break
                    else:
                        print("Invalid input. Please try again.")
            
            elif choice == "6":
                end_program = input("Are you sure you want to exit?y/n: ")
                if end_program.lower() == 'y':
                    print("Goodbye")
                    return
                elif end_program.lower() == 'n':
                    continue
                else:
                    print("Invalid input. Please try again.")
            
   
if __name__ == "__main__": main()