import spacy as sp
import pandas

class InvertedIndex(object):
    

    def __init__(self):
        self._hashtable = dict()
        self._documents = dict()

    # document will either be a Series or a DataFrame, 
    # using the tweettime as the key, and the Doc as the value
    def addDocument(self, document):
        self._documents[document['querytweettime']] = document['doc']
    
    # token is a string, document is a DataFrame
    def addToken(self, token, document):
        if (self._hashtable.get(token) == None):
            self._hashtable[token] = list()
            self._hashtable[token].append((document['querytweettime'], 0))
        else:
            self._hashtable[token]
        
    
    def tokenCount(self, token):
        if (self._hashtable.get(token) == None):
            return 0
        else:
            return len(self._hashtable[token])

    
