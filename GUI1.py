import tkinter as tk
from backend import functionality

class WordleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disable Text after One Character")
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        self.back = functionality()
        self.targetWord = 'looks'
        print(self.targetWord)
        self.text_widgets = []
        self.COLUMNS = 5
        self.ROWS = 6
        
        self.create_text_widgets()
        self.focused = self.text_widgets[0][0]
        self.focused.focus_set()
        self.bind_events()
        

    def create_text_widgets(self):
        self.text_widgets = [[tk.Text(self.frame, width=10, height=2) for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

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

    # status: maybe
    def add(self, next_widget, row, next_column, e):
        self.focused.insert("1.0", e.char)
        self.focused.config(state=tk.DISABLED)
        self.focused.unbind('<Key>')
        self.focused = next_widget
        self.focused.focus_set()
        self.bind_key(next_widget, row, next_column)


    def disable_text(self, text_widget):
        text_widget.config(state=tk.DISABLED)


    def enable_text(self, text_widget):
        text_widget.config(state=tk.NORMAL)


    def bind_key(self, widget, row, column):
        widget.bind('<Key>', lambda e, r=row, c=column: self.on_text_change(e, r, c))


    def get_row(self, row):
        word = ''
        print('using')
        for obj in self.text_widgets[row]:
            word += obj.get('1.0', 'end-1c')
        
        print(word)
        return word
    

    def find_focused_index(self):
        for x in range(len(self.text_widgets)):
            for y in range(len(self.text_widgets[x])):
                if self.focused is self.text_widgets[x][y]:
                    return x, y
        return -1, -1

    # status: complete
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
            next_widget.insert(tk.END, e.char)
            self.focused = next_widget


    def patterns(self, word, row):
        self.dic_of_target = {x: self.targetWord.count(x) for x in self.targetWord}

        # f  a=0  v  o  r
        # s  a    n  t  a

        # l  o  o  k  s
        # s  p  o  k  e
        # c  o  i  n  s
        # p  o  r  n  o

        for index in range(len(self.text_widgets[row])):

            char = word[index]
            widget = self.text_widgets[row][index]

            if char in self.targetWord:

                widget.focus_set()

                if char == self.targetWord[index]:
                    self.dic_of_target[char] -= 1
                    widget.config(bg = 'green')
                
                elif self.dic_of_target[char] == 1:
                        self.dic_of_target[char] -= 1
                        widget.config(bg='yellow')

                # case in which target word is only one char, but we enter two of the same char, so only one should turn up yell
                #ow
                else:
                    widget.config(bg='gray9')

            else:
                widget.config(bg='gray9')
            
        # check for last row
        if row == len(self.text_widgets) - 1:

            # change this eventually
            self.back.lose()
        
        # upate cursor for user, once they entered a valid word for a row, it is impossible to enter that row again
        else:
            self.focused = self.text_widgets[row + 1][0]
            self.focused.focus_set()


    def wins(self, row):
        for index in range(len(self.text_widgets[row])):
            widget = self.text_widgets[row][index]
            widget.config(bg = 'green')


    def lose(self):
        pass

    # status:
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
                print("not long enough")

            # not a valid word
            elif not self.back.validateWord(word):
                
                # custamization
                print('Not a valid word')

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

    # status: completed
    def on_click(self, e, i , j):
        widget = self.text_widgets[i][j]
        self.disable_text(widget)
        self.focused.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
