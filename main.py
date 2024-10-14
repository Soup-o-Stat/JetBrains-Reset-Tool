import tkinter as tk
from tkinter import messagebox
import subprocess
import getpass
import os
import random


def run_reset_trial():
    command = r'reg delete "HKEY_CURRENT_USER\Software\JavaSoft" /f'
    user_name = getpass.getuser()
    file_path = f"C:/Users/{user_name}/AppData/Roaming/JetBrains/PermanentUserId"

    try:
        subprocess.run(command, shell=True, check=True)
        if os.path.exists(file_path):
            os.remove(file_path)
            messagebox.showinfo("Success", "The reset was successful!")
        else:
            messagebox.showwarning("Warning", "Reset error")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Reset error")


def change_button_color():
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    brightness = (random_color[1:3], random_color[3:5], random_color[5:7])
    if sum(int(c, 16) for c in brightness) < 383:
        random_color = f'#{random.randint(200, 255):02x}{random.randint(200, 255):02x}{random.randint(200, 255):02x}'

    reset_button.config(fg=random_color)
    root.after(1000, change_button_color)

root = tk.Tk()
root.title("JetBrains Reset Tool by Soup-o-Stat")
root.geometry("854x480")
root.wm_attributes('-alpha', 0.8)
root.wm_attributes('-topmost', True)

root.configure(bg='#012142')

frame = tk.Frame(root, bg='#000a14', bd=5, relief='ridge')
frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.9, relheight=0.8)

reset_button = tk.Button(frame, text="Reset Trial", command=run_reset_trial,
                         bg='#444444', fg='#00FFCC', font=("Arial", 16),
                         width=20, height=2, activebackground='#555555')

reset_button.pack(pady=20)

reset_button.config(bg='#444444')

change_button_color()

root.mainloop()
