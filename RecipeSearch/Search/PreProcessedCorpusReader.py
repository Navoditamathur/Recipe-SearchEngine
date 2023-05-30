import Classes.Path as Path


class PreprocessedCorpusReader:

    corpus = 0

    def __init__(self):
        self.corpus = open(Path.ResultHM1, "r", encoding="utf8")

    def nextRecipe(self):

        title = self.corpus.readline().strip()
        if title == "":
            self.corpus.close()
            return
        ingredients = self.corpus.readline().strip()
        url = self.corpus.readline().strip()
        return [title, ingredients, url]
