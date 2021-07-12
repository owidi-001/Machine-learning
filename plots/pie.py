import csv
from matplotlib import pyplot as plt
import numpy as np


def read_file():
    col_names = []
    data = []
    with open ('video_games_sales.csv', 'r') as file:
        csv_reader = csv.reader (file, delimiter = ',')

        col_names = next(csv_reader)
        data = [[row[0], row[1], row[2],float(row[3])] for row in csv_reader]

    return col_names,data

def create_dict(col_names, data):
    data_dict ={}

    cols = tuple(zip(*data))

    for i in range(len(col_names)):
        data_dict[col_names[i]] = np.array(cols[i])

    return data_dict


def pie_genre(data_dict):
    genre,counts = [],[]
    genre,counts=np.unique(data_dict['Genre'],return_counts=True)

    plt.pie(counts,labels=genre,autopct='%1.1f%%')

    plt.title("Distribution of genres among the best-selling video games until 2017 ")

    plt.show()


if __name__ == '__main__':
    names,data = read_file()

    data_dict = create_dict(names, data)


    pie_genre(data_dict)