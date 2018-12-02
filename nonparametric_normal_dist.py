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
    print 'new data'
    da = map(prettyfloat, [llr for llr, S in subset_stat])
    print da
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
    print 'LLRs'
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
        p_value = 1 - scipy.stats.binom(30, p_0).cdf(observation)
        #        print idx+1, observation, p_value
        p_values.append([idx + 1, p_value])

    signfciant_observations = [item for item in p_values if item[1] <= alpha]
    return signfciant_observations


def main():
    hist = [[43,37,40,39,43,42,34,37,37,37,42,41],
        [42,38,38,37,39,39,46,42,39,37,42,41],
        [41,48,39,43,45,39,41,41,38,43,40,38],
        [36,38,35,37,38,45,43,42,41,34,41,41],
        [39,43,41,39,40,39,48,42,44,39,34,41],
        [37,38,40,34,43,47,40,33,37,44,40,37],
        [37,41,41,46,43,36,41,36,45,40,38,42],
        [41,39,43,43,41,43,40,38,42,33,41,37],
        [38,37,37,43,36,39,38,40,41,41,37,34],
        [42,42,39,37,40,36,38,41,45,44,44,37]]

    new_day = [27,31,41,39,29,26,26,40,37,36,36,40]
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

# sum_measurements = 0
# for day in range(10):
#    sum_measurements += sum(hist[day])
# mu = sum_measurements / (10.0 * count)

# print hist
