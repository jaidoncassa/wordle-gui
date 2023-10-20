import tkinter as tk
from wordlePage import *

class howToPlays:

    def __init__(self, width, height):
        
        # self.rules gui
        self.rules = tk.Tk()
        self.rules.title("")
        self.rules['background'] = 'black'

        self.width = width
        self.height = height

        posX, posY = self.getDimensions(self.rules, int(self.width*.6), int(self.height *.6))
        self.rules.geometry(f'{int(self.width*.6)}x{int(self.height *.6)}+{int(posX)}+{int(posY)}')

        # first texts during directions gui
        label_1 = tk.Label(self.rules, 
                           text='How To Play', 
                           font=("helvetica", 17, 'bold'),
                           fg='white', bg='black') 
        label_2 = tk.Label(self.rules, text='Guess the Wordle in 6 tries.', 
                           font=("helvetica", 14),
                           fg='white', bg='black')
        label_3 = tk.Label(self.rules, text='• Each gues must be a valid 5-letter word.', 
                           font=("helvetica", 11),
                           fg='white', bg='black')
        label_4 = tk.Label(self.rules, text='• The color of the tiles will change to show how close you guess', 
                           font=("helvetica", 11),
                           fg='white', bg='black')
        label_5 = tk.Label(self.rules, text='was to the word.', 
                           font=("helvetica", 11),
                           fg='white', bg='black')
        
        label_6 = tk.Label(self.rules, text='Examples', 
                           font=("helvetica", 12, 'bold'),
                           fg='white', bg='black')
        
        label_1.pack(padx=15, pady=(25,0), anchor='w')
        label_2.pack(padx=15, pady=(0, 10), anchor='w')
        label_3.pack(padx=15, anchor='w')
        label_4.pack(padx=15, anchor='w')
        label_5.pack(padx=25, pady=(0, 10), anchor='w')
        label_6.pack(padx=15, pady=4, anchor='w')


        # word boxes WEARY
        border_outer = tk.Frame(self.rules, background='black')
        border_outer.pack(anchor='w', padx=15, pady=(0, 4))

        border1 = tk.Frame(border_outer, background='green')
        label_1 = tk.Label(border1, text='W', font=('helvetica', 15, 'bold'), fg='white', bg='green')
        label_1.pack(padx=1, pady=1)
        border1.grid(row=0, column=0, pady=1, padx=1)

        word = 'EARY'
        for x in range(len(word)):
            border = tk.Frame(border_outer)
            label = tk.Label(border, text=word[x],
                            font=("helvetica", 15, 'bold'),
                            fg='white', bg='black')
            label.pack(padx=1, pady=1)
            border.grid(row=0, column=x+1, padx=2, pady=1)

        # middle text
        label = tk.Label(self.rules, text='W is the word and in the correct Spot.', 
                         font=('helvetica', 11), fg='white', bg='black')
        label.pack(padx=15, anchor='w', pady=(0, 10))

        # word boxes PILLS
        border_outer1 = tk.Frame(self.rules, background='black')
        border_outer1.pack(anchor='w', padx=15)
        word = 'PILLS'
        for x in range(len(word)):

            if x == 1:
                border1 = tk.Frame(border_outer1, background='gold')
                label_1 = tk.Label(border1, text=word[x], 
                                   font=('helvetica', 15, 'bold'), fg='white', bg='gold')
                label_1.pack(padx=1, pady=1)
                border1.grid(row=0, column=x + 1, pady=1, padx=1)

            else:
                border = tk.Frame(border_outer1)
                label = tk.Label(border, text=word[x],
                                font=("helvetica", 15, 'bold'),
                                fg='white', bg='black')
                label.pack(padx=1, pady=1)
                border.grid(row=0, column=x+1, padx=2, pady=1)

        # middle text
        label = tk.Label(self.rules, text='I is in the word but in the wrong spot.', 
                         font=('helvetica', 11), fg='white', bg='black')
        label.pack(padx=15, anchor='w', pady=(0, 10))


        # word boxes VAGUE
        border_outer2 = tk.Frame(self.rules, background='black')
        border_outer2.pack(anchor='w', padx=15)
        word = 'VAGUE'
        for x in range(len(word)):

            if x ==3:
                border1 = tk.Frame(border_outer2, background='dimgray')
                label_1 = tk.Label(border1, text=word[x], 
                                   font=('helvetica', 15, 'bold'), fg='white', bg='dimgray')
                label_1.pack(padx=1, pady=1)
                border1.grid(row=0, column=x + 1, pady=1, padx=1)

            else:
                border = tk.Frame(border_outer2)
                label = tk.Label(border, text=word[x],
                                font=("helvetica", 15, 'bold'),
                                fg='white', bg='black')
                label.pack(padx=1, pady=1)
                border.grid(row=0, column=x+1, padx=2, pady=1)


            # middle text
        label = tk.Label(self.rules, text='U is not in the word in any spot.', 
                         font=('helvetica', 11), fg='white', bg='black')
        label.pack(padx=15, anchor='w', pady=(0, 10))

        canvas = tk.Canvas(self.rules, width=self.width*.6, height=.0005, highlightthickness=0)
        canvas.pack()

        wordlePages(self.width, self.height)
        self.rules.mainloop()

    def getDimensions(self, parent, w, h):
        screenWidth = parent.winfo_screenwidth()
        screenHeight = parent.winfo_screenheight()

        posX = (screenWidth / 2) - (w / 2)
        posY = (screenHeight / 2) - (h / 2)

        return posX, posY


