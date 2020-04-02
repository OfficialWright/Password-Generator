from tkinter import *
import random

# Application gui
def gui():
    # Setting up the TK gui and options
    r = Tk()
    r.resizable(width=False, height=False)
    r.geometry("450x125")
    r.title('Password Generator')

    # Creating frames for the content in the gui
    contentframe = Frame(r)
    contentframe.place(relx=.5, rely=.5, anchor=CENTER)

    topframe = Frame(contentframe)
    topframe.pack()

    bottomframe = Frame(contentframe)
    bottomframe.pack()

    # Creating content for the application
    passwordlabel = Label(topframe, text='Password:')
    textentry = Entry(topframe, width=42, borderwidth=2, justify='center', state='readonly', fg="green")
    clipbutton = Button(topframe, text='Copy', command=lambda: copy(r, textentry, clipbutton))
    genbutton = Button(bottomframe, text='Generate', command=lambda: generator(textentry, clipbutton))
    canbutton = Button(bottomframe, text='Close', command=lambda: close(r))

    # Showing the content to the apllications frame
    passwordlabel.pack(side=LEFT, padx=5)
    textentry.pack(side=LEFT)
    clipbutton.pack(side=LEFT, padx=5)
    genbutton.pack(side=LEFT, padx=10)
    canbutton.pack(side=LEFT, padx=10)
    r.mainloop()

# Copying the password from the entry box
def copy(r, textentry, clipbutton):
    r.clipboard_clear()
    r.clipboard_append(textentry.get())
    clipbutton.configure(padx=5)
    clipbutton.configure(text='Copied')

# Closing application
def close(r):
    r.destroy()

# Loads list of words into a set
def loadwords():
    with open('wordslist.txt') as wordfile:
        validwords = set(wordfile.read().split())
    return validwords

# Grabs a random word from set
def getwords(wordslist):
    current = random.sample(wordslist, 1)[0]
    if (validwords(current)):
        return current
    else:
        getwords(wordslist)

# Validates the current word
def validwords(words):
    if (len(words) > 4 & len(words) < 9):
        return True
    else:
        return False

# Modifies the current word by capitalization and padding
def modwords(words, padding):
    words = list(words.capitalize())
    words.append(padding+padding)
    return str(''.join(words))

# Generates passwords
def generator(textentry, clipbutton):
    output = []
    englishwords = loadwords()
    padding = str(''.join(random.sample(['!','^','*','-','+',':','~','?','.',';'], 1)))

    while (len(output) < 3):
        current = getwords(englishwords)
        current = modwords(current, padding)
        output.append(current)
    
    output.append(str(random.randint(0, 9)) + str(random.randint(0, 9)))

    # Displays generated password
    clipbutton.configure(padx=10)
    clipbutton.configure(text='Copy')
    textentry.configure(state='normal')
    textentry.delete(0, END)
    textentry.insert(0, str(''.join(output)))
    textentry.configure(state='readonly')

# Main function
if __name__ == '__main__':
    gui()