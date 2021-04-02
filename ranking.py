import pandas as pd
import numpy as np
import weighting
from tokenizer import QueryData
import gensim
from gensim.models import Word2Vec
import itertools


def queryRankingCosSim(query, tfidf, inv_index, spacy, dvl):
    weightDict = weighting.queryWeighting(query, inv_index, spacy)
    similarityDict = {}
    queryWeightingArray = np.array(list(weightDict.values()))
    queryVectorLength = np.sqrt(np.sum(np.power(queryWeightingArray, 2)))
    for token, w_iq in weightDict.items():
        tokenDict = inv_index.dict()[token]
        for document in tokenDict.keys():
            if (document not in similarityDict.keys()):
                similarityDict.update({document: 0.0})
            similarity = w_iq * tfidf[document, token] / (dvl[document] * queryVectorLength)
            similarityDict[document] = similarityDict[document] + similarity
    return similarityDict

def queryRanking(query, tfidf, inv_index, spacy, dvl):
    weightDict = weighting.queryWeighting(query, inv_index, spacy)
    similarityDict = {}
    #queryWeightingArray = np.array(list(weightDict.values()))
    #queryVectorLength = np.sqrt(np.sum(np.power(queryWeightingArray, 2)))
    for token, w_iq in weightDict.items():
        tokenDict = inv_index.dict()[token]
        for document in tokenDict.keys():
            if (document not in similarityDict.keys()):
                similarityDict.update({document: 0.0})
            similarity = w_iq * tfidf[document, token]
            similarityDict[document] = similarityDict[document] + similarity
    return similarityDict

def addSynonyms(query, model, dataset):
    wordlist = query.split()
    newQuery = query
    for word1, word2 in itertools.combinations(wordlist, 2):
        if (word1 != word2):
            sim = model.wv.similarity(word1, word2)
            if (sim >= 0.9):
                syn = model.wv.most_similar(positive=[word1,word2])[0][0]
                if (syn not in newQuery):
                    newQuery.append(f' {syn}')
    return newQuery