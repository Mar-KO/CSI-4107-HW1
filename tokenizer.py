import pandas as pd
import re
from spacy.tokens import Doc
import spacy

stopwords = pd.read_csv("stopwords.txt", names=['stopwords'])
stops =stopwords["stopwords"]

def Is_StopWord(token):
    ans = False
    for i in stops:
        if (i == str(token)):
            ans = True
    return ans
#print("Answer is:",Is_StopWord("a"))

def Is_Number(token):
    ans = False
    try:
        tmp = int(token)
        #print('The variable is a number')
        return True
    except:
        #print('The variable is not a number')
        return False

def Remove_Punctuations(sentence):
    res = re.sub(r'[^\w\s]', '', sentence)
    return res

def tokenize(*args, **kwrds):
    df = args[0]
    spacy = kwrds['spacy']
    # x = Remove_Punctuations(str(df["title"]))
    x = str(df['title'])
    doc = spacy(x)
    new_token_list = list()
    for token in doc:
        if not(token.is_stop == True or token.like_num == True or token.is_punct == True or token.like_url == True):
            new_token_list.append(token.text)
    new_doc = Doc(doc.vocab, new_token_list)
    return pd.Series({'querytweettime': df["querytweettime"], 'doc': new_doc})

query_list = []
#https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python/16922328



#[MB001, Q0, Tweettime, rank_for_word, score_for_word, tag]

class QueryData(object):
    
    def __init__(self):
        self._query_list = []
    
    def queries(self):
        with open('Queries.txt','r') as f:
            i = 0
            temp_list = []
            for line in f:

                x = line.split() 
                #print(x)
                if (i < 7):
                    temp_list.append(x)
                    i = i + 1
                if (len(temp_list) > 6):
                    cleaned = self.cleaning(temp_list)
                    temp_list = []
                    self._query_list.append(cleaned)
                    i = -1
  
    # creates an array for every tweet
    def cleaning(self, array):
        temp_list = []
        copy = array
        for line in copy: 
            for word in line:
                if(str(word) == "<num>"):
                    #print(x[2])
                    temp_list.append(line[2])
                if (str(word) == "<querytweettime>"):
                    #print(x[1])
                    temp_list.append(line[1])
                    y=0
                if(str(word) == "<title>"):
                    line.pop(0)
                    line.pop(-1)
                    temp_list.append(line)
                    length = len(line)
        return temp_list
          
 