__author__ = 'fengchen'

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:30:03 2014

@author: Feng Chen
"""
import scipy.stats
import numpy as np
import json
from scipy.stats import norm
import math


class prettyfloat(float):
    def __repr__(self):
        return "%0.2f" % self


def calc_null_parameters(hist):
    count = len(hist[0])  # Total number of measurements per day
    observations = [item for sublist in hist for item in sublist]
    # p_0 = sum(observations) / (len(observations) * 30.0)
    p_0=np.mean(observations)
    std_0=np.std(hist)
    print p_0
    print std_0
    return p_0,std_0


def calc_alter_parameters(new, S):
    #count= len(S)
    alter_observations = [new[i] for i in S]  # Set of observations from the distribution related to event under alternative hypothesis
    #p_1 = sum(alter_observations) / (len(alter_observations) * 30.0)
    p_1 = np.mean(alter_observations)
    #new_stdev=np.std(alter_observations)
    return p_1


def calc_likelihood_ratio(new, S,std_0, p_0, p_1):
    log_likelihood_ratio = 0
    for i in S:
        item1 = math.log(scipy.stats.norm(p_1,std_0).pdf(new[i]))
        item2 = math.log(scipy.stats.norm(p_0,std_0).pdf(new[i]))
        log_likelihood_ratio = log_likelihood_ratio + item1 - item2
    print "LLR",log_likelihood_ratio
    return log_likelihood_ratio


def day_process(day_observations,std_0, p_0):
    subset_stat = []  # llr: log likelihood ratio
    count = len(day_observations)  # Total number of measurements in the current day
    for C in range(count+1):
        for z in range(C,count+1):
           # V_minus_S = range(C)
            S = range(C, z)
            if len(S) > 0:
                p_1 = calc_alter_parameters(day_observations, S)
            else:
                p_1 = 0
            llr = calc_likelihood_ratio(day_observations, S,std_0, p_0, p_1)
            subset_stat.append([llr, S])
    [best_llr, best_subset] = max(subset_stat, key=lambda item: item[0])
    return best_llr, best_subset, subset_stat


def anomalous_subset_detection(hist, new_day, alpha):
    # Calcualte the mean and standard deviation of normal bload pressure
    p_0 ,std_0 = calc_null_parameters(hist)

    """
    Step 1: Identify the best subset S*
    """
    [best_llr, best_subset, subset_stat] = day_process(new_day,std_0, p_0)

    da = map(prettyfloat, [llr for llr, S in subset_stat])

    print '+++++++++++++++++++++++++'

    hist_day_max_llrs = []
    """
    Step 2: Caldualte empirical p-value of the best subset S*
    """
    llrs = []
    for hist_day in hist:
        [best_hist_day_llr, best_hist_day_subset, subset_stat] = day_process(hist_day,np.std(hist), p_0)
        llrs.append([llr for llr, S in subset_stat])
        hist_day_max_llrs.append(best_hist_day_llr)
    for items in llrs:
        da = map(prettyfloat, items)
        print da

    da = map(prettyfloat, hist_day_max_llrs)
    # print 'LLRs'
    print da

    empirical_p_value = len([item for item in hist_day_max_llrs if item > best_llr]) / (1.0 * len(hist_day_max_llrs))

    if empirical_p_value <= alpha:
        return empirical_p_value, best_subset
    else:
        return None, None


def anomalous_point_detection(hist, new_day, alpha):
    # Calcualte the mean and standard deviation of normal bload pressure
    p_0 = calc_null_parameters(hist)
    print p_0
    # Calculate the p-value of individual observations in new_day
    p_values = []
    for idx, observation in enumerate(new_day):
        p_value = 1 - scipy.stats.norm(30, p_0).cdf(observation)
        #        print idx+1, observation, p_value
        p_values.append([idx + 1, p_value])

    signfciant_observations = [item for item in p_values if item[1] <= alpha]
    return signfciant_observations


def main():
    hist = [[68.05680264516128, 66.93892817857143, 65.8490321935484, 64.5239897, 64.41869383870967, 64.43204623333334, 64.42004025806452, 63.976866774193546, 64.40885999999999, 65.05859754838711, 64.83987113333335, 64.21648770967741],
            [67.27909483870967, 68.25780341379311, 66.90909751612902, 66.46393513333334, 66.94090425806453, 67.2566731, 67.14910122580645, 66.93645848387096, 66.73580016666666, 66.73161819354839, 67.70613713333331, 67.79911293548386]]
    # 2018 data
    new_day = [63.61552119354839, 64.44885832142856, 65.04169216129033, 65.68700323333333, 67.50892812903224, 67.75483848387097, 68.6614654516129, 69.57460880645161, 72.23412933333334, 73.73052035483872, 72.15457015999999]
    #2017 data
    # new_day = [68.05680264516128, 66.93892817857143, 65.8490321935484, 64.5239897, 64.41869383870967, 64.43204623333334,
    #            64.42004025806452, 63.976866774193546, 64.40885999999999, 65.05859754838711, 64.83987113333335,
    #            64.21648770967741]
    alpha = 0.05  # confidence interval
    empirical_p_value, best_subset = anomalous_subset_detection(hist, new_day, alpha)

    print '\n**************************************'
    print 'Strategy 1: Anomalous Subset Detection at the confidence interval: alpha = 0.05'
    if empirical_p_value != None:
        print 'The signficant subset and empirical p-value are: '
        print best_subset, empirical_p_value
    else:
        print 'No signficant subset is detected'
    print '**************************************\n'


    # [empirical_p_value, best_subset] = anomalous_subset_detection(hist, new_day, alpha)
    # signfciant_observations = anomalous_point_detection(hist, new_day, alpha)

    # print '\n**************************************'
    # print 'Strategy 2: Anomalous Points Detection at the confidence interval: alpha = 0.05'
    # if len(signfciant_observations) > 0:
    #     print 'The signficant points and empirical p-values are: '
    #     for [idx, p_value] in signfciant_observations:
    #         print idx, p_value
    # print '**************************************\n'

if __name__ == '__main__':
    main()

    pass

