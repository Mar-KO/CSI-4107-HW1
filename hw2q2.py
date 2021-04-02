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
import textwrap


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
print(textwrap.shorten(str(weights), width=50))



# %%
import ranking
import queryutils
import gensim
from gensim.models import Word2Vec

## Query and ranking using CosSim

dvl = weighting.computeDocumentVectorLengths(docs_tokenized, weights)
queryData = queryutils.importQueries()
results = io.open('Results.txt', 'w')
model = Word2Vec(df["title"].tolist())

for query in queryData:
    print(f'Adding synonyms for query {query.num}...')
    newQuery = ranking.addSynonyms(query.text, model, df)
    print(f'Ranking query {query.num}...')
    similarityRankings = ranking.queryRanking(newQuery, weights, invIndex, sp, dvl)
    series = pd.Series(similarityRankings).sort_values(ascending=False).head(1000)
    count = 0
    print(f'Writing results to Results.txt...')
    for doc, value in series.iteritems():
        count = count + 1
        results.write(f'{query.num} Q0 {doc} {count} {value} run3\n')
results.close()
