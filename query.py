import numpy as np
from pandas import DataFrame, Series



# inv_index is an InvertedIndex
def indexWeighting(inv_index):

    # returns a 
    def invDocFreq():
        n = len(inv_index.dict().keys())
        idf_array = list()
        for token in inv_index.dict().keys():
            df = inv_index.tokenTf(token)
            idf = np.log2(n/df)
            idf_array.append(idf)
        return idf_array
    
    def tfMatrix():
        matrix = DataFrame()
        indexDict = inv_index.dict()
        matrixDict = dict()
        for token, tokenDict in indexDict.items():
            series = Series()
            max = 0
            matrixDict.update({token: dict()})
            for document, tf in tokenDict.items():
                if tf > max:
                    max = tf
            for document, tf in tokenDict.items():
                tf_ij = tf/max
                matrixDict[token].update({document: tf_ij})
        matrix = DataFrame(matrixDict)
        return matrix.to_numpy()
    return

    def tfMatrix(invIndex):
        matrix = DataFrame()
        indexDict = inv_index.dict()
        matrixDict = dict()
        for token, tokenDict in indexDict.items():
            series = Series()
            max = 0
            matrixDict.update({token: dict()})
            for document, tf in tokenDict.items():
                if tf > max:
                    max = tf
            for document, tf in tokenDict.items():
                tf_ij = tf/max
                matrixDict[token].update({document: tf_ij})
        matrix = DataFrame(matrixDict)
        return matrix.to_numpy()
    
            