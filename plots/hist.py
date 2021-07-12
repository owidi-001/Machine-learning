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
    """
    Function which returns a dictionary containing each of the columns present
    in data associated with their respective name present in col_names. Columns must
    be stored in the dictionary as a numpy array.

    example:
    col_names = ["A", "B"]
    data = [[1, 2], [3, 4]]

    return data_dict where
    
    data_dic = {
        "A": np.array ([1, 3])
        "B": np.array ([2, 4])
    }
    """
    data_dict = {}

    cols = tuple(zip(*data))

    for i in range(len(col_names)):
        data_dict[col_names[i]] = np.array(cols[i])

    return data_dict


def hist_platforms_best_global_sales(data_dict):
    """
    Function that displays a histogram of the 10 returning game platforms
    the most times in the best selling games list.
    """

    # TODO:
    # Use the np.unique() function to get the names of the platforms
    # as well as the indices representing their positions in the array to
    # the "Platform" column of data_dict

    """TODO call to the function np.unique ()"""
    platforms, indices = np.unique(data_dict['Platform'], return_inverse=True)

    # Using the np.bincount() function, use indices and values ​​in the
    # column "Global_Sales" of data_dict in order to calculate the sums of sales
    # of each platform to column

    """TODO call to the function np.bincount()"""
    sales_sum = np.bincount(indices, weights=data_dict["Global_Sales"])

    # Rearrange in descending order
    # 1. Create a list of tuples by associating each platform with its number of sales
    """TODO create a list of tuples associating each platform with its number of game sales"""
    platforms_sales = list(zip(platforms, sales_sum))

    # 2. Rearrange this list in descending order of sales
    """TODO sort platforms_sales list in descending order of sales"""
    # platforms_sales=platforms_sales[::-1].sort()
    platforms_sales = sorted(platforms_sales, key=lambda x: x[1], reverse=True)

    # 3. Create two lists, each containing the platforms and their sales respectively
    """TODO create two lists from platforms_sales"""
    platforms, sales = [], []

    for pair in platforms_sales:
        platforms.append(pair[0])
        sales.append(pair[1])

    # Generate the histogram of the 10 platforms that sold the most games until 2017
    """TODO generate the histogram of the first 10 platforms with a call to the plt.bar () function"""
    bar = plt.bar(platforms[:10], sales[:10])

    # Show numbers above histogram bars
    for rect in bar:
        #     """TODO for each rectangle of the histogram, display the text of the value of its height above"""
        plt.text(rect.xy[0], rect.get_height()+5, str(int(rect.get_height())))

    # Add a title to the chart
    """TODO add a title to the chart with a plt function"""
    plt.title("Video game platforms having sold the most games until 2017")

    # Add the titles of the axes of the graph
    """TODO add the names of the x and y axes to the graph"""
    plt.xlabel('Platforms')
    plt.ylabel('Game sales (in millions of copies)')

    # Show graph
    """TODO display graph"""
    plt.show()



if __name__ == '__main__':
    names, data = read_file()
    data_dict = create_dict(names, data)

    hist_platforms_best_global_sales(data_dict)