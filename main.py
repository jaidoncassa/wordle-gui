from backend import *
import entryPage 
from howToPlayPage import *

CONSTANT_SCREEN_WIDTH = 800
CONSTANT_SCREEN_HEIGHT = 800

class wordle:

    def __init__(self):

        self.begin = entryPage.entry(CONSTANT_SCREEN_WIDTH, CONSTANT_SCREEN_HEIGHT)
        
        # if that opens the howToPlay()
        if self.begin.getChoice():
            howToPlays(CONSTANT_SCREEN_WIDTH, CONSTANT_SCREEN_HEIGHT)




if __name__ == "__main__":
    wordle()
