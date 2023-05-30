import IngredientCollection as IngredientCollection
import StopWordRemover as StopWordRemover
import WordNormalizer as WordNormalizer
import WordTokenizer as WordTokenizer
import Classes.Path as Path
import datetime


def PreProcess():
    # initialize essential objects
    collection = IngredientCollection.IngredientCollection()
    stopwordRemover = StopWordRemover.StopWordRemover()
    normalizer = WordNormalizer.WordNormalizer()
    wr = open(Path.ResultHM1, "w", encoding="utf8")
    recipes = []

    # process the corpus, recipe by recipe, iteratively.
    count = 0
    while True:
        recipes = collection.nextRecipe(count)
        if recipes == None or recipes == [" ", " "]:
            break
        title = recipes[0].strip()
        title = title.replace("\n", " ")
        ingredients = recipes[1]
        directions = recipes[2]
        url = recipes[3]

        # Output the title
        wr.write(title+"\n")

        # Output the preprocessed content (title + ingredients + directions)
        all_words = title + " " + ingredients + directions
        tokenizer = WordTokenizer.WordTokenizer(all_words)
        while True:
            word = tokenizer.nextWord()
            if word == None:
                break
            word = normalizer.lowercase(word)
            if stopwordRemover.isStopword(word) == False:
                wr.write(normalizer.stem(word) + " ")
        wr.write("\n")
        wr.write(str(url))
        wr.write("\n")
        count += 1
        if count % 30000 == 0:
            print("finish %s docs" % count)
    wr.close()
    print("Total : %s docs" % count)
    return


startTime = datetime.datetime.now()
PreProcess()
endTime = datetime.datetime.now()
print ("running time: ", endTime - startTime)

