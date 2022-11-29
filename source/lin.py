import matplotlib.pyplot as plt
import pandas as pd


def getMergeFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_merge_{YM}.csv', index_col=0)
    return data


def getCollectionFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_collections_{YM}.csv', index_col=0)
    return data


if __name__ == '__main__':
    tags = ['c', 'c++', 'c#', 'java', 'javascript',
            'python', 'typescript', 'css', 'html', 'sql']

    year = {
        # 2012: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        # 2019: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        # 2020: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        # 2021: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
        2022: [1,  2,  3,  4,  5,  6,  7,  8,  9],
    }

    for tag in tags:
        x_value = [f'{str(y)[2:]}{m:02d}' for y in year for m in year[y]]

        top5 = getMergeFromCSV(tag, '2022')['word'][:5].tolist()

        y1 = []
        y2 = []
        y3 = []
        y4 = []
        y5 = []

        for y in year:
            for m in year[y]:
                print(f'{y}-{m:02d}')
                data = getCollectionFromCSV(tag, f'{y}-{m:02}')
                y1.append(data[data['word'] == top5[0]]['count'].values[0]
                          if data[data['word'] == top5[0]]['count'].values else 0)
                y2.append(data[data['word'] == top5[1]]['count'].values[0]
                          if data[data['word'] == top5[1]]['count'].values else 0)
                y3.append(data[data['word'] == top5[2]]['count'].values[0]
                          if data[data['word'] == top5[2]]['count'].values else 0)
                y4.append(data[data['word'] == top5[3]]['count'].values[0]
                          if data[data['word'] == top5[3]]['count'].values else 0)
                y5.append(data[data['word'] == top5[4]]['count'].values[0]
                          if data[data['word'] == top5[4]]['count'].values else 0)

        plt.plot(x_value, y1, label=top5[0])
        plt.plot(x_value, y2, label=top5[1])
        plt.plot(x_value, y3, label=top5[2])
        plt.plot(x_value, y4, label=top5[3])
        plt.plot(x_value, y5, label=top5[4])

        plt.legend()

        plt.savefig(f'{tag}\{tag}_line_{y}.png',
                    bbox_inches='tight', pad_inches=0.5)

        plt.clf()
