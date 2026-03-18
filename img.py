import tkinter as tk 
from PIL import Image, ImageChops 
from tkinter  import messagebox,filedialog 
class imagecomparisiontool:
    def __init__(self,root):
        self.root = root 
        self.root.title("Image Comprasion Tool")
        self.root.geometry("400x250")
        self.ref_img = ""
        self.act_img = ""
        tk.Label(root,text="Image Comp Tool",font=("Arial",12)).pack(pady=15)
        tk.Button(root,text="Upload ref Image",command=self.referal_img).pack(pady=5)
        tk.Button(root,text="Upload Actual Image",command=self.actual_img).pack(pady=5)
        tk.Button(root,text="Compare Images",command=self.compare_img).pack(pady=15)
    def referal_img(self):
        self.ref_img = filedialog.askopenfilename(title="Select Referal Image")
    def actual_img(self):
        self.act_img = filedialog.askopenfilename(title="Select Actual Image")
    def compare_img(self):
        if not self.ref_img or not  self.act_img:
            messagebox.showerror("Error"," Please Upload both  images")
            return 
        image1 = Image.open(self.ref_img)
        image2 = Image.open(self.act_img)
        w1,h1 = image1.size 
        w2,h2 = image2.size 
        resolution_result = ""
        if (w1,h1) == (w2,h2):
            resolution_result = f"Resolution SAME \n Reference:{w1}x{h1} \n Actual:{w2}x{h2}"
        else:
            resolution_result = f"Resolution Different \n Reference:{w1}x{h1} \n Actual:{w2}x{h2}"
        diff = ImageChops.difference(image1,image2)
        if diff.getbbox() is None:
          pixel_result = "Pixel SAME \n Pixel Difference: 0%"
          final_result = "Images are SAME"
        else:
          pixel_result = "Pixel DIFFERENT"
          final_result = "Images are NOT SAME"
        messagebox.showinfo("Comparison Result",f"{final_result}\n\n{resolution_result}\n\n{pixel_result}")
root = tk.Tk()
app = imagecomparisiontool(root)
root.mainloop()