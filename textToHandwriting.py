from tkinter import *
import pywhatkit


def trasnfer():
	text = text_entry.get(1.0, END)
	pywhatkit.text_to_handwriting(text, rgb=(0, 0, 255))

root = Tk()
root.title("Nguyen")
root.geometry("750x500")
label = Label(root, text = "Text to handwriting", font = ('digital-7'), fg="green").pack(pady=10)

frame = Frame(root)
text_notifi = Label(frame, text = "Enter text: ", font = ("digital-7"), fg= "green").pack(side=LEFT)
text_entry = Text(frame, width = 50, height = 20)
text_entry.pack()
frame.pack(pady=10)
button = Button(frame, text = "Ok", font = ("digital-7"), command = trasnfer, width = 20).pack(pady=10)

root.mainloop()