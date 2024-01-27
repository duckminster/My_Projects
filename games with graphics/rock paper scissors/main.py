# importing libraries
from tkinter import *
from PIL import Image, ImageTk
import random

# defining variables
userscore = 0
pcscore = 0


# functions for handling events
def enter(event):
    rock.config(bg='black', fg='white')


def enter1(event):
    paper.config(bg='black', fg='white')


def enter2(event):
    scissor.config(bg='black', fg='white')


def leave(event):
    rock.config(bg='white', fg='black')


def leave1(event):
    paper.config(bg='white', fg='black')


def leave2(event):
    scissor.config(bg='white', fg='black')


def entergame(event):
    maingame()


def maingame():
    global userscore, pcscore
    global nameinp
    global rock, paper, scissor
    # window size
    root.geometry('650x750')
    # destroying widgets on the screen
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()

    # displaying scores
    L2 = Label(text=f"{nameinp.get()} Score: {userscore}", bg='#4834DF', fg='#ffffff', borderwidth=5, relief=RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L2.grid(row=6, column=0, pady=15)
    L3 = Label(text=f"PC Score: {pcscore}", bg='#4834DF', fg='white', borderwidth=5, relief=RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L3.grid(row=7, column=0, pady=15)

    def click(event):

        global userscore, pcscore
        global L1
        global pcchose

        L1.grid_forget()
        # this below will destroy the selected label
        pcchose.destroy()

        val = event.widget.cget('text')

        # random computer selection
        x = random.randint(0, 2)
        l1 = ['Rock', 'Paper', 'Scissor']
        pc_opt = l1[x]

        # pc choice
        pcchose = Label(text=f'PC Opted: {pc_opt}', font='lucida 15 bold', bg='black', fg='red')
        # position of elements
        pcchose.grid(row=6, column=1, pady=15)

        # val means what user chose and pc_opt means what pc chose or opted
        # rock and paper
        if val == 'Rock' and pc_opt == 'Paper':
            L1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            pcscore += 1

        # rock and scissor
        elif val == 'Rock' and pc_opt == 'Scissor':
            L1 = Label(text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            userscore += 1

        # paper and scissor
        elif val == 'Paper' and pc_opt == 'Scissor':
            L1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            pcscore += 1

        # paper and rock
        elif val == 'Paper' and pc_opt == 'Rock':
            L1 = Label(text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            userscore += 1

        # scissor and rock
        elif val == 'Scissor' and pc_opt == 'Rock':
            L1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            pcscore += 1

        # scissor and paper
        elif val == 'Scissor' and pc_opt == 'Paper':
            L1 = Label(text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            userscore += 1

        # tie
        elif val == pc_opt:
            L1 = Label(text=f"It's A Tie", font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
        maingame()

    # the overall Layout of RPS Game is handled by the below code
    # used the label() to add various labels on the new window
    head = Label(text='Rock Paper Scissor', font='arial 35 bold', bg='black', fg='white')
    head.grid(columnspan=2, row=0, ipadx=70, padx=33, pady=10)
    head1 = Label(text='CopyAssignment', font='arial 35 bold', bg='red', fg='white')
    head1.grid(columnspan=2, row=1, ipadx=70, padx=33, pady=10)
    playerone = Label(text=f'Player 1 : {nameinp.get()}', font='lucida 16')
    playerone.grid(row=2, column=0)
    playertwo = Label(text=f'Player 2 : Computer', font='lucida 16')
    playertwo.grid(row=2, column=1)

    rock = Button(text='Rock', font='comicsansms 14 bold', height=1, width=7)
    rock.grid(row=3, column=0, pady=15)

    rock.bind('<Enter>', enter)
    rock.bind('<Leave>', leave)
    rock.bind('<Button-1>', click)
    paper = Button(text='Paper', font='comicsansms 14 bold', height=1, width=7)
    paper.grid(row=4, column=0)
    paper.bind('<Enter>', enter1)
    paper.bind('<Leave>', leave1)
    paper.bind('<Button-1>', click)
    scissor = Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7)
    scissor.grid(row=5, column=0, pady=15)
    scissor.bind('<Enter>', enter2)
    scissor.bind('<Leave>', leave2)
    scissor.bind('<Button-1>', click)

    # these are the buttons for the computer
    rock1 = Button(text='Rock', font='comicsansms 14 bold', height=1, width=7)
    rock1.grid(row=3, column=1, pady=15)
    paper1 = Button(text='Paper', font='comicsansms 14 bold', height=1, width=7)
    paper1.grid(row=4, column=1)
    scissor1 = Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7)
    scissor1.grid(row=5, column=1, pady=15)

    # game closing button
    btnclose = Button(text='Close Game', command=root.destroy, bg='green', font='arial 10 bold')
    btnclose.place(x=300, y=410)


# if __name__=='__main__':
root = Tk()
root.title('Rock Paper Scissor - CopyAssignment')
root.wm_iconbitmap("play.png")
root.geometry('650x750')
# this maxsize() function is used to set the max size of window equivlent to the one that we passed in the function
root.maxsize
# this is minsize() function annd it is bascially responsible for handling the minimum size of the tkinter window
root.minsize(650, 450)

# Defining some widgets to use them in diff functions
rock = Button()
paper = Button()
scissor = Button()

# This Label will show who won pc or user
L1 = Label()
pcchose = Label()

# handling first window
f1 = Frame(root)
img = Image.open('symbols.png')
img = img.resize((650, 450))
pic = ImageTk.PhotoImage(img)
Lab = Label(f1, image=pic)
Lab.pack()
f1.pack()

name = Label(root, text='Enter Your Name :', font='arial 15 bold')
name.place(x=262, y=250)

# storing user name
nameinp = StringVar()
inpname = Entry(root, textvar=nameinp, font='arial 10 bold')

# binded Return event with inpname entry widget
inpname.bind('<Return>', entergame)
inpname.place(x=275, y=290)

sub = Button(root, text="Let's Play", font='lucida 10 bold', bg='black', fg='white', command=maingame)
sub.place(x=305, y=350)

root.mainloop()