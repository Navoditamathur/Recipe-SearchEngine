from .Classes import Path as Path
import os

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class StopWordRemover:

    def __init__(self):
        fp_stop = open(os.path.dirname(__file__)+'/data/stopword.txt', "r", encoding='utf-8')  # open stopword file
        self.stopword = fp_stop.readlines()
        self.stopword = [line.rstrip() for line in self.stopword]  # read stopword into list

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.
        if word in self.stopword:  # if word is in list return true
            return True
        else:
            return False
