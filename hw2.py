# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'




# %%
from IPython import get_ipython

# %% [markdown]
# # Assignment 2

# %%
import spacy
import pandas as pd 
import numpy as np


# %%
sp = spacy.load("en_core_web_sm")

#read the tweets
df = pd.read_csv("Twitter.txt", '\t', names=['querytweettime', 'title'])
docs = df["title"]
print(df.dtypes)


# %%
import tokenizer
import io
import pickle
    
docs_mini = df.head(20)

## Open documents
try:
    with open('tokenizedDataFrame.bin', 'rb+') as pickle_file:
        docs_tokenized = pickle.load(pickle_file)
except:
    docs_tokenized = df.apply(tokenizer.tokenize, 1, spacy=sp)
    with open('tokenizedDataFrame.bin', 'wb') as pickle_file:
        rawdocs = pickle.dump(docs_tokenized, pickle_file)
print(docs_tokenized)


# %%
from index import InvertedIndex, indexDocs
invIndex = InvertedIndex()


for label, data in docs_tokenized.iterrows():
    indexDocs(data, invIndex)

print(list(invIndex.dict().keys())[:100])



# %%
a = invIndex.dict()
print(len(a.keys()))


# %%
## TF-IDF
import weighting
weights = weighting.indexWeighting(invIndex)
print(weights)



# %%
import ranking
import queryutils

## Query and ranking using CosSim

dvl = weighting.computeDocumentVectorLengths(docs_tokenized, weights)
queryData = queryutils.importQueries()
results = io.open('Results.txt', 'w')

from pygaggle.rerank.base import Query, Text
from pygaggle.rerank.transformer import MonoBERT

reranker =  MonoBERT()

for query in queryData:
    similarityRankings = ranking.queryRanking(query.text, weights, invIndex, sp, dvl)
    series = pd.Series(similarityRankings).sort_values(ascending=False).head(1000)
    texts = [ Text(df.loc[df.querytweettime.isin([doc]), 'title'].tolist()[0], {'docid': doc}, 0) for doc, value in series.iteritems()]
    count = 0
    queryObject = Query(query.text)
    reranked = reranker.rerank(queryObject, texts)
    reranked.sort(key=lambda x: x.score, reverse=True)
    for doc, value in series.iteritems():
        count = count + 1
        results.write(f'{query.num} Q0 {doc} {count} {value} run1\n')
    count = 1
    for text in reranked:
        results.write(f'{query.num} Q0 {text.metadata['docid']} {count} {text.score} run2\n')
        count = count + 1
results.close()



# %%

## start using BERT