import tkinter as tk

#create the first window called root
root = tk.Tk()
root.title("Select you choices")
# How to have our own logo for the window --> root.iconbitmap("C:/filelocation/something.png")  unsure of the image type as of now

mappings = []
## List of all functions
def myClick():

    if clicked.get() == options[1] or clicked.get() == options[0]:
        print("You can't do that")
        secondLabel = tk.Label(root, text="Invalid option in Dropdown Menu").pack()
    else:
        if enter.get():
            myLabel = tk.Label(root, text= enter.get() + " mapped to " + clicked.get()).pack()
            mappings.append(clicked.get() + ", " + enter.get())
            print(clicked.get() + " " + enter.get())
        else:
            myLabel = tk.Label(root, text= "Type a value to map " + clicked.get() + " above.").pack()

def myView():

    #code to make a new window
    """
    second_root = tk.Tk()
    second_root.title("List of Mappings")
    second = tk.Label(second_root, text = "This is a new window?")
    second.pack()
    """

    #create a layered window but it will be closed if its root is closed
    second_lvl = tk.Toplevel()
    second_lvl.title("List of Mappings")
    second_lvl.geometry("400x400")
    second = tk.Label(second_lvl, text = "All keybinds and strings listed below.  They are in the order Keybind, String:")
    second.pack()

    for i in mappings:
        second = tk.Label(second_lvl, text=i).pack()

##Main Loop starts here
root.geometry("400x400")

options = [ "--", "Choose an option",
           "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
           "a", "s", "d", "f", "g", "h", "j", "k", "l",
           "z", "x", "c", "v", "b", "n", "m"
           ]

myLabel = tk.Label(root, text="Enter a message to map to the dropdown shortcut").pack()

#An input table on the root window
enter = tk.Entry(root, width=75)
enter.pack()

#Dropdown window drop with value selected saved into clicked variable, created on the root window
#Dropdown options are from the options list
clicked = tk.StringVar()
clicked.set(options[0])
drop = tk.OptionMenu(root, clicked, *options).pack()

#A button for the user to click
#Once it is clicked the function myClick() will run
myButton = tk.Button(root, text="Submit you mapping Click", command=myClick).pack()

mapViewer = tk.Button(root, text= "View all mappings", command=myView).pack()
#Pressing the butotn exits the program
exitButton = tk.Button(root, text="Exit Program", command=root.quit).pack()

root.mainloop()