import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from sorter.sorter import sort_files_by_type
import os

class FileSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sorter")
        
        # Set up resizing behavior
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Create the main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Add image
        self.image = Image.open("logo.png")
        self.image = self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = ttk.Label(main_frame, image=self.photo)
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Add label
        self.label = ttk.Label(main_frame, text="Select a folder to sort:")
        self.label.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
        
        # Add buttons
        self.select_button = ttk.Button(main_frame, text="Browse", command=self.browse_folder)
        self.select_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.sort_button = ttk.Button(main_frame, text="Sort Files", command=self.sort_files)
        self.sort_button.grid(row=2, column=1, padx=10, pady=10)
        
        # Files listbox
        self.files_listbox = tk.Listbox(main_frame, height=10)
        self.files_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        
        # Status bar
        self.status = ttk.Label(root, text="Select a folder to start sorting.", relief=tk.SUNKEN, anchor="w")
        self.status.grid(row=1, column=0, sticky="ew")

        self.folder_path = None

    def browse_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.label.config(text=f"Selected Folder: {self.folder_path}")
            self.display_files()

    def display_files(self):
        self.files_listbox.delete(0, tk.END)
        files = os.listdir(self.folder_path)
        for file in files:
            self.files_listbox.insert(tk.END, file)

    def sort_files(self):
        if not self.folder_path:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return
        
        try:
            sort_files_by_type(self.folder_path)
            messagebox.showinfo("Success", "Files sorted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))