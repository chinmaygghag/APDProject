import datetime
import numpy
import csv
import matplotlib.pyplot as plt


week1_2015_list = []
week2_2015_list = []
week3_2015_list = []
week4_2015_list = []


reader = csv.reader(open('2015/2015_final.csv', 'rb'))
for row in reader:
	date = datetime.datetime.strptime(row[0],'%Y-%m-%d')

	if date.day in range(1,7):
		week1_2015_list.append(float(row[3]))
	elif date.day in range(8,14):
		week2_2015_list.append(float(row[3]))
	elif date.day in range(15,21):
		week3_2015_list.append(float(row[3]))
	else:
		week4_2015_list.append(float(row[3]))





y2015 = [numpy.mean(week1_2015_list),
		 numpy.mean(week2_2015_list),
		 numpy.mean(week3_2015_list),
		 numpy.mean(week4_2015_list)]



week1_2016_list = []
week2_2016_list = []
week3_2016_list = []
week4_2016_list = []


reader = csv.reader(open('2016/2016_final.csv', 'rb'))
for row in reader:
	date = datetime.datetime.strptime(row[0],'%Y-%m-%d')

	if date.day in range(1,7):
		week1_2016_list.append(float(row[3]))
	elif date.day in range(8,14):
		week2_2016_list.append(float(row[3]))
	elif date.day in range(15,21):
		week3_2016_list.append(float(row[3]))
	else:
		week4_2016_list.append(float(row[3]))





y2016 = [numpy.mean(week1_2016_list),
		 numpy.mean(week2_2016_list),
		 numpy.mean(week3_2016_list),
		 numpy.mean(week4_2016_list)]




week1_2017_list = []
week2_2017_list = []
week3_2017_list = []
week4_2017_list = []


reader = csv.reader(open('2017/2017_final.csv', 'rb'))
for row in reader:
	date = datetime.datetime.strptime(row[0],'%Y-%m-%d')

	if date.day in range(1,7):
		week1_2017_list.append(float(row[3]))
	elif date.day in range(8,14):
		week2_2017_list.append(float(row[3]))
	elif date.day in range(15,21):
		week3_2017_list.append(float(row[3]))
	else:
		week4_2017_list.append(float(row[3]))





y2017 = [numpy.mean(week1_2017_list),
		 numpy.mean(week2_2017_list),
		 numpy.mean(week3_2017_list),
		 numpy.mean(week4_2017_list)]



week1_2018_list = []
week2_2018_list = []
week3_2018_list = []
week4_2018_list = []


reader = csv.reader(open('2018/2018_final.csv', 'rb'))
for row in reader:
	date = datetime.datetime.strptime(row[0],'%Y-%m-%d')

	if date.day in range(1,7):
		week1_2018_list.append(float(row[3]))
	elif date.day in range(8,14):
		week2_2018_list.append(float(row[3]))
	elif date.day in range(15,21):
		week3_2018_list.append(float(row[3]))
	else:
		week4_2018_list.append(float(row[3]))





y2018 = [numpy.mean(week1_2018_list),
		 numpy.mean(week2_2018_list),
		 numpy.mean(week3_2018_list),
		 numpy.mean(week4_2018_list)]







week_1 = []
week_2 = []
week_3 = []
week_4 = []




for val2017 in week1_2017_list:
	week_1.append(val2017)
for val2016 in week1_2016_list:
	week_2.append(val2016)
for val2015 in week2_2015_list:
	week_3.append(val2015)


for val2017 in week2_2017_list:
	week_2.append(val2017)
for val2016 in week2_2016_list:
	week_2.append(val2016)
for val2015 in week2_2015_list:
	week_2.append(val2015)

for val2017 in week3_2017_list:
	week_3.append(val2017)
for val2016 in week3_2016_list:
	week_3.append(val2016)
for val2015 in week3_2015_list:
	week_3.append(val2015)

for val2017 in week4_2017_list:
	week_4.append(val2017)
for val2016 in week4_2016_list:
	week_4.append(val2016)
for val2015 in week4_2015_list:
	week_4.append(val2015)



test_data_week1 = numpy.mean(week1_2018_list)
test_data_week2 = numpy.mean(week2_2018_list)
test_data_week3 = numpy.mean(week3_2018_list)
test_data_week4 = numpy.mean(week4_2018_list)





x = ['Week 1','Week 2','Week 3','Week 4']


# Code for graph plotting
plt.xticks(range(len(y2015)),x)
plt.plot(y2015)
plt.ylabel('2015')
plt.show()


mean_of_data_week1 = numpy.mean(week_1)
stand_dev_week1 = numpy.std(week_1)

a = (test_data_week1 - mean_of_data_week1)/stand_dev_week1
print "Week1 z-score",a
print "Mean of Week1",mean_of_data_week1
print "Stand Dev of Week1", stand_dev_week1


mean_of_data_week2 = numpy.mean(week_2)
stand_dev_week2 = numpy.std(week_2)

a = (test_data_week2 - mean_of_data_week2)/stand_dev_week2
print "week2 z-score",a
print "Mean of week2",mean_of_data_week2
print "Stand Dev of week2", stand_dev_week2



mean_of_data_week3 = numpy.mean(week_3)
stand_dev_week3 = numpy.std(week_3)

a = (test_data_week3 - mean_of_data_week3)/stand_dev_week3
print "week3 z-score",a
print "Mean of week3",mean_of_data_week3
print "Stand Dev of week3", stand_dev_week3




mean_of_data_week4 = numpy.mean(week_4)
stand_dev_week4 = numpy.std(week_4)

a = (test_data_week4 - mean_of_data_week4)/stand_dev_week4
print "week4 z-score",a
print "Mean of week4",mean_of_data_week4
print "Stand Dev of week4", stand_dev_week4
