import re

class WordTokenizer:

    def __init__(self, ingredients):

        #Tokenize the input texts.
        punc = ",(').:;[]/-*1234567890" + ' "" ' + "\\"  # punc to remove from recipes
        for ele in ingredients:
            if ele in punc:
                ingredients = ingredients.replace(ele, " ")

        ingredients = ingredients.split()  # tokenize ingredients
        self.word_array = ingredients  # put tokenized ingredients into word_array
        self.max_pos = len(self.word_array)  # last word of word_array list
        self.cur_pos = -1
        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        self.cur_pos += 1

        if self.cur_pos == self.max_pos:  # if at end of list return null
            return None
        else:
            return self.word_array[self.cur_pos]
