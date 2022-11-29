import matplotlib.pyplot as plt
import pandas as pd


def getMergeFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_Merges_{YM}.csv', index_col=0)
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
            'python', 'typescript', 'css', 'html', 'sql']

    year = {
        2012: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2022: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
    }

    top5 = getCollectionFromCSV('python', '2022-01')
    top5 = cleanData(top5, 'python')
    top5 = top5.head(5)

    print(top5)

    # for tag in tags:
    #     for y in year:
    #         dataMerge = pd.DataFrame()
    #         for m in year[y]:
    #             YM = f'{y}-{m:02}'
    #             print(f'{tag} {YM}')
    #             data = getCollectionFromCSV(tag, YM)
    #             data = cleanData(data, tag)

    #             dataMerge = pd.concat([dataMerge, data], axis=0)

    #         dataMerge = dataMerge.groupby('word').sum().sort_values(
    #             'count', ascending=False).reset_index()
    #         dataMerge.to_csv(f'{tag}\{tag}_merge_{y}.csv')

    #         dataMerge = dataMerge.head(5)
    #         print(dataMerge)

    #         explode = [0.05, 0.05, 0.05, 0.05, 0.05]
    #         colors = ['#41a4ff', '#ff914d', '#7ed957', '#FFACAC', '#B7A1FF']
    #         plt.pie(dataMerge['count'], labels=dataMerge['word'] + ' ' + dataMerge['count'].astype(
    #             str), autopct='%.1f%%', startangle=90, counterclock=False, explode=explode, colors=colors)

    #         plt.savefig(f'{tag}\{tag}_pie_{y}.png',
    #                     bbox_inches='tight', pad_inches=0.5)
