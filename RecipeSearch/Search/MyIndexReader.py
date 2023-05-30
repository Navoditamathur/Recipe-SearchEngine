import whoosh.index as index
from whoosh.query import *
from whoosh.qparser import QueryParser


# Efficiency and memory cost should be paid with extra attention.
class MyIndexReader:

    searcher=[]

    def __init__(self):
        path_dir= 'RecipeSearch/data/index'
        self.searcher = index.open_dir(path_dir).searcher()

    # Return the integer RecipeID of input string Title.
    def getRecipeId(self, title):
        return self.searcher.document_number(title=title)

    # Return the string Title of the input integer RecipeID.
    def getDocNo(self, recipeId):
        return self.searcher.stored_fields(recipeId)["title"]

    # Return the url of the input integer RecipeID
    def getURL(self, recipeId):
        return self.searcher.stored_fields(recipeId)["url"]

    # Return DF.
    def DocFreq(self, token):
        results = self.searcher.search(Term("recipe", token))
        return len(results)

    # Return the frequency of the token in whole collection/corpus.
    def CollectionFreq(self, token):
        results = self.searcher.search(Term("recipe", token), limit=None)
        count = 0
        for result in results:
            words = self.searcher.stored_fields(result.docnum)["recipe"].split(" ")
            for word in words:
                if word==token:
                    count+=1
        return count

    # Return posting list in form of {documentID:frequency}.
    def getPostingList(self, token):
        results = self.searcher.search(Term("recipe", token), limit=None)
        postList = {}
        for result in results:
            words = self.searcher.stored_fields(result.docnum)["recipe"].split(" ")
            count=0
            for word in words:
                if word==token:
                    count+=1
            postList[result.docnum]=count
        return postList

    # Return the length of the requested document.
    def getDocLength(self, recipeId):
        words = self.searcher.stored_fields(recipeId)["recipe"].split(" ")
        return len(words)
