import matplotlib.pyplot as plt
import pandas as pd


def getMergeFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_merge_{YM}.csv', index_col=0)
    return data


if __name__ == '__main__':
    tags = ['c', 'c++', 'c#', 'java', 'javascript',
            'python', 'typescript', 'css', 'html', 'sql']

    year = {
        2012: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2022: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
    }

    for tag in tags:
        for y in year:
            data = getMergeFromCSV(tag, y)

            explode = [0.05, 0.05, 0.05, 0.05, 0.05]
            colors = ['#41a4ff', '#ff914d', '#7ed957', '#FFACAC', '#B7A1FF']
            plt.pie(data['count'], labels=data['word'] + ' ' + data['count'].astype(
                str), autopct='%.1f%%', startangle=90, counterclock=False, explode=explode, colors=colors)

            plt.savefig(f'{tag}\{tag}_pie_{y}.png',
                        bbox_inches='tight', pad_inches=0.5)

            plt.clf()
