import matplotlib.pyplot as plt
import pandas as pd


def getCollectionFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_collections_{YM}.csv', index_col=0)
    return data


def cleanData(data):
    # data = data[data['count'] > 10]
    data = data[data['word'].str.len() > 1]
    data = data[data['word'] != tag]

    cleanTarget = ['error', 'js', 'type']
    data = data[~data['word'].isin(cleanTarget)]

    return data


if __name__ == '__main__':
    # tags = ['javascript', 'python', 'c#', 'c++', 'c',
    #         'java', 'sql', 'typescript', 'html', 'css']
    tags = ['java']

    year = {
        # 2009: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2012: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        # 2019: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        # 2020: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        # 2021: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        # 2022: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
    }

    # for tag in tags:
    #     for y in year:
    #         for m in year[y]:
    #             YM = f'{y}-{m:02}'
    #             print(f'{tag} {YM}')
    #             data = getCollectionFromCSV(tag, YM)
    #             data = cleanData(data)
    #             cnt = data['count'].sum()
    #             data = data.head(5)
    #             # data.loc['0'] = ['other', cnt - data['count'].sum()]

    #             explode = [0.05, 0.05, 0.05, 0.05, 0.05]
    #             colors = ['#41a4ff', '#ff914d', '#7ed957',
    #                       '#FFACAC', '#B7A1FF']  # , '#d0d0d0'

    #             plt.pie(data['count'], labels=data['word'],
    #                     autopct='%.1f%%', startangle=90, counterclock=False, explode=explode, colors=colors)

    #             plt.savefig(f'{tag}\{tag}_pie_{YM}.png',
    #                         bbox_inches='tight', pad_inches=0.5)

    #             plt.clf()

    for tag in tags:
        for y in year:
            dataMerge = pd.DataFrame()
            for m in year[y]:
                YM = f'{y}-{m:02}'
                print(f'{tag} {YM}')
                data = getCollectionFromCSV(tag, YM)
                data = cleanData(data)
                dataMerge = pd.concat([dataMerge, data], axis=0)

            dataMerge = dataMerge.groupby('word').sum().sort_values(
                'count', ascending=False).reset_index()
            dataMerge.to_csv(f'{tag}\{tag}_merge_{y}.csv')

            dataMerge = dataMerge.head(5)
            print(dataMerge)

            explode = [0.05, 0.05, 0.05, 0.05, 0.05]
            colors = ['#41a4ff', '#ff914d', '#7ed957', '#FFACAC', '#B7A1FF']
            plt.pie(dataMerge['count'], labels=dataMerge['word'] + ' ' + dataMerge['count'].astype(
                str), autopct='%.1f%%', startangle=90, counterclock=False, explode=explode, colors=colors)

            plt.savefig(f'{tag}\{tag}_pie_{y}.png',
                        bbox_inches='tight', pad_inches=0.5)

            plt.clf()
