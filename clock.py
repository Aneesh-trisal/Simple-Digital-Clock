from tkinter import *  # Importing tkinter for GUI
from time import strftime  # Importing strftime to get the current time and date

# Create the main application window
root = Tk()
root.title("Digital Clock")  # Set window title
root.geometry("500x250")  # Set initial window size
root.configure(bg="black")  # Default to dark mode

# Function to update the time and date
def update_time():
    current_time = strftime("%H:%M:%S %p")  # Format: HH:MM:SS AM/PM
    current_date = strftime("%A, %d %B %Y")  # Format: Day, Date Month Year
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  # Update every second

# Function to center the window on the screen
def center_window():
    root.update_idletasks()  # Update window properties
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")  # Set new position

# Function to toggle between Dark and Light mode
def toggle_theme():
    global dark_mode
    if dark_mode:
        # Switch to Light Mode
        root.configure(bg="white")
        time_label.config(bg="white", fg="black")
        date_label.config(bg="white", fg="black")
        mode_button.config(text="☀️", bg="white", fg="black")  # Sun emoji
        dark_mode = False
    else:
        # Switch to Dark Mode
        root.configure(bg="black")
        time_label.config(bg="black", fg="white")
        date_label.config(bg="black", fg="white")
        mode_button.config(text="🌙", bg="black", fg="white")  # Moon emoji
        dark_mode = True

# Initialize the theme in Dark Mode
dark_mode = True

# Create and position labels
time_label = Label(root, font=("ds-digital", 60), bg="black", fg="white")  # Time Display
time_label.pack(anchor="center", pady=10)

date_label = Label(root, font=("Arial", 20), bg="black", fg="white")  # Date Display
date_label.pack(anchor="center")

# Create theme toggle button below the date label
mode_button = Button(root, text="🌙", font=("Arial", 16), command=toggle_theme, bd=0, padx=10, pady=5)
mode_button.pack(anchor="center", pady=10)

# Allow window resizing and center it on the screen
root.resizable(True, True)
center_window()

# Start updating time
update_time()

# Run the application
root.mainloop()
