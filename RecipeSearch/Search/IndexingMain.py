import PreProcessedCorpusReader as PreprocessedCorpusReader
import MyIndexWriter as MyIndexWriter
import MyIndexReader as MyIndexReader
import QueryRetreivalModel as QueryRetreivalModel
import ExtractQuery as ExtractQuery
import datetime



def WriteIndex():
    count = 0
    # Initiate pre-processed collection file reader.
    corpus =PreprocessedCorpusReader.PreprocessedCorpusReader()
    # Initiate the index writer.
    indexWriter = MyIndexWriter.MyIndexWriter()
    # Build index of corpus document by document.
    while True:
        recipe = corpus.nextRecipe()
        if recipe == None:
            break
        indexWriter.index(recipe[0], recipe[1], recipe[2])
        count+=1
        if count%30000==0:
            print("finish ", count," docs")
    print("totally finish ", count, " docs")
    indexWriter.close()
    return


def ReadIndex(token):
    # Initiate the index file reader.
    index = MyIndexReader.MyIndexReader()
    # retrieve the token.
    rf = index.DocFreq(token)
    ctf = index.CollectionFreq(token)
    print(" >> the token \""+token+"\" appeared in " + str(rf) + " documents and " + str(ctf) + " times in total")
    if rf>0:
        posting = index.getPostingList(token)
        for recipeId in posting:
            title = index.getDocNo(recipeId)
            print(title+"\t"+str(recipeId)+"\t"+str(posting[recipeId]))


if __name__ == "__main__":
    startTime = datetime.datetime.now()
    #SSWriteIndex()
    endTime = datetime.datetime.now()
    print("index corpus running time: ", endTime - startTime)
    startTime = datetime.datetime.now()
    index = MyIndexReader.MyIndexReader()
    search = QueryRetreivalModel.QueryRetrievalModel(index)
    extractor = ExtractQuery.ExtractQuery()
    queries= extractor.getQuries()
    for query in queries:
        print(query.topicId,"\t",query.queryContent)
        results = search.retrieveQuery(query, 10)
        rank = 1
        for result in results:
            print(result.getDocNo(),' \t ', index.getRecipeId(result.getDocNo()), '\t',
                  result.getScore(), '\t', index.getURL(index.getRecipeId(result.getDocNo())))
            rank += 1

    endTime = datetime.datetime.now()
    print("query search time: ", endTime - startTime)
