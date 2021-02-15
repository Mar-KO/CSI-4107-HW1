import pandas as pd
import numpy as np
import weighting
from tokenizer import QueryData


def queryRanking(query, tfidf, inv_index, spacy):
    weightDict = weighting.queryWeighting(query, inv_index, spacy)
    similarityDict = {}
    for token, w_iq in weightDict.items():
        tokenDict = inv_index.dict()[token]
        for document in tokenDict.keys():
            if (document not in similarityDict.keys()):
                similarityDict.update({document: 0.0})
            similarity = w_iq * tfidf[document, token]
            similarityDict[document] = similarityDict[document] + similarity
    return similarityDict