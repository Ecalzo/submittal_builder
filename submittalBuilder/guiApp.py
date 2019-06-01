from tkinter import *
from tkinter import filedialog
from coverPageBuilder import buildCoverPage
filename = None

root = Tk()
Label(root, text='Submittal No. ').grid(row=0)
Label(root, text='Project Name ').grid(row=1)
Label(root, text='Product Name ').grid(row=2)
subNo = Entry(root)
projName = Entry(root)
prodName = Entry(root)
subNo.grid(row=0, column=1)
projName.grid(row=1, column=1)
prodName.grid(row=2, column=1)

def selectAndProcess():
    # root.fileName = filedialog.askopenfilename()
    # print(root.fileName)
    submittal_num = subNo.get()
    project_name = projName.get()
    product_name = prodName.get()

    buildCoverPage(submittal_num, project_name, product_name)


Button(root, text='Select PDF file ', command=selectAndProcess).grid(row=3)


if __name__ == "__main__":
    mainloop()

