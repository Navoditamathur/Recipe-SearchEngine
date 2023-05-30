from .Classes import Document as Document
import whoosh.index as index
from whoosh.qparser import QueryParser
from whoosh import scoring

class QueryRetrievalModel:

    indexReader=[]

    query_parser=[]
    searcher=[]

    def __init__(self, ixReader):
        path_dir= 'RecipeSearch/data/index'
        self.searcher = index.open_dir(path_dir).searcher(weighting=scoring.BM25F(B=0.75, content_B=1.0, K1=1.5))
        self.query_parser=QueryParser("recipe", self.searcher.schema)
        return

    # query:  The query to be searched for.
    # topN: The maximum number of returned documents.
    # The returned results (retrieved documents) should be ranked by the score (from the most relevant to the least).
    # You will find our IndexingLucene.Myindexreader provides method: docLength().
    # Returned documents should be a list of Document.
    def retrieveQuery(self, query, pagenum):
        query_input=self.query_parser.parse(query.getQueryContent())
        #query_input=self.query_parser.parse(querystring)
        #query = self.query_parser.parse("content", querystring)
        #search_results = self.searcher.search_page(query, int(pagenum))
        search_results = self.searcher.search(query_input, limit=None)
        return_docs = []
        for result in search_results:
            a_doc=Document.Document()
            a_doc.setDocId(result.docnum)
            a_doc.setDocNo(self.searcher.stored_fields(result.docnum)["title"])
            a_doc.setHighlights(result.highlights("recipe",top=5))
            a_doc.setScore(result.score)
            return_docs.append(a_doc)

        return return_docs
