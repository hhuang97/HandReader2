from __future__ import unicode_literals, print_function, division, absolute_import
from bin.read_mnist import read_num

import numpy as np
import matplotlib.pyplot as plt


def main():
    model, totals = train()
    produce_heatmap(model, True, True)
    right, wrong = predict(model, totals, True)
    print("Accuracy: %.4f" % (float(right)/wrong))

def train():
    model = np.zeros([10, 28, 28])
    totals = np.zeros(10) # accumulate total
    generator_func = read_num('training') # generator to read numbers
    for arr, num in generator_func:
        model[num] += arr
        totals[num] += 1
    produce_heatmap(model, True, True)
    
    return model, totals

def predict(model, totals):
    total_num = 0
    right = 0
    pred = process(model, totals, vv)
    for p, n in pred:
        if p == n:
            right += 1
        total_num += 1
        if v:
            if total_num == 50:
                print("%6d" % (total_num))
            elif total_num % 50 == 0:
                print("\r%6d" % (total_num))
        if (not every) and total_num == t_max:
            print("\rDone")
            return right, total_num

    return right, total_num

def process(model, totals, v = False):
    test_set = read_num('test')
    prob = np.vectorize(map_prob)
    for arr, num in test_set:
        prob_map = [np.multiply.reduce(np.multiply.reduce(prob(arr, model[i], totals[i]))) for i in range(10)]
        predict = np.argmax(prob_map)
        if v:
            if predict != num:
                pprint_num(arr)
        yield predict, num


def map_prob(test_elm, model_elm, total):
    outof = model_elm
    if test_elm == 0:
        outof = total - outof

    return (np.float128(outof) + 1) / (total + 11)


####################################
# Utility Functions for you to use #
####################################

def pprint_num(arr_like):
    dash = "-" * 28
    print(dash)
    for i in range(len(arr_like)):
        str_build = ""
        for j in range(len(arr_like[0])):
            str_build += "%d" % (arr_like[i][j])
        print(str_build)
    print(dash)

def produce_heatmap(model, every = True, save = False):
    col_label = range(28)
    row_label = range(28)
    if every:
        for i in range(10):
            plt.pcolor(np.flipud(model[i]))
            plt.xticks(col_label)
            plt.yticks(row_label)
            plt.axis('off')
            plt.title("HeatMap for %d" % (i))
            cb = plt.colorbar()
            cb.set_label("Frequency")
            if save:
                plt.savefig('imgs/%d.png' % (i), bbox_inches='tight')
            else:
                plt.show()
            plt.close()
    else:
        plt.pcolor(np.flipud(model))
        plt.xticks(col_label)
        plt.yticks(row_label)
        plt.axis('off')
        cb = plt.colorbar()
        cb.set_label("Frequency")
        if save:
            plt.savefig('imgs/temp.png', bbox_inches='tight')
        else:
            plt.show()
        plt.close()

######################
# Internal Functions #
######################

if __name__ == '__main__':
    main()