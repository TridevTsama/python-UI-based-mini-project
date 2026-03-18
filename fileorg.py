import tkinter as tk 
import os 
from tkinter import filedialog,messagebox 
import shutil 
class Fileorganizer:
    def __init__(self,root):
        self.root = root 
        self.root.title("File Organizer")
        self.root.geometry("500x300")
        tk.Label(root,text="Organize Files",font=("Arial",20)).pack(pady=15)
        tk.Button(root,text="select Folder",command=self.file_org).pack(pady=10)
    def file_org(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path,file)
            if not os.path.isfile(file_path):
                continue
            if "." not in file:
                continue 
            ext = file.split(".")[-1].lower()
            if ext in  ["jpeg","jpg","png"] :
                folder_name = "images"
            elif ext in ["mp4","mkv"]:
                folder_name = "Videos"
            elif ext in ["pdf"]:
                folder_name = "PDFS"
            elif ext in ["docx","txt"]:
                folder_name = "Document"
            else:
                folder_name = "others"
            dest_folder = os.path.join(folder_path,folder_name)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            shutil.move(file_path,os.path.join(dest_folder,file))
        messagebox.showinfo("Success","File Organized Succesfully")
root = tk.Tk()
app = Fileorganizer(root)
root.mainloop()