import xml.etree.ElementTree as ET
import re

class Query(object):

    def __init__(self):
        self.text = ""
        self.num = 0
    
    def __str__(self):
        return f'{self.num}, {self.text}'
    
    def __repr__(self):
        return f'Query(num={self.num}, text={self.text})'

def importQueries():
    root = ET.parse('Queries.txt').getroot()
    query_list = []
    for child in root:
        query = Query()
        query.num = int(re.findall(r'\d+', child[0].text)[0])
        query.text = child[1].text
        query_list.append(query)
    return query_list
