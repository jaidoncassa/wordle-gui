import tkinter as tk
from backend import *
from tkinter import messagebox

class wordlePages:

        def __init__(self, width, height):

                self.wordleLayout = tk.Tk()
                self.back = functionality()
                self.targetWord = self.back.getTargetWord()
                self.wordleLayout.title("Wordle")
                self.wordleLayout['background'] = 'gray9'

                self.width = width
                self.height = height
                posX, posY = self.getDimensions(self.wordleLayout, self.width, self.height)
                self.wordleLayout.geometry(f'{self.width}x{self.height}+{int(posX)}+{int(posY)}')

                self.label = tk.Label(self.wordleLayout, text='Wordle', bg='gray9', fg='white', font=('Impact', 18, 'bold'))
                self.label.pack(pady=15)
                
                canvas = tk.Canvas(self.wordleLayout, width=self.width, height=.0005, highlightthickness=0)
                canvas.pack(pady=(0, 15))

                self.frame = tk.Frame(self.wordleLayout, bg='gray9')
                self.frame.pack()
                self.text_widgets = []
                self.COLUMNS = 5
                self.ROWS = 6


                self.create_text_widgets()
                self.focused = self.text_widgets[0][0]
                self.focused.focus_set()
                self.bind_events()

                self.wordleLayout.mainloop()

        def create_text_widgets(self):
                self.text_widgets = [[tk.Text(self.frame, width=5, height=2,
                                               bg='gray9', font=('Ubuntu Mono', 13, 'bold'),
                                               fg='white') 
                                      for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

                for i in range(6):
                        for j in range(5):
                                self.text_widgets[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        def bind_events(self):
                for i in range(self.ROWS):
                        for j in range(self.COLUMNS):
                                self.text_widgets[i][j].bind('<Key>', lambda e, r=i, c=j: self.on_text_change(e, r, c))
                                self.text_widgets[i][j].bind('<BackSpace>', lambda e, r=i, c=j: self.on_delete(e, r, c))
                                self.text_widgets[i][j].bind('<Return>', lambda e, r=i, c=j: self.on_enter(e, r, c))
                                self.text_widgets[i][j].bind('<Button-1>', lambda e, r=i, c=j: self.on_click(e, r, c))
                                self.text_widgets[i][j].bind('<Tab>', lambda e: 'break')

        def getDimensions(self, parent, w, h):
                screenWidth = parent.winfo_screenwidth()
                screenHeight = parent.winfo_screenheight()

                posX = (screenWidth / 2) - (w / 2)
                posY = (screenHeight / 2) - (h / 2)

                return posX, posY
        
        def disable_text(self, text_widget):
                text_widget.config(state=tk.DISABLED)

        def enable_text(self, text_widget):
                text_widget.config(state=tk.NORMAL)

        def bind_key(self, widget, row, column):
                widget.bind('<Key>', lambda e, r=row, c=column: self.on_text_change(e, r, c))

        def get_row(self, row):
                word = ''
                for obj in self.text_widgets[row]:
                        word += obj.get('1.0', 'end-1c')
                return word.lower()
        
        def add(self, next_widget, row, next_column, e):
                self.focused.insert("1.0", e.char.upper())
                self.focused.config(state=tk.DISABLED)
                self.focused.unbind('<Key>')
                self.focused = next_widget
                self.focused.focus_set()
                self.bind_key(next_widget, row, next_column)

        def find_focused_index(self):
                for x in range(len(self.text_widgets)):
                        for y in range(len(self.text_widgets[x])):
                                if self.focused is self.text_widgets[x][y]:
                                        return x, y
                return -1, -1

        def on_text_change(self, e, row, current_index):

                if not e.char.isalpha():
                        self.text_widgets[row][current_index].mark_set("insert", "1.0")
                        return 'break'
                
                current_text_widget = self.text_widgets[row][current_index]
                # make sure no one can type anywhere else
                if current_text_widget != self.focused:
                        self.disable_text(current_text_widget)
                        self.focused.focus_set()

                current_text = self.focused.get("1.0", "end-1c").strip()
                row, current_index = self.find_focused_index()
                next_column = (current_index + 1) % self.COLUMNS if current_index != self.COLUMNS - 1 else self.COLUMNS - 1
                next_widget = self.text_widgets[row][next_column]

                if current_text == '':
                        self.add(next_widget, row, next_column, e)    
                # case3: user enters a key, with the desire of adding a key, but there is an element there
                else:   
                        next_widget.focus_set()
                        next_widget.insert(tk.END, e.char.upper())
                        self.focused = next_widget

        def patterns(self, word, row):

                dic_of_target = {x: self.targetWord.count(x) for x in self.targetWord}

                for index in range(len(self.text_widgets[row])):
                        char = word[index]
                        widget = self.text_widgets[row][index]
                                
                        if char in self.targetWord:

                                widget.focus_set()

                                if char == self.targetWord[index]:
                                        dic_of_target[char] -= 1
                                        widget.config(bg = 'green')
                        
                                elif dic_of_target[char] == 1:
                                        dic_of_target[char] -= 1
                                        widget.config(bg='goldenrod')

                                # case in which target word is only one char, but we enter two of the same char, so only one should turn up yellow
                                else:
                                        widget.config(bg='azure4')

                        else:
                                widget.config(bg='azure4')
                
                # check for last row
                if row == len(self.text_widgets) - 1:

                        # change this eventually
                        self.loses()
                
                # upate cursor for user, once they entered a valid word for a row, it is impossible to enter that row again
                else:
                        self.focused = self.text_widgets[row + 1][0]
                        self.focused.focus_set()

        def wins(self, row):
                for index in range(len(self.text_widgets[row])):
                        widget = self.text_widgets[row][index]
                        widget.config(bg = 'green')
                messagebox.showinfo("WON", "CONGRATS YOU WON!")

        def loses(self):
                messagebox.showinfo("Lose", "Sorry Maybe Next Time \n" + "   " + self.targetWord)
                exit()

        def on_delete(self, e, i, j):

                current_text_widget = self.text_widgets[i][j]

                if current_text_widget != self.focused:
                        self.disable_text(current_text_widget)
                        self.focused.focus_set()
                        return 'break'
                
                current_text = current_text_widget.get("1.0", "end-1c").strip()
                # in this case user enters a key filling the last box, the next_wiget becomes the last rows text_widget, or
                # the text box they just filled fyi
                next_column = (j + 1) % self.COLUMNS if j != self.COLUMNS - 1 else self.COLUMNS - 1
                next_widget = self.text_widgets[i][next_column]

                def backSpace(current_text, row , current_index, next_widget): 
                # case: the specific row is full, we must delete the last element,
                        if current_text != '':
                                
                                # since this last box will be disabled
                                self.enable_text(next_widget)
                                next_widget.delete("1.0", tk.END)
                                self.focused = next_widget
                                self.focused.focus_set()

                        # case: fails
                        else:
                                if current_index > 0:
                                        prev_text_widget = self.text_widgets[row][current_index - 1]
                                        self.enable_text(prev_text_widget)
                                        prev_text_widget.delete('end-2c')
                                        self.focused = prev_text_widget
                                        self.focused.focus_set()
                                        self.bind_key(prev_text_widget, row, current_index - 1)

                backSpace(current_text, i, j, next_widget)

        def on_enter(self, e, i, j):

                def enter(row):
                        word = self.get_row(row)
                        # not full row
                        if len(word) != 5:

                                # MESSAGE BOX HEREE
                                messagebox.showinfo("Invalid", "Not Enough Letters")

                        # not a valid word
                        elif not self.back.validateWord(word):
                                
                                # custamization
                                messagebox.showinfo("Invalid", "Not In Words List")

                        # a valid 5 letter word
                        else:
                                check = self.back.afterValidation(word)

                                # it is target wordle word
                                if check:
                                        self.wins(row)

                                # not the word
                                else:
                                        self.patterns(word, row)
                enter(i)

        def on_click(self, e, i , j):
                widget = self.text_widgets[i][j]
                self.disable_text(widget)
                self.focused.focus_set()
