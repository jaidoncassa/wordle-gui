
import tkinter as tk
from backend import *

root = tk.Tk()
root.title("Disable Text after One Character")
frame = tk.Frame(root)
frame.pack()

back = functionality()
targetWord = back.getTargetWord()
text_widgets = []
COLUMNS = 5
ROWS = 6
text_widgets = [[tk.Text(frame, width=10, height=2) for _ in range(COLUMNS)] for _ in range(ROWS)]
focused = text_widgets[0][0].focus_set()

# Arrange the text widgets in a grid
for i in range(6):
    for j in range(5):
        text_widgets[i][j].grid(row=i, column=j, padx=5, pady=5)

for i in range(ROWS):
    for j in range(COLUMNS):
        text_widgets[i][j].bind('<Key>', lambda e, r=i, c=j: on_text_change(e, r, c))

for i in range(ROWS):
    for j in range(COLUMNS):
        text_widgets[i][j].bind('<BackSpace>', lambda e, r=i, c=j: on_delete(e, r, c))

for i in range(ROWS):
    for j in range(COLUMNS):
        text_widgets[i][j].bind('<Return>', lambda e, r=i, c=j: on_enter(e, r, c))

def add(current_text_widget, next_widget, row, next_column, e):
    current_text_widget.insert("1.0", e.char)
    current_text_widget.config(state=tk.DISABLED)
    current_text_widget.unbind('<Key>')
    next_widget.focus_set()
    bindKey(next_widget, row, next_column)
    
def disable_text(text_widget):
    text_widget.config(state=tk.DISABLED)

def enable_text(text_widget):
    text_widget.config(state=tk.NORMAL)

def bindKey(widget,row, column):
    widget.bind('<Key>', lambda e, r=row, c=column: on_text_change(e, r, c))

def getRow(row):
    word = ''
    for obj in text_widgets[row]:
        word += obj.get('1.0', 'end-1c')
    return word


def on_text_change(e, row, current_index):                                             
    
    current_text_widget = text_widgets[row][current_index]
    current_text = current_text_widget.get("1.0", "end-1c").strip()

    # in this case user enters a key filling the last box, the next_wiget becomes the last rows text_widget, or
    # the text box they just filled fyi
    next_column = (current_index + 1) % COLUMNS if current_index != COLUMNS - 1 else COLUMNS - 1
    next_widget = text_widgets[row][next_column]

    if e.keysym == 'space':
        text_widgets[row][current_index].mark_set("insert", "1.0")
        return 'break'
    
    elif current_text == '':
        add(current_text_widget, next_widget, row, next_column, e)
    
    # case3: user enters a key, with the desire of adding a key, but there is an element there
    else:   
        next_widget.focus_set()
        next_widget.insert(tk.END, e.char)
    

def patterns(word, row):
    for index in range(len(text_widgets[row])):
        # wordtar = death
        # our word = deets
        char = word[index]
        charPresent = targetWord.count(char)
        widget = text_widgets[row][index]

        if char in targetWord:

            widget.focus_set()

            if char == targetWord[index]:
                charPresent -= 1
                widget.config(bg = 'green')
            
            elif charPresent > 0:
                    widget.config(bg='yellow')

            # case in which target word is only one char, but we enter two of the same char, so only one should turn up yellow
            else:
                widget.config(bg='grey')

        else:
            widget.config(bg='grey')
    
    # check for last row
    if row == len(text_widgets) - 1:

        # change this eventually
        back.lose()
    
    # upate cursor for user, once they entered a valid word for a row, it is impossible to enter that row again
    else:
        text_widgets[row + 1][0].focus_set()


def wins(row):
    for index in range(len(text_widgets[row])):
        widget = text_widgets[row][index]
        widget.config(bg = 'green')
    # pop up you won


def lose():
    pass
    

def on_delete(e, i, j):
    
    # two cases to take care 
    def backSpace(current_text, current_index, row, current_text_widget, next_widget): 
    # case: the specific row is full, we must delete the last element,
        if current_text != '':
                
                # since this last box will be disabled
                enable_text(next_widget)
                next_widget.delete("1.0", tk.END)
                next_widget.focus_set()

        # case: fails
        else:

            if current_index > 0:
                prev_text_widget = text_widgets[row][current_index - 1]
                enable_text(prev_text_widget)
                prev_text_widget.delete('end-2c')
                prev_text_widget.focus_set()
                bindKey(prev_text_widget, row, current_index - 1)


def on_enter(e, i, j):

    def Enter(row):
        word = getRow(row)
        # not full row
        if len(word) != 5:

            # MESSAGE BOX HEREE
            print("not long enough")

        # not a valid word
        elif not back.validateWord(word):
            
            # custamization
            print('Not a valid word')

        # a valid 5 letter word
        else:
            check = back.afterValidation(word)

            # it is target wordle word
            if check:
                wins(row)

            # not the word
            else:
                patterns(word, row)


# create message pop ups for win, for lose, and then implement them into the wordlePage

root.mainloop()