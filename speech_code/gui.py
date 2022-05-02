from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import threading

import speech_detection

def handle_start(delay, hasDebug):
    print("start")
    speech_detection.start(delay, hasDebug)

def handle_start_thread():
    global submit_thread
    submit_thread = threading.Thread(target=handle_start, args=(int(ent_mute_time.get()), is_debug.get()))
    submit_thread.daemon = True
    submit_thread.start()

# def handle_apply():
#     print(ent_mute_time.get())
#     print(is_debug.get())
#     print("apply")

# def handle_restore_default():
#     print("default")


if __name__ == "__main__":
    window = Tk()
    # style = ttk.Style(window)
    # style.theme_use('winnative')
    window.geometry("600x350")
    window.title("SpeakCV")
    is_debug = BooleanVar()

    frm_options = Frame(master=window, relief=FLAT, borderwidth=2)

    png_logo = Image.open("./logo.jpg")
    png_logo = png_logo.resize((300, 180), Image.ANTIALIAS)
    img_logo = ImageTk.PhotoImage(png_logo)
    lbl_logo = ttk.Label(master=window, text="speakCV", image=img_logo)
    lbl_logo.image = img_logo
    btn_start = Button(master=window, text="Start", width=10, height=2, command=handle_start_thread)
    
    #btn_apply = ttk.Button(master=frm_options, text="Apply", command=handle_apply)s
    lbl_mute_time = Label(master=frm_options, text="Mute Delay (secs):")
    ent_mute_time = Entry(master=frm_options,)
    ent_mute_time.insert(END, "5")
    #scale_mute_time = Scale(master=frm_options, from_=0, to=60, orient=HORIZONTAL)
    check_debug = ttk.Checkbutton(master=frm_options, text="Debug Frame", variable=is_debug)

    lbl_logo.place(x=140, y=10)
    btn_start.place(x=140, y=250)
    #btn_apply.place(x=40, y=120)
    lbl_mute_time.place(x=-5, y=43)
    ent_mute_time.place(x=120, y=45,width=20)
    #scale_mute_time.place(x=50, y=50)
    check_debug.place(x=-4, y=82)
    frm_options.place(x=300, y=200, width=160, height=160)

    window.mainloop()
