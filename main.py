import multiprocessing
from playsound import playsound
from tkinter import *
window = Tk()
window.title("Playsound")
window.geometry("500x500")
p = multiprocessing.Process(target=playsound, args=("karabo.mp3",))


def sound():
    p.start()


def stop():
    p.terminate()
    window.destroy()


play_button = Button(window, text="Play", font=("consolas 15 bold"), command=sound)
play_button.place(x=20, y=50)

stop_button = Button(window, text="Stop", font=("consolas 15 bold"), command=stop)
stop_button.place(x=100, y=50)


window.mainloop()
