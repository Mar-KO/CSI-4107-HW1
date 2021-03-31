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
        maxTf = np.amax(list(tokenDict.values()))
        #for document, tf in tokenDict.items():
        #    if tf > maxTf:
        #        maxTf = tf 
        for document, tf in tokenDict.items():
            tf_ij = tf/maxTf
            w_ij = tf_ij * idfDict[token]
            tf_idf[document, token] = np.float32(w_ij)
        
        
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
    tokens = spacy(query)
    tokenCount = {}
    for token in tokens:
        if (token.text not in tokenCount.keys()):
            tokenCount.update({token.text: 1})
        tokenCount[token.text] = tokenCount[token.text] + 1
    for token in tokens:
        if (token.lemma_ in idfDict.keys()):
            w_iq = idfDict[token.text] * (0.5 + 0.5 * tokenCount[token.text])
            weightArray.update({token.text: w_iq})
    return weightArray

# docCollection is a DataFrame, tf_idf is the weights dictionary
def computeDocumentVectorLengths(docCollection, tf_idf):
    documentVectorLengths = {}
    for label, data in docCollection.iterrows():
        doc = data['doc']
        docId = data['querytweettime']
        weightsSum = 0.0
        for token in doc:
            weightsSum = weightsSum + np.power(tf_idf[str(docId), token.text], 2)
        documentVectorLengths[str(docId)] = np.sqrt(weightsSum)
    return documentVectorLengths




            