from . Classes import Query as Query
from . import StopWordRemover as StopWordRemover
from . import WordNormalizer as WordNormalizer
from . import WordTokenizer as WordTokenizer

class ExtractQuery:

    def __init__(self):
        # 1. you should extract the 4 queries from the Path.TopicDir
        # 2. the query content of each topic should be 1) tokenized, 2) to lowercase, 3) remove stop words, 4) stemming
        # 3. you can simply pick up title only for query.
        self.topicId = 1
        return

    # Return extracted queries with class Query in a list.
    def getQuries(self):
        queries=[]
        aQuery=Query.Query()
        aQuery.setTopicId("901")
        aQuery.setQueryContent("chicken OR funni")
        queries.append(aQuery)
        aQuery=Query.Query()
        aQuery.setTopicId("902")
        aQuery.setQueryContent("mushroom")
        queries.append(aQuery)
        aQuery=Query.Query()
        aQuery.setTopicId("903")
        aQuery.setQueryContent("chicken OR alfredo OR pasta")
        queries.append(aQuery)
        aQuery.setTopicId("904")
        aQuery.setQueryContent("Pizza OR Yeast")
        queries.append(aQuery)

        return queries

    def getProcessedQuery(self, content):
        query=Query.Query()
        stopwordRemover = StopWordRemover.StopWordRemover()
        normalizer = WordNormalizer.WordNormalizer()
        processedQuery = ''
        query.setTopicId(str(self.topicId))
        self.topicId +=1;
        tokenizer = WordTokenizer.WordTokenizer(content)
        while True:
            word = tokenizer.nextWord()
            if word == None:
                break
            word = normalizer.lowercase(word)
            if stopwordRemover.isStopword(word) == False:
                processedQuery += normalizer.stem(word) + " AND "
        query.setQueryContent(processedQuery)
        return query
