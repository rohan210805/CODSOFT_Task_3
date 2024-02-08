import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        
        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.master, text="Name:", font='Arial 14', fg='dark orange')
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry_var = tk.StringVar()
        self.name_entry = tk.Entry(self.master, textvariable=self.name_entry_var, font='Arial 10 bold')
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(self.master, text="Phone:", font='Arial 14', fg='dark orange')
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_entry_var = tk.StringVar()
        self.phone_entry = tk.Entry(self.master, textvariable=self.phone_entry_var, font='Arial 10 bold')
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.master, text="Add", command=self.add_contact, font='Arial 12 bold', bg ='orange', fg='black')
        self.add_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.contacts_tree = ttk.Treeview(self.master, columns=('Name', 'Phone'), show='headings')
        self.contacts_tree.heading('Name', text='Name')
        self.contacts_tree.heading('Phone', text='Phone')
        self.contacts_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.update_button = tk.Button(self.master, text="Update", command=self.update_contact, font='Arial 12 bold', bg ='orange', fg='black')
        self.update_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_contact, font='Arial 12 bold', bg ='orange', fg='black')
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(self.master, text="View Contacts", command=self.view_contacts, font='Arial 12 bold', bg ='orange', fg='black')
        self.view_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.search_label = tk.Label(self.master, text="Search:", font='Arial 14', fg='dark orange')
        self.search_label.grid(row=7, column=0, sticky="e")
        self.search_entry_var = tk.StringVar()
        self.search_entry = tk.Entry(self.master, textvariable=self.search_entry_var, font='Arial 10 bold')
        self.search_entry.grid(row=7, column=1)

        self.search_button = tk.Button(self.master, text="Search", command=self.search_contact, font='Arial 12 bold', bg ='orange', fg='black')
        self.search_button.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry_var.get()
        phone = self.phone_entry_var.get()
        if name and phone:
            if self.validate_phone(phone):
                self.contacts[name] = phone
                self.contacts_tree.insert('', 'end', values=(name, phone))
                messagebox.showinfo("Success", "Contact added successfully!")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Invalid phone number format!")
        else:
            messagebox.showerror("Error", "Name and Phone cannot be empty!")

    def validate_phone(self, phone):
        # Basic phone number validation for demonstration
        # You may enhance this according to your needs
        return phone.isdigit() and len(phone) >= 8  # Example: Accepts only digits and at least 8 characters

    def update_contact(self):
        selected_item = self.contacts_tree.selection()
        if selected_item:
            name = self.name_entry_var.get()
            phone = self.phone_entry_var.get()
            if name and phone:
                if self.validate_phone(phone):
                    old_name = self.contacts_tree.item(selected_item, 'values')[0]
                    self.contacts[old_name] = (name, phone)
                    self.contacts_tree.item(selected_item, values=(name, phone))
                    messagebox.showinfo("Success", f"Contact '{old_name}' updated successfully!")
                    self.clear_entries()
                else:
                    messagebox.showerror("Error", "Invalid phone number format!")
            else:
                messagebox.showerror("Error", "Name and Phone cannot be empty!")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_item = self.contacts_tree.selection()
        if selected_item:
            name = self.contacts_tree.item(selected_item, 'values')[0]
            del self.contacts[name]
            self.contacts_tree.delete(selected_item)
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{name}: {phone}" for name, (name, phone) in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available!")

    def search_contact(self):
        search_name = self.search_entry_var.get()
        found = False
        for item in self.contacts_tree.get_children():
            name = self.contacts_tree.item(item, 'values')[0]
            if search_name.lower() in name.lower():
                found = True
                self.contacts_tree.selection_set(item)
                self.contacts_tree.focus(item)
                messagebox.showinfo("Contact Found", f"Contact '{name}': {self.contacts[name]}")
                break
        if not found:
            messagebox.showinfo("Contact Not Found", f"No contact found with name '{search_name}'")

    def clear_entries(self):
        self.name_entry_var.set('')
        self.phone_entry_var.set('')

def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()
