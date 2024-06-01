import tkinter as tk
from tkinter import filedialog, messagebox
from sorter.sorter import sort_files_by_type

class FileSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sorter")
        
        self.label = tk.Label(root, text="Select a folder to sort:")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.select_button.pack(pady=10)
        
        self.sort_button = tk.Button(root, text="Sort Files", command=self.sort_files)
        self.sort_button.pack(pady=10)
        
        self.folder_path = None

    def browse_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.label.config(text=f"Selected Folder: {self.folder_path}")

    def sort_files(self):
        if not self.folder_path:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return
        
        try:
            sort_files_by_type(self.folder_path)
            messagebox.showinfo("Success", "Files sorted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
