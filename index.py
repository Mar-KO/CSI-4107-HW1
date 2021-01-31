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
    
    # token is a string, document is the document ID
    def addToken(self, token, document):
        if (self._hashtable.get(token) == None):
            self._hashtable[token] = dict()
            self._hashtable[token].update({document: 0})
        else if (self._hashtable[token] != None and self._hashtable[token][document] != None):
            self._hashtable[token][document] = 0
        else:
            self._hashtable[token][document]++
        
    
    def tokenDf(self, token):
        if (self._hashtable.get(token) == None):
            return 0
        else:
            return len(self._hashtable[token])
    

# docs param is a DataFrame, inverted_index is a ref to InvertedIndex
def indexDocs(docs, inverted_index):
    doc = docs['doc']
    docId = docs['querytweettime']
    for token in doc:
        inverted_index.addDocument(docs)
        inverted_index.addToken(token.text, docId)
