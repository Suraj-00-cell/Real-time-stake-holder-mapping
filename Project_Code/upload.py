import tkinter as tk
from tkinter import filedialog
import pandas as pd

def browse_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    
    # Read the selected file into a DataFrame
    df = pd.read_excel(file_path)
    return df
# Create the Tkinter root window
root = tk.Tk()

# Create a button for browsing files
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()
