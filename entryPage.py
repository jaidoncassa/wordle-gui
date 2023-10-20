import tkinter as tk

class entry:
    
    def __init__(self, width, height):

        # GUI initialization
        self.openPage = tk.Tk()
        self.openPage.title("Wordle")
        self.openPage['background'] = 'gainsboro'

        self.width = width
        self.height = height

        posX, posY = self.getDimensions(self.openPage, self.width, self.height)
        self.openPage.geometry(f'{self.width}x{self.height}+{int(posX)}+{int(posY)}')

        # Initial Text
        label_1 = tk.Label(self.openPage, text='Wordle', font=("helvetica", 25, 'bold'),
                            bg='gainsboro')
        label_1.pack(padx=10, pady=(self.height/3, 5))

        label_2 = tk.Label(self.openPage, text='Get 6 chances to', font=("Samanat a", 15),
                            bg='gainsboro')
        label_2.pack(padx=10, pady=2)

        label_3 = tk.Label(self.openPage, text='guess a 5-letter word.', font=("Samanat a", 15),
                            bg='gainsboro')
        label_3.pack(padx=10)

        self.choices = False

        # Buttons for Button Frame
        btn = tk.Button(self.openPage, text="Play", font=("Arial", 18), 
                        fg='white', 
                        bg='black',
                        command=self.redirect)
        btn.pack(padx=10, pady=10)

        # run the app window
        self.openPage.mainloop()
    
    def getDimensions(self, parent, w, h):
        screenWidth = parent.winfo_screenwidth()
        screenHeight = parent.winfo_screenheight()

        posX = (screenWidth / 2) - (w / 2)
        posY = (screenHeight / 2) - (h / 2)

        return posX, posY
    
    def redirect(self):
        self.choices = True
        self.openPage.destroy()

    def getChoice(self):
        return self.choices

