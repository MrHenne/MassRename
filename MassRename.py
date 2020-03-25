import os
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

# create program as window
window = Tk()
# test

# define window properties
window.title("MassRename")
window.geometry('570x260')

# create title and subtitle
label_title = Label(window, anchor="center",text="Mass Rename", font=("",30))
label_title.grid(sticky=(E+W), column=0, columnspan=2, row=0, padx=10)
label_subtitle = Label(window, anchor="center", text="Henne v0.1", font=("",10))
label_subtitle.grid(sticky=(E+W), column=0, columnspan=2, row=1, padx=10)

# blank line
label_blank = Label(window, text="", width=50)
label_blank.grid(column=0, columnspan=2, row=3)

# create text field for file prefixes
label_prefix = Label(window, anchor="e", text="Desired file names:")
label_prefix.grid(sticky=(W+E), column=0, row=5, ipady=5, padx=10)
text_prefix = Entry(window, width=70)
text_prefix.grid(sticky=W, column=1, row=5, padx=10)

# create text field for field extensions
label_extension = Label(window, anchor="e", text="File extension:")
label_extension.grid(sticky=(W+E), column=0, row=7, ipady=5, padx=10)
combo_extension = Combobox(window, width=10, state='readonly')
combo_extension['values'] = (".txt",".jpg",".pdf",".exe",".py")
combo_extension.grid(sticky=W, column=1, row=7, padx=10)

def btn_filediag():
    user_directory = filedialog.askdirectory()
    user_directory = user_directory + "/"
    text_filediag.delete(0, END)
    text_filediag.insert(END, user_directory)

# create file browser dialog
button_filediag = Button(window, width=10, command=btn_filediag, text="Select Directory:")
button_filediag.grid(sticky=(W+E), column=0, row=9, padx=10)
text_filediag = Entry(window, width=70, text="sdf")
text_filediag.grid(sticky=W, column=1, row=9, padx=10)

# create function to carry out rename
def massRename():

    desiredName = text_prefix.get()
    desiredFileExtension = combo_extension.get()
    desiredDirectory = text_filediag.get()
    print(desiredName)
    print(desiredFileExtension)
    print(desiredDirectory)

    i = 0
    for filename in os.listdir(desiredDirectory): # for each file in directory
        dst = desiredName + str(i) + desiredFileExtension
            # new file name is desired name plus string number plus extension
        src = desiredDirectory + filename
            # source is directory plus found file
        dst = desiredDirectory + dst
            # new file path and name is ./directory/newfilename

        # carry out the renaming process
        os.rename(src, dst)
        # cycle through to next file
        i += 1

    label_subtitle.configure(text="Renaming complete")

    print("Mass rename complete")


button_finish = Button(window, width=30, command=massRename, text="Rename")
button_finish.grid(sticky=W+E, column=0, columnspan=2, row=10, padx=10, pady=30)



# finish and create window


window.mainloop()
