from docx import Document
import win32com.client as client
import os

current_directory = os.getcwd()

document = Document()


paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')

document.save('test.docx')

# convert to pdf src: https://github.com/python-openxml/python-docx/issues/113
def convert_to_pdf(filepath:str):
    """Save a pdf of a docx file."""    
    try:
        word = client.DispatchEx("Word.Application")
        target_path = filepath.replace(".docx", r".pdf")
        word_doc = word.Documents.Open(filepath)
        word_doc.SaveAs(target_path, FileFormat=17)
        word_doc.Close()
    except:
        print("huh")
    finally:
        word.Quit()


convert_to_pdf(current_directory + "/" + "test.docx")

'''
TODO:
Create template submittal page in .docx
Edit submittal page for desiredf submittal number
Overlay on arbitrary numbers of submittals

Challenge: How can we input the desired submittal number intuitively?

hard code project name, append to word doc
input: submittal #
-> check return number, are you sure y/n?
append to word doc
get current date with python datetime package, append to word doc
delete word doc
'''