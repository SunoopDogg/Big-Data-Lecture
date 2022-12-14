import time
import datetime
import requests
import pandas as pd


def getTaggedData(tag, fromDate, toDate):
    result = []

    page = 1
    url = f'https://api.stackexchange.com/2.3/search?page={page}&pagesize=100&fromdate={fromDate}&todate={toDate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'

    for _ in range(25):
        print(f'Getting page {url}...')

        r = requests.get(url)
        rJson = r.json()

        if 'items' not in rJson:
            print('No items found')
            break

        result.extend(rJson['items'])

        if rJson['has_more'] == False:
            print('No more pages')
            break
        else:
            page += 1
            url = f'https://api.stackexchange.com/2.3/search?page={page}&pagesize=100&fromdate={fromDate}&todate={toDate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'
            time.sleep(1)

    return result


def taggedDataToCSV(tag, fromDate, toDate):
    YM = datetime.datetime.fromtimestamp(fromDate).strftime('%Y-%m')
    data = getTaggedData(tag, fromDate, toDate)
    df = pd.DataFrame(data)
    df.to_csv(f'{tag}\{tag}_data_{YM}.csv')


if __name__ == '__main__':
    tags = ['c', 'c++', 'c#', 'java', 'javascript',
            'python', 'sql', 'typescript', 'html', 'css']

    year = [2012, 2022]

    month = {
        1: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        2: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        3: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        4: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        5: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        6: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        7: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        8: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        9: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        10: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        11: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        12: [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    }

    for tag in tags:
        for y in year:
            for m in month:
                fromDate = int(time.mktime(datetime.datetime(
                    y, m, month[m][0], 0, 0).timetuple()))
                toDate = int(time.mktime(datetime.datetime(
                    y, m, month[m][-1], 23, 59).timetuple()))
                print(f'Getting data for {tag} from {y}-{m}...')

                taggedDataToCSV(tag, fromDate, toDate)
                time.sleep(1)
