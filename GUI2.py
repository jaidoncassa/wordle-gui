import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show an information message box
messagebox.showinfo("Information", "This is an example of an info message box.")

# Main loop (required for the message box to appear)
root.mainloop()
