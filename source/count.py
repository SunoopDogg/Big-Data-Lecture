import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter


def getTaggedDataFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_data_{YM}.csv', index_col=0)
    return data


def getTitleFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_data_{YM}.csv', index_col=0)
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


def getCollectionFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_collections_{YM}.csv', index_col=0)
    return data


def cleanData(data, tag):
    data = data[data['word'].str.len() > 1]
    data = data[data['word'] != tag]

    cleanTarget = ['error', 'js', 'type', 'function', 'file',
                   'list', 'code', 'value', 'class', 'array',
                   'column', 'model', 'struct', 'string', 'number',
                   'char', 'input', 'output', 'loop', 'fault',
                   'method', 'div', 'element', 'button', 'page',
                   'color', 'form', 'exception', 'object', 'project',
                   'component', 'table', 'date', 'row', 'join',
                   'group', 'property', 'ts', 'way']
    data = data[~data['word'].isin(cleanTarget)]

    return data


if __name__ == '__main__':
    tags = ['c', 'c++', 'c#', 'java', 'javascript',
            'python', 'sql', 'typescript', 'html', 'css']

    year = {
        2012: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2019: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2020: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2021: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
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

    for tag in tags:
        for y in year:
            dataMerge = pd.DataFrame()
            for m in year[y]:
                YM = f'{y}-{m:02}'
                print(f'{tag} {YM}')
                data = getCollectionFromCSV(tag, YM)
                data = cleanData(data, tag)
                dataMerge = pd.concat([dataMerge, data], axis=0)

            dataMerge = dataMerge.groupby('word').sum().sort_values(
                'count', ascending=False).reset_index()
            dataMerge.to_csv(f'{tag}\{tag}_merge_{y}.csv')
