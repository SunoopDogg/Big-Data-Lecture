import matplotlib.pyplot as plt
import pandas as pd


def getCollectionFromCSV(tag, YM):
    data = pd.read_csv(f'{tag}\{tag}_collections_{YM}.csv', index_col=0)
    return data
