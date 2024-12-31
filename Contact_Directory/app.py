import json

class Contact():
    def __init__(self, fname, lname, phone, email, address, city, state, zip):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

        
    def __str__(self):
        return f'Name: {self.fname} {self.lname} \nPhone: {self.phone} \nEmail: {self.email} \nAddress: {self.address} \nCity: {self.city} \nState: {self.state} \nZip Code: {self.zip}'
    
    def update_contact(self, new_fname=None, new_lname=None, new_phone=None, new_email=None, new_address=None, new_city=None, new_state=None, new_zip=None):
        
        if new_fname: self.fname = new_fname
        if new_lname: self.lname = new_lname
        if new_phone: self.phone = new_phone
        if new_email: self.email = new_email
        if new_address: self.address = new_address
        if new_city: self.city = new_city
        if new_state: self.state = new_state
        if new_zip: self.zip = new_zip
          
class Phonebook():
    
    def __init__(self, filename="conatcts.json"): 
        self.filename = filename
        self.contacts = self.load_from_file()
        
    def add_contact(self, contact):
        
        contact_key = f"{contact.fname}_{contact.lname}"
        
        if contact_key in self.contacts:
            print(f"Contact '{contact_key}' already exists. Adding failed.")
            return
        
        
        self.contacts[contact_key] = {
            "fname": contact.fname,
            "lname": contact.lname,
            "phone": contact.phone,
            "email": contact.email,
            "address": contact.address,
            "city": contact.city,
            "state": contact.state,
            "zip": contact.zip
        }
        self.save_to_file()
        
        print(f"Contact '{contact.fname} {contact.lname}' added successfully.")

    def update_contact(self, fname, lname, new_fname=None, new_lname=None, new_phone=None, new_email=None, new_address=None, new_city=None, new_state=None, new_zip=None):
        contact = self.search_contact(fname, lname)

        if not contact:
            print("Contact not found.")
            return False 

        
        contact.update_contact(new_fname, new_lname, new_phone, new_email, new_address, new_city, new_state, new_zip)

        
        contact_key = f"{new_fname or fname}_{new_lname or lname}"
        self.contacts[contact_key] = {
            "fname": contact.fname,
            "lname": contact.lname,
            "phone": contact.phone,
            "email": contact.email,
            "address": contact.address,
            "city": contact.city,
            "state": contact.state,
            "zip": contact.zip
        }

        
        if new_fname and new_lname and (new_fname, new_lname) != (fname, lname):
            old_key = f"{fname}_{lname}"
            if old_key in self.contacts:
                del self.contacts[old_key]

        self.save_to_file()
        return True


    def search_contact(self, fname, lname):
        for contact_key, contact_data in self.contacts.items():
            if contact_data["fname"] == fname and contact_data["lname"] == lname:
                
                return Contact(contact_data["fname"], contact_data["lname"], contact_data["phone"], contact_data["email"], contact_data["address"], contact_data["city"], contact_data["state"], contact_data["zip"])
        return None  
    
    def display_all(self):
        if not self.contacts:
            print("\nContacts list is empty\n")
        else:
            for name, contact in self.contacts.items():
                print(contact['fname']+" "+contact['lname'])
                    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_to_file()
            print(f"\nContact '{name}' has been deleted successfully.\n")
            return True
        return False
    
    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)
        # print("Contacts saved:", self.contacts)  # Add this line for debugging
        
class UserInputs():
    
    def greeting(self):
        print("\n**Welcome to the Pheonix Contact Database**\n")
        print("Please choose from the selection below\n")

    def searchAll(self):
       
        error = "Invalid input"
        not_found = "Contact not found"
        contacts_book = Phonebook("contacts.json")
       
        while True:
            print("\nSearch by name: ")
            search = input("\nEnter Full Name: ")
            if len(search.split()) != 2:
                print(f"{error}: Please enter First and Last Name.")
                continue
            fname, lname = search.split()
            contact = contacts_book.search_contact(fname, lname)
            if contact:
                print(f'{contact}')   
            else: 
                print(not_found)
            
            search_more = input("\nWould you like to search another name? (y/n): ")
            
            if search_more.lower() == 'y':
                continue
            if search_more.lower() =='n':
                break
            else:
                print(error)
                continue
    
    def display(self):
        
        contacts_book = Phonebook("contacts.json")
        
        print("\n***Displaying Contacts***")
        
        contacts_book.display_all()   
            
    def add(self):
        added = "Contact Added: "
        error = "Invalid Input"
        contacts_book = Phonebook("contacts.json")

        while True:
            print("\n***Add Contact***")
            print("\nPress the <ENTER> key to proceed to the next line")

            while True:
                fname = input("\nFirst Name: ")
                lname = input("Last Name: ")
                if len(fname) <= 2 or len(lname) <= 2:
                    print(error)
                    print("Names must be at longer than 2 characters.")
                    
                    add_more = input("Would you like to try adding another contact? (y/n): ")
                    if add_more.lower() == 'y':
                        continue
                    elif add_more.lower() == 'n':
                        break
                    else:
                        print(error)
                        continue
                else:
                    while True:
                        phone = input("Phone Number: ")
                        if len(phone) == 10 and phone.isdigit():
                            break
                        else:
                            print(error)
                            print("Phone number must be 10 digits.")
                            
                while True:
                    email = input("Email Address: ")
                    if '@' in email and '.com' in email:
                        break
                    else:
                        print(error)
                        print("Email address must contain '@' and '.com').") 

                address = input("Street Address: ")
                city = input("City/Town: ")

                while True:        
                    state = input("State (VT, MA, etc.): ")
                    if len(state) == 2 and state.isalpha() and state.isupper():
                        break
                    else:
                        print(error)
                        print("State must only consist of two uppercase letters.")
                while True:
                    zip_code = input("Zip Code: ")
                    if len(zip_code) >= 5 and zip_code.isdigit():
                        break
                    elif not zip_code.isdigit():
                        print(error)
                        print("Zip code must be in digits.")
                    else:
                        print(error)
                        print("Zip code must be 5 or more digits.")

                contact = Contact(fname, lname, phone, email, address, city, state, zip_code)
                contacts_book.add_contact(contact)
                print(f"\n{added}: {fname} {lname}")
                
                add_more = input("Add another contact? (y/n): ")
                if add_more.lower() == 'y':
                    break
                elif add_more.lower() == 'n':
                    add_more = False
                    break
                else:
                    print(error)
                    continue

            if not add_more:
                break

    def update(self):
        
        updated = "Updated Contact:"
        not_found = "Contact not found"
        error = "Invalid Input"
        contacts_book = Phonebook("contacts.json")
        
        while True:
            print("\n***Update Contacts***")

            search = input("\nEnter Full Name: ")
            if len(search.split()) != 2:
                print(f"{error}: Please enter First and Last Name.")
                continue
            fname, lname = search.split()
            contact = contacts_book.search_contact(fname, lname)
            if contact: # See if we cant do these inputs 
                print("Please enter the new information below.\n")
                print("**If you wish to leave an entry unchanged, press <ENTER>**")
                print("Press <ENTER> to continue:")
                new_fname = input("\nFirst Name: ")
                new_fname = new_fname if new_fname else contact.fname
                new_lname = input("Last Name: ")
                new_lname = new_lname if new_lname else contact.lname
                new_phone = input("Phone Number: ")
                new_phone = new_phone if new_phone else contact.phone
                new_email = input("Email Address: ")
                new_email = new_email if new_email else contact.email
                new_address = input("Street Address: ")
                new_address = new_address if new_address else contact.address
                new_city = input("City/Town: ")
                new_city = new_city if new_city else contact.city
                new_state = input("State(VT,MA, etc.): ")
                new_state = new_state if new_state else contact.state
                new_zip = input("Zip Code: ")
                new_zip = new_zip if new_zip else contact.zip
                contacts_book.update_contact(fname, lname, new_fname, new_lname, new_phone, new_email, new_address, new_city, new_state, new_zip)
                print(f"\n{updated} {new_fname or contact.fname} {new_lname or contact.lname} to the database")
            else:
                print(not_found)
            
            new_update = input("Update another contact? (y/n): ")
            
            if new_update == 'y':
                continue
            elif new_update == 'n':
                break
            else:
                print(error)
    
    def delete(self):
        delete = "Deleted Contact:"
        error = "Invalid Input"
        contacts_book = Phonebook("contacts.json")

        while True:
            print("\n***Delete Contacts***")

            search = input("\nEnter Full Name: ").strip()
            if len(search.split()) != 2:
                print(f"{error}: Please enter First and Last Name.")
                continue
            try:
                fname, lname = search.split()
            except ValueError:
                print(error)
                continue
            
            contact_key = f"{fname}_{lname}"

            if contact_key in contacts_book.contacts:
                confirm = input("Are you sure you want to delete this contact? (y/n): ")
                if confirm == 'y':
                    if contacts_book.delete_contact(contact_key):
                        print(f"{delete} {fname} {lname} from the database")
                else:
                    print("Deletion canceled.")
            else:
                print("Contact not found.")

            delete_new = input("Delete another contact? (y/n): ")
            if delete_new == 'n':
                break
            elif delete_new != 'y':
                print(error)
                break
                
    def exit(self):
        
        error = "Invalid Input"
        while True:
            end_program = input("Are you sure to want to exit? (y/n): ")

            if end_program.lower() == 'y':        
                print("\nProgram Terminated,")
                print("\n    Goodbye")
                return
            elif end_program.lower() == 'n':
                continue    
            else:
                print(error)
            
            
def main():

    while True:
        UserInputs().greeting()
        print("1: Search contacts")
        print("2: Display all Contacts")
        print("3: Add Contact")
        print("4: Update Contact")
        print("5: Delete Contact")
        print("6: Exit")


        choice = input("\nEnter your choice here: ")

        if choice == "1":
            UserInputs().searchAll()
        elif choice == "2":
            UserInputs().display()
        elif choice == "3":
            UserInputs().add()
        elif choice == "4":
            UserInputs().update()
        elif choice == "5":
            UserInputs().delete()
        elif choice == "6":
            UserInputs().exit()
            break
               
if __name__ == "__main__": main()
