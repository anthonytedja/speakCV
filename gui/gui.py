from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

def handle_start():
    print("start")

def handle_apply():
    print(ent_mute_time.get())
    print(is_debug.get())
    print("apply")

def handle_restore_default():
    print("default")


if __name__ == "__main__":
    window = Tk()
    window.geometry("600x400")
    window.title("SpeakCV")

    frm_options = Frame(master=window, relief=FLAT, borderwidth=2)

    png_logo = Image.open("./logo.png")
    png_logo = png_logo.resize((300, 180), Image.ANTIALIAS)
    img_logo = ImageTk.PhotoImage(png_logo)
    lbl_logo = ttk.Label(master=window, text="speakCV", image=img_logo)
    lbl_logo.image = img_logo
    btn_start = Button(master=window, text="Start", width=10, height=2, command=handle_start)
    
    btn_apply = ttk.Button(master=frm_options, text="Apply", command=handle_apply)
    lbl_mute_time = Label(master=frm_options, text="Mute Delay (seconds)")
    ent_mute_time = Entry(master=frm_options)
    ent_mute_time.insert(END, "5")
    #scale_mute_time = Scale(master=frm_options, from_=0, to=60, orient=HORIZONTAL)
    is_debug = BooleanVar()
    check_debug = ttk.Checkbutton(master=frm_options, text="Debug", variable=is_debug)

    lbl_logo.place(x=140, y=10)
    btn_start.place(x=80, y=250)
    btn_apply.place(x=40, y=120)
    lbl_mute_time.place(x=5, y=5)
    ent_mute_time.place(x=5, y=30)
    #scale_mute_time.place(x=50, y=50)
    check_debug.place(x=5, y=70)
    frm_options.place(x=300, y=200, width=160, height=160)

    window.mainloop()
