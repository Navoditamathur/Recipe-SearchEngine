import os
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import RegexTokenizer


# write index with whoosh

class MyIndexWriter:
    writer = []

    def __init__(self):
        path_dir = 'RecipeSearch/data/index'  # set output path of index
        os.makedirs(path_dir, exist_ok=True)
        schema = Schema(title=ID(stored=True),
                        url=ID(stored=True),
                        recipe=TEXT(analyzer=RegexTokenizer(), stored=True))
        indexing = index.create_in(path_dir, schema)
        self.writer = indexing.writer()
        return

    def index(self, title, recipe, url):
        self.writer.add_document(title=title, url=url, recipe=recipe)
        return

    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):
        self.writer.commit()
        return
