import random
import tkinter



def name_to_number(name):
    if name == "rock":
        number = 0
        return number

    elif name == "paper":
        number = 1
        return number
    elif name == "scissors":
        number = 2
        return number
    else:
        return -1
def number_to_name(number):
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "paper"
        return name
    elif number == 2:
        name = "scissors"
        return name
    else:
        return "Given number is incorrect"

def rps(player_choice):
    print ()

    player_output = "Player chooses: " + player_choice
    player_number = name_to_number(player_choice)
    #following if is for handling incorrect input
    if player_number == -1:
        return "Incorrect input."
    comp_number = random.randrange(0, 3)
    comp_choice = number_to_name(comp_number)

    computer_output = "Computer chooses: " + comp_choice
    if comp_number == player_number:
        winner = "Player and computer tie!"
    elif ((comp_number - player_number) % 3) == 1:
        winner = "Computer wins!"
    else:
        winner = "Player wins!"
    return player_output + "\n" + computer_output + "\n" + winner


class rpsGuiTk(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.player_choice = None

        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnButtonClick)
        self.entryVariable.set("")

        button = tkinter.Button(self,text=u"Play",command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,text="Helvetica", font=("Helvetica", 14),anchor="w",
                              fg="white",bg="grey",height=10, width=40)
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"")

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0, minsize=50)
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonClick(self):
        self.player_choice = self.entryVariable.get()
        self.labelVariable.set(rps(self.player_choice))
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

if __name__ == "__main__":
    app = rpsGuiTk(None)

    app.title('Rock, paper and scissors!')
    app.mainloop()



