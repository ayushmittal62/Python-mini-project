from tkinter import *
from textblob import TextBlob


def checkSpelling():
    a = text.get()
    b = TextBlob(a)
    corrected_text.set("The Corrected Sentence is:\n" + str(b.correct()))


# Creating GUI
wn = Tk()
wn.title("Spelling Checker")
wn.geometry("700x450")
wn.config(bg="SlateGray1")

# Making input variables
text = StringVar(wn)
corrected_text = StringVar(wn)

# Title label
Label(
    wn,
    text="Spelling Checker",
    bg="SlateGray1",
    fg="gray30",
    font=("Times", 40, "bold"),
).place(x=10, y=10)

# Input prompt label
Label(
    wn,
    text="Enter the words: ",
    bg="SlateGray1",
    font=("calibre", 17, "normal"),
    anchor="e",
    justify=LEFT,
).place(x=10, y=100)

# Entry widget for user input
Entry(wn, textvariable=text, width=35, font=("calibre", 13, "normal")).place(
    x=190, y=106
)

# Label to display corrected text
result_label = Label(
    wn,
    textvariable=corrected_text,
    bg="SlateGray1",
    anchor="w",
    font=("calibre", 13, "normal"),
    justify=LEFT,
    wraplength=680,  # This makes the text wrap at 680 pixels
)
result_label.place(x=10, y=150)

# Submit button
Button(
    wn, text="Submit", bg="SlateGray4", font=("calibre", 20), command=checkSpelling
).place(x=300, y=400)

# Run the main loop
wn.mainloop()
