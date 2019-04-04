import json

import matplotlib.pyplot as plt
import numpy as np


class DataPresenter:
    def prepare_data(self, data, labels):
        tp = []
        for intent in data[0]['intents']:
            for label in labels:
                tp.append(intent[label][0]['truePos'])
        return tp

    def bar_presenter(self, first_data_file, second_data_file):
        first_data = json.load(open(first_data_file))
        second_data = json.load(open(second_data_file))
        labels = []
        keys = list(first_data[0]['intents'][0].keys())
        for key in keys[:-4]:
            labels.append(key)

        TP1 = self.prepare_data(first_data, labels)
        TP2 = self.prepare_data(second_data, labels)
        n_groups = len(labels)

        fig, ax = plt.subplots()

        index = np.arange(n_groups)

        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, TP1, bar_width,
                        alpha=opacity, color='b',
                        error_kw=error_config,
                        label='Watson')

        rects2 = ax.bar(index + bar_width, TP2, bar_width,
                        alpha=opacity, color='r',
                        error_kw=error_config,
                        label='Dialog flow')

        ax.set_xlabel('Intents')
        ax.set_ylabel('True Positive')
        ax.set_title('Compare true positives')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(labels)
        ax.legend()

        fig.tight_layout()
        plt.show()


'''

men_means, men_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                color='SkyBlue', label='Men')
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                color='IndianRed', label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()
'''
