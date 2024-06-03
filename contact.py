import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []
        self.load_contacts()

        # UI Components
        self.label_title = tk.Label(root, text="Contact Manager", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=5)

        self.button_add = tk.Button(self.frame_buttons, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=0, column=0, padx=5)

        self.button_view = tk.Button(self.frame_buttons, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=0, column=1, padx=5)

        self.button_edit = tk.Button(self.frame_buttons, text="Edit Contact", command=self.edit_contact)
        self.button_edit.grid(row=0, column=2, padx=5)

        self.button_delete = tk.Button(self.frame_buttons, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=0, column=3, padx=5)

    def load_contacts(self):
        if os.path.exists("contacts.csv"):
            with open("contacts.csv", newline='') as csvfile:
                reader = csv.reader(csvfile)
                self.contacts = list(reader)

    def save_contacts(self):
        with open("contacts.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.contacts)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if name:
            phone = simpledialog.askstring("Input", "Enter contact phone number:")
            email = simpledialog.askstring("Input", "Enter contact email address:")
            if phone and email:
                self.contacts.append([name, phone, email])
                self.save_contacts()
                messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contacts_str = "\n".join([f"{i+1}. {c[0]}, {c[1]}, {c[2]}" for i, c in enumerate(self.contacts)])
        if contacts_str:
            messagebox.showinfo("Contact List", contacts_str)
        else:
            messagebox.showinfo("Contact List", "No contacts found.")

    def edit_contact(self):
        try:
            index = int(simpledialog.askstring("Input", "Enter the contact number to edit:")) - 1
            if 0 <= index < len(self.contacts):
                name = simpledialog.askstring("Input", "Enter new contact name:", initialvalue=self.contacts[index][0])
                phone = simpledialog.askstring("Input", "Enter new contact phone number:", initialvalue=self.contacts[index][1])
                email = simpledialog.askstring("Input", "Enter new contact email address:", initialvalue=self.contacts[index][2])
                if name and phone and email:
                    self.contacts[index] = [name, phone, email]
                    self.save_contacts()
                    messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Invalid contact number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def delete_contact(self):
        try:
            index = int(simpledialog.askstring("Input", "Enter the contact number to delete:")) - 1
            if 0 <= index < len(self.contacts):
                confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {self.contacts[index][0]}?")
                if confirm:
                    self.contacts.pop(index)
                    self.save_contacts()
                    messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showerror("Error", "Invalid contact number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
