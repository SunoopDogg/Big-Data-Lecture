import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter


def getTaggedDataFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_data_{YM}.csv', index_col=0)
    return data


def getTitleFromCSV(tag, YM):
    data = getTaggedDataFromCSV(tag, YM)
    title = data['title']
    return title.tolist()


def getTaggedFromTitle(title):
    title = [t.replace('_', ' ') for t in title]
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = []
    for t in title:
        tokens.extend(tokenizer.tokenize(t))
    tokens = [t.lower() for t in tokens]
    tagged = nltk.pos_tag(tokens)
    return tagged


def getNNPFromTagged(tagged):
    NNP = []
    for t in tagged:
        if t[1] == 'NNP' or t[1] == 'NNPS' or t[1] == 'NN':
            NNP.append(t[0])
    return NNP


def collectionToCSV(tag, YM, collections):
    df = pd.DataFrame(collections, columns=['word', 'count'])
    df.to_csv(f'{tag}\{tag}_collections_{YM}.csv')


if __name__ == '__main__':
    tags = ['c', 'c++', 'c#', 'java', 'javascript',
            'python', 'sql', 'typescript', 'html', 'css']

    year = {
        2012: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2022: [1,  2,  3, 4,  5,  6,  7,  8,  9, 10],
    }

    for tag in tags:
        for y in year:
            for m in year[y]:
                YM = f'{y}-{m:02}'
                print(f'{tag} {YM}')
                title = getTitleFromCSV(tag, YM)
                tagged = getTaggedFromTitle(title)
                NNP = getNNPFromTagged(tagged)
                collections = Counter(NNP).most_common()
                collectionToCSV(tag, YM, collections)
