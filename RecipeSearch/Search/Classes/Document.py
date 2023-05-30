class Document:

    def __init__(self):
        return

    docid = ""
    docno = ""
    score = 0.0
    title = ""
    url = ""
    highlights = ""

    def getDocId(self):
        return self.docid

    def getDocNo(self):
        return self.docno

    def getScore(self):
        return self.score

    def getTitle(self):
        return self.title

    def getUrl(self):
        return self.url
    
    def getHighlights(self):
        return self.highlights

    def setDocId(self, docid):
        self.docid = docid

    def setDocNo(self, no):
        self.docno = no

    def setScore(self, the_score):
        self.score = the_score

    def setTitle(self, title):
        self.title = title

    def setUrl(self, url):
        self.url = url
        
    def setHighlights(self, highlights):
        self.highlights = highlights
