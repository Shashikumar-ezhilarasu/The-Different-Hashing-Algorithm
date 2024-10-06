import tkinter as tk
from tkinter import messagebox

# Function to check for safe state using Banker's Algorithm
def is_safe(allocation, max_need, available, num_processes, num_resources):
    work = available[:]
    finish = [False] * num_processes
    safe_seq = []
    
    while len(safe_seq) < num_processes:
        allocated = False
        for i in range(num_processes):
            if not finish[i]:
                # Check if all resources of process i can be satisfied
                if all(max_need[i][j] - allocation[i][j] <= work[j] for j in range(num_resources)):
                    for j in range(num_resources):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_seq.append(i)
                    allocated = True
        
        if not allocated:
            return False, []

    return True, safe_seq

# Function for deadlock detection (simple approach)
def detect_deadlock(allocation, max_need, available, num_processes, num_resources):
    is_deadlock, _ = is_safe(allocation, max_need, available, num_processes, num_resources)
    if is_deadlock:
        messagebox.showinfo("Status", "No Deadlock Detected")
    else:
        messagebox.showwarning("Status", "Deadlock Detected")

# Function to display the results of Banker's Algorithm
def check_deadlock():
    num_processes = int(process_entry.get())
    num_resources = int(resource_entry.get())
    
    allocation = [[int(allocation_entries[i][j].get()) for j in range(num_resources)] for i in range(num_processes)]
    max_need = [[int(max_need_entries[i][j].get()) for j in range(num_resources)] for i in range(num_processes)]
    available = [int(available_entry[j].get()) for j in range(num_resources)]
    
    # Check for safe state
    is_safe_state, safe_seq = is_safe(allocation, max_need, available, num_processes, num_resources)
    
    if is_safe_state:
        result_label.config(text="System is in a safe state. Safe Sequence: " + str(safe_seq))
    else:
        result_label.config(text="System is not in a safe state (Deadlock may occur)")

# Initialize the GUI
root = tk.Tk()
root.title("Deadlock Detection and Prevention")

# Number of processes and resources
tk.Label(root, text="Number of Processes:").grid(row=0, column=0)
process_entry = tk.Entry(root)
process_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Resources:").grid(row=1, column=0)
resource_entry = tk.Entry(root)
resource_entry.grid(row=1, column=1)

# Matrix for resource allocation
tk.Label(root, text="Resource Allocation Matrix").grid(row=2, column=0, columnspan=2)
allocation_entries = []

# Matrix for maximum resource need
tk.Label(root, text="Maximum Resource Need Matrix").grid(row=4, column=0, columnspan=2)
max_need_entries = []

# Available resources
tk.Label(root, text="Available Resources:").grid(row=6, column=0)
available_entry = []

def create_matrix_entries():
    num_processes = int(process_entry.get())
    num_resources = int(resource_entry.get())
    
    # Clear old entries
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 3:
            widget.grid_forget()

    # Create allocation matrix entries
    global allocation_entries, max_need_entries, available_entry
    allocation_entries = [[tk.Entry(root, width=5) for _ in range(num_resources)] for _ in range(num_processes)]
    for i in range(num_processes):
        for j in range(num_resources):
            allocation_entries[i][j].grid(row=3+i, column=j)

    # Create maximum need matrix entries
    max_need_entries = [[tk.Entry(root, width=5) for _ in range(num_resources)] for _ in range(num_processes)]
    for i in range(num_processes):
        for j in range(num_resources):
            max_need_entries[i][j].grid(row=5+i, column=j)

    # Create available resources entries
    available_entry = [tk.Entry(root, width=5) for _ in range(num_resources)]
    for j in range(num_resources):
        available_entry[j].grid(row=7, column=j)

tk.Button(root, text="Set Matrices", command=create_matrix_entries).grid(row=8, column=0, columnspan=2)

# Button to check for deadlock and prevention
tk.Button(root, text="Check for Deadlock", command=check_deadlock).grid(row=9, column=0, columnspan=2)
tk.Button(root, text="Detect Deadlock", command=lambda: detect_deadlock(allocation_entries, max_need_entries, available_entry, int(process_entry.get()), int(resource_entry.get()))).grid(row=10, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=2)

root.mainloop()
