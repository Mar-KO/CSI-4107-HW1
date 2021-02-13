import pandas as pd
import numpy as np
import weighting
from tokenizer import QueryData


def queryRanking(query, tfidf_df):
    weightDict = weighting.queryWeighting(query)
    
    pass