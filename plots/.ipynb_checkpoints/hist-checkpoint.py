import csv
from matplotlib import pyplot as plt
import numpy as np


def read_file():
    col_names = []
    data = []
    with open('video_games_sales.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        col_names = next(csv_reader)
        data = [[row[0], row[1], row[2], float(row[3])] for row in csv_reader]

    return col_names, data


def create_dict(col_names, data):
    data_dict = {}

    cols = tuple(zip(*data))

    for i in range(len(col_names)):
        data_dict[col_names[i]] = np.array(cols[i])

    return data_dict


def hist_platforms_best_global_sales(data_dict):
    # ploting a histogram of the 10  game platforms with the most times in the vest selli. game list

    platforms, indices = [], []
    platforms, indices = np.unique(data_dict['Platform'], return_index=True)

    # test using the function np.bincount()
    # using indices and values ​​in the column "Global_Sales" of data_dict in order to calculate the sums of sales f each platform to column

    sales_sum = []
    sales_sum = np.bincount(data_dict['Global_Sales'], indices)

    # for i in indices:

    #     if i=

    # associating each platform with its number of sales
    platforms_sales = []
    platforms_sales = zip(platforms, sales_sum)

    # rearrange this list in descending order of sales
    platforms_sales = []
    platforms_sales = platforms_sales[::-1].sort()

    # create lists of platforms and their sales
    platforms, sales = [], []

    for platform, sale in platforms_sales:
        platforms.append(platform)
        sale.append(sale)

    bar = plt.bar()

    # displaying values on top of hist bars
    for rect in bar:
        # plt.text(platform[1][rect],platform[0][rect],str(platform[0][rect]))

    plt.title("owidi video games data plottings")

    plt.xlabel('Platforms')
    plt.ylabel('game sales (in millions of copies)')

    plt.show()


if __name__ == '__main__':
    names, data = read_file()

    data_dict = create_dict(names, data)

    hist_platforms_best_global_sales(data_dict)
