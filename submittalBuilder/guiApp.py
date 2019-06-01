from tkinter import *
from tkinter import filedialog

filename = None

root = Tk()
Label(root, text='Submittal No. ').grid(row=0)
Label(root, text='Project Name ').grid(row=1)
Label(root, text='Product Name ').grid(row=2)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

def fileSelector():
    global filename
    root.withdraw()
    root.fileName = filedialog.askopenfilename()
    print(root.fileName)

Button(root, text='Select PDF file ', command=fileSelector).grid(row=3)

if __name__ == "__main__":
    mainloop()

