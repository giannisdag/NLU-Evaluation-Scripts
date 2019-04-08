import json
import matplotlib.pyplot as plt
import numpy as np


class DataPresenter:
    def prepare_data(self, data, labels, conf_matrix_param, label_name):
        tp = []
        for intent in data[0][label_name]:
            for label in labels:
                label_data_name = intent[label][0][conf_matrix_param]
                if label_data_name == 'null':
                    label_data_name = 'Null response'
                tp.append(label_data_name)
        return tp

    def prepare_bars(self, plot, data1, data2, x_label, y_label, title, labels, conf_matrix_param, label_name):
        n_groups = len(labels)
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.4
        bar1 = self.prepare_data(data1, labels, conf_matrix_param, label_name)
        bar2 = self.prepare_data(data2, labels, conf_matrix_param, label_name)

        error_config = {'ecolor': '0.3'}
        plot.bar(index, bar1, bar_width,
                 alpha=opacity, color='b',
                 error_kw=error_config,
                 label='Watson')

        plot.bar(index + bar_width, bar2, bar_width,
                 alpha=opacity, color='r',
                 error_kw=error_config,
                 label='Dialog flow')
        plot.set_xlabel(x_label)
        plot.set_ylabel(y_label)
        plot.set_title(title)
        plot.set_xticks(index + bar_width / 2)
        plot.set_xticklabels(labels)
        plot.legend()
        return plot

    def prepare_figure(self, first_data, second_data, label_name):
        labels = []
        keys = list(first_data[0][label_name][0].keys())
        print(keys)
        for key in keys[:-3]:
            labels.append(key)

        print(labels)
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
        # fig.subplots_adjust(hspace=0.4, wspace=0.4)
        self.prepare_bars(ax1, first_data, second_data,
                          label_name,
                          'True Positive',
                          label_name+': Compare true positives',
                          labels,
                          'truePos',
                          label_name)
        self.prepare_bars(ax2, first_data, second_data,
                          label_name,
                          'False Negative',
                          label_name+': Compare false negatives',
                          labels,
                          'falseNeg',
                          label_name)
        self.prepare_bars(ax3, first_data, second_data,
                          label_name,
                          'False Positive',
                          label_name+': Compare false Positives',
                          labels,
                          'falsePos',
                          label_name)
        # self.prepare_bars(ax2, FN1, FN2, 'Intents', 'False Negative', 'Intents: Compare false negatives', labels)
        fig.tight_layout()



    def bar_presenter(self, first_data_file, second_data_file):
        first_data = json.load(open(first_data_file))
        second_data = json.load(open(second_data_file))
        self.prepare_figure(first_data, second_data, 'intents')
        self.prepare_figure(first_data, second_data, 'entities')

        plt.show()

        # rects1 = ax[0].bar(index, TP1, bar_width,
        #                    alpha=opacity, color='b',
        #                    error_kw=error_config,
        #                    label='Watson')
        #
        # rects2 = ax[0].bar(index + bar_width, TP2, bar_width,
        #                    alpha=opacity, color='r',
        #                    error_kw=error_config,
        #                    label='Dialog flow')
        #
        # ax[1].bar(index, TP3, bar_width,
        #           alpha=opacity, color='b',
        #           error_kw=error_config,
        #           label='Watson')
        #
        # ax[1].bar(index + bar_width, TP4, bar_width,
        #           alpha=opacity, color='r',
        #           error_kw=error_config,
        #           label='Dialog flow')



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
