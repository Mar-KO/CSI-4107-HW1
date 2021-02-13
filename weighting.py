import numpy as np
import pandas
from pandas import DataFrame, Series
import threading
import multiprocessing


# inv_index is an InvertedIndex
def indexWeighting(inv_index):

    # returns a 
    
    
    indexDict = inv_index.dict()
    tf_idf = dict()
    idfDict = invDocFreq(inv_index)
    for token, tokenDict in indexDict.items():
        maxTf = 0
        for document, tf in tokenDict.items():
            if tf > maxTf:
                maxTf = tf
        for document, tf in tokenDict.items():
            tf_ij = tf/maxTf
            w_ij = tf_ij * idfDict[token]
            tf_idf[document, token] = w_ij
        
        
    return tf_idf

def invDocFreq(inv_index):
    n = len(inv_index.dict().keys())
    idf_array = dict()
    for token in inv_index.dict().keys():
        df = inv_index.tokenTf(token)
        idf = np.log2(n/df)
        idf_array.update({token: idf})
    return idf_array


# query is a string
def queryWeighting(query, inv_index, spacy):
    idfDict = invDocFreq(inv_index)
    weightArray = dict()
    tokens = spacy.tokenizer(query)
    for token in tokens:
        if (token in idfDict.keys()):
            w_iq = idfDict[token] * (0.5 + 0.5)
            weightArray.update({token: w_iq})
    return weightArray

def vectorizeWeighting(tf_idf):
    idx = pandas.MultiIndex.from_tuples(tf_idf.keys())
    return Series(tf_idf.values(), index=idx).unstack(fill_value=0.0)   

            