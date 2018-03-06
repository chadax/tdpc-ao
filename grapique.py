import numpy as np
import matplotlib.pyplot as plt

def graph(label_data , data , title , data_title):
    y_pos = np.arange(len(label_data))

    plt.barh(y_pos, data)
    plt.title(title)
    plt.yticks(y_pos,label_data)
    plt.xlabel(data_title)
    plt.show()

