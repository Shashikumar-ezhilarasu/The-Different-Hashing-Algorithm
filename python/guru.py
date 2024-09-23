import tkinter as tk
from tkinter import messagebox

class HotelManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Hotel Management System")
        self.master.geometry("400x300")

        # Create main window widgets
        self.label = tk.Label(master, text="Hotel Management System", font=("Arial", 16))
        self.label.pack(pady=10)

        self.check_in_button = tk.Button(master, text="Check-in", command=self.check_in_window)
        self.check_in_button.pack(pady=5)

        self.check_out_button = tk.Button(master, text="Check-out", command=self.check_out_window)
        self.check_out_button.pack(pady=5)

    def check_in_window(self):
        check_in_window = tk.Toplevel(self.master)
        check_in_window.title("Check-in")
        check_in_window.geometry("300x250")

        # Guest Name Label and Entry
        self.guest_name_label = tk.Label(check_in_window, text="Guest Name:")
        self.guest_name_label.pack(pady=5)
        self.guest_name_entry = tk.Entry(check_in_window)
        self.guest_name_entry.pack(pady=5)

        # Room Number Label and Entry
        self.room_number_label = tk.Label(check_in_window, text="Room Number:")
        self.room_number_label.pack(pady=5)
        self.room_number_entry = tk.Entry(check_in_window)
        self.room_number_entry.pack(pady=5)

        # Confirm Check-in Button
        self.confirm_button = tk.Button(check_in_window, text="Confirm Check-in", command=self.check_in)
        self.confirm_button.pack(pady=10)

    def check_in(self):
        guest_name = self.guest_name_entry.get()
        room_number = self.room_number_entry.get()

        if guest_name and room_number:
            messagebox.showinfo("Check-in", f"{guest_name} has checked into room {room_number}")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")

    def check_out_window(self):
        check_out_window = tk.Toplevel(self.master)
        check_out_window.title("Check-out")
        check_out_window.geometry("300x200")

        # Room Number Label and Entry
        self.room_number_label = tk.Label(check_out_window, text="Room Number:")
        self.room_number_label.pack(pady=5)
        self.room_number_entry = tk.Entry(check_out_window)
        self.room_number_entry.pack(pady=5)

        # Confirm Check-out Button
        self.confirm_button = tk.Button(check_out_window, text="Confirm Check-out", command=self.check_out)
        self.confirm_button.pack(pady=10)

    def check_out(self):
        room_number = self.room_number_entry.get()

        if room_number:
            messagebox.showinfo("Check-out", f"Room {room_number} has been checked out.")
        else:
            messagebox.showwarning("Input Error", "Please enter the room number!")


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
