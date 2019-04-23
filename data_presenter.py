import json
import matplotlib.pyplot as plt
import numpy as np


class DataPresenter:
    @staticmethod
    def prepare_data(data, labels, conf_matrix_param, label_name):
        tp = []
        for intent in data[0][label_name]:
            for label in labels:
                # print(type(intent[label][0][conf_matrix_param]))
                label_data_name = intent[label][0][conf_matrix_param]
                # print(label_data_name)
                if label_data_name == 'null':
                    label_data_name = 'Null response'
                if label_data_name == 'n.a.':
                    label_data_name = 0
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
                 label='Wat')

        plot.bar(index + bar_width, bar2, bar_width,
                 alpha=opacity, color='r',
                 error_kw=error_config,
                 label='Dial')
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

        labels =[label for label in labels if label != 'notFound']
        print(labels)
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1)
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
        self.prepare_bars(ax4, first_data, second_data,
                          label_name,
                          'F1 score',
                          label_name+': Compare F1 score',
                          labels,
                          'f1',
                          label_name)
        # self.prepare_bars(ax2, FN1, FN2, 'Intents', 'False Negative', 'Intents: Compare false negatives', labels)
        fig.tight_layout()

    def bar_presenter(self, first_data_file, second_data_file):
        first_data = json.load(open(first_data_file))
        second_data = json.load(open(second_data_file))
        self.prepare_figure(first_data, second_data, 'intents')
        self.prepare_figure(first_data, second_data, 'entities')

        plt.show()
