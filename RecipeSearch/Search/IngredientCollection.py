import Classes.Path as Path
import pandas as pd


# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class IngredientCollection:

    def __init__(self):
        self.fp_ingredient = pd.read_csv('./Search/data/recipe_dataset.csv')  # read in csv file of original dataset
        return

    def nextRecipe(self, count):
        try:
            ingredient = self.fp_ingredient['NER'][count]  # set ingredient equal to ingredient column at row 'count'
            title = self.fp_ingredient['title'][count]  # set title equal to title column at row 'count'
            directions = self.fp_ingredient['directions'][count]  # set directions equal to title directions
            url = self.fp_ingredient['link'][count]  # set link equal to title url
            str_ingredient = str(ingredient)  # convert ingredient to string
            str_title = str(title)  # convert title to string
            str_directions = str(directions)
            return [str_title, str_ingredient, str_directions, url]
        except KeyError:  # if there is key error return None
            return None





