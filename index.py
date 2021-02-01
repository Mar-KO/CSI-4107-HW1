import spacy as sp
import pandas
import io





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
        if (token not in self._hashtable.keys()):
            self._hashtable[token] = dict()
            self._hashtable[token].update({str(document): 1})
        elif (token in self._hashtable.keys()) and (str(document) not in self._hashtable[token].keys()):
            self._hashtable[token].update({document: 1})
        else:
            self._hashtable[token][str(document)] = self._hashtable[token][str(document)] + 1
        
    
    def tokenTf(self, token):
        if (token not in self._hashtable.keys()):
            return 0
        else:
            return len(self._hashtable[token])

    def __str__(self):
        final_str = io.StringIO()
        for token in self._hashtable.keys():
            final_str.write(f'{token}, {self.tokenTf(token)}: {self._hashtable[token]} \n')
        return final_str.getvalue()
    
    def dict():
        return self._hashtable;

    def documentCount():
        return count(self._documents.keys())


    

# docs param is a DataFrame, inverted_index is a ref to InvertedIndex
def indexDocs(docs, inverted_index):
    doc = docs['doc']
    docId = docs['querytweettime']
    for token in doc:
        inverted_index.addDocument(docs)
        inverted_index.addToken(token.text, docId)
