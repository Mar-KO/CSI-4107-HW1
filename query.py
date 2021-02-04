import numpy as np



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
        return idf_array()
    
    
    
            