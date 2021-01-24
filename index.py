import spacy as sp

class InvertedIndex(object):
    

    def __init__(self):
        self._hashtable = dict()

    def addDocument(self, token, document):
        if (self._hashtable.get(token) == None):
            self._hashtable[token] = list()
        self._hashtable[token].append(document)
    
    def tokenCount(self, token):
        if (self._hashtable.get(token) == None):
            0
        else:
            len(self._hashtable[token])

    
