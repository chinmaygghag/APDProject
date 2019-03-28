import numpy
import csv
import matplotlib.pyplot as plt

mon_list2017 = []
tue_list2017 = []
wed_list2017 = []
thur_list2017 = []
fri_list2017 = []
sat_list2017 = []
sun_list2017 = []

mon_list2018 = []
tue_list2018 = []
wed_list2018 = []
thur_list2018 = []
fri_list2018 = []
sat_list2018 = []
sun_list2018 = []

mon_list2016 = []
tue_list2016 = []
wed_list2016 = []
thur_list2016 = []
fri_list2016 = []
sat_list2016 = []
sun_list2016 = []


mon_list2015 = []
tue_list2015 = []
wed_list2015 = []
thur_list2015 = []
fri_list2015 = []
sat_list2015 = []
sun_list2015 = []



reader = csv.reader(open('2017/2017_final.csv', 'rb'))
for row in reader:
	if row[4] == '0':
		sun_list2017.append(float(row[3]))
	elif row[4] == '1':
		mon_list2017.append(float(row[3]))
	elif row[4] == '2':
		tue_list2017.append(float(row[3]))
	elif row[4] == '3':
		wed_list2017.append(float(row[3]))
	elif row[4] == '4':
		thur_list2017.append(float(row[3]))
	elif row[4] == '5':
		fri_list2017.append(float(row[3]))
	else:
		sat_list2017.append(float(row[3]))



y2017 = [numpy.mean(sun_list2017),
		 numpy.mean(mon_list2017),
		 numpy.mean(tue_list2017),
		numpy.mean(wed_list2017),
		 numpy.mean(thur_list2017),
		 numpy.mean(fri_list2017),
		 numpy.mean(sat_list2017)]


reader2 = csv.reader(open('2016/2016_final.csv', 'rb'))
for row in reader2:
	if row[4] == '0':
		sun_list2016.append(float(row[3]))
	elif row[4] == '1':
		mon_list2016.append(float(row[3]))
	elif row[4] == '2':
		tue_list2016.append(float(row[3]))
	elif row[4] == '3':
		wed_list2016.append(float(row[3]))
	elif row[4] == '4':
		thur_list2016.append(float(row[3]))
	elif row[4] == '5':
		fri_list2016.append(float(row[3]))
	else:
		sat_list2016.append(float(row[3]))



y2016 = [numpy.mean(sun_list2016),
		 numpy.mean(mon_list2016),
		 numpy.mean(tue_list2016),
		numpy.mean(wed_list2016),
		 numpy.mean(thur_list2016),
		 numpy.mean(fri_list2016),
		 numpy.mean(sat_list2016)]


reader4 = csv.reader(open('2015/2015_final.csv', 'rb'))
for row in reader4:
	if row[4] == '0':
		sun_list2015.append(float(row[3]))
	elif row[4] == '1':
		mon_list2015.append(float(row[3]))
	elif row[4] == '2':
		tue_list2015.append(float(row[3]))
	elif row[4] == '3':
		wed_list2015.append(float(row[3]))
	elif row[4] == '4':
		thur_list2015.append(float(row[3]))
	elif row[4] == '5':
		fri_list2015.append(float(row[3]))
	else:
		sat_list2015.append(float(row[3]))



y2015 = [numpy.mean(sun_list2015),
		 numpy.mean(mon_list2015),
		 numpy.mean(tue_list2015),
		numpy.mean(wed_list2015),
		 numpy.mean(thur_list2015),
		 numpy.mean(fri_list2015),
		 numpy.mean(sat_list2015)]





reader1 = csv.reader(open('2018/2018_final.csv', 'rb'))
for row in reader1:
	if row[4] == '0':
		sun_list2018.append(float(row[3]))
	elif row[4] == '1':
		mon_list2018.append(float(row[3]))
	elif row[4] == '2':
		tue_list2018.append(float(row[3]))
	elif row[4] == '3':
		wed_list2018.append(float(row[3]))
	elif row[4] == '4':
		thur_list2018.append(float(row[3]))
	elif row[4] == '5':
		fri_list2018.append(float(row[3]))
	else:
		sat_list2018.append(float(row[3]))



y2018 = [numpy.mean(sun_list2018),
		 numpy.mean(mon_list2018),
		 numpy.mean(tue_list2018),
		numpy.mean(wed_list2018),
		 numpy.mean(thur_list2018),
		 numpy.mean(fri_list2018),
		 numpy.mean(sat_list2018)]

input_mon = []
input_tue = []
input_wed = []
input_thur = []
input_fri = []
input_sat = []
input_sun = []

for val2017 in mon_list2017:
	input_mon.append(val2017)
for val2016 in mon_list2016:
	input_mon.append(val2016)
for val2015 in mon_list2015:
	input_mon.append(val2015)


for val2017 in tue_list2017:
	input_tue.append(val2017)
for val2016 in tue_list2016:
	input_tue.append(val2016)
for val2015 in wed_list2015:
	input_wed.append(val2015)

for val2017 in wed_list2017:
	input_wed.append(val2017)
for val2016 in wed_list2016:
	input_wed.append(val2016)
for val2015 in wed_list2015:
	input_wed.append(val2015)

for val2017 in thur_list2017:
	input_thur.append(val2017)
for val2016 in thur_list2016:
	input_thur.append(val2016)
for val2015 in thur_list2015:
	input_thur.append(val2015)

for val2017 in fri_list2017:
	input_fri.append(val2017)
for val2016 in fri_list2016:
	input_fri.append(val2016)
for val2015 in fri_list2015:
	input_fri.append(val2015)

for val2017 in sat_list2017:
	input_sat.append(val2017)
for val2016 in sat_list2016:
	input_sat.append(val2016)
for val2015 in sat_list2015:
	input_sat.append(val2015)

for val2017 in sun_list2017:
	input_sun.append(val2017)
for val2016 in sun_list2016:
	input_sun.append(val2016)
for val2015 in sun_list2015:
	input_sun.append(val2015)









test_data_mon = numpy.mean(mon_list2018)
print "Mean of 2018 Monday",numpy.mean(mon_list2018)
test_data_tue = numpy.mean(tue_list2018)
test_data_wed = numpy.mean(wed_list2018)
test_data_thur = numpy.mean(thur_list2018)
test_data_fri = numpy.mean(fri_list2018)
test_data_sat = numpy.mean(sat_list2018)
test_data_sun = numpy.mean(sun_list2018)





x = ['Sun','Mon','Tue','Wed','Thur','Fri','Sat']


plt.xticks(range(len(y2015)),x)

plt.plot(y2015)
plt.ylabel('2015')



plt.show()

mean_of_data_mon = numpy.mean(input_mon)
stand_dev_mon = numpy.std(input_mon)

a = (test_data_mon - mean_of_data_mon)/stand_dev_mon
print "Monday z-score",a
print "Mean of Monday",mean_of_data_mon
print "Stand Dev of Monday", stand_dev_mon

mean_of_data_tue = numpy.mean(input_tue)
stand_dev_tue = numpy.std(input_tue)

a_tue = (test_data_tue - mean_of_data_tue)/stand_dev_tue
print "Tue z-score",a_tue
print "Mean of Tuesday",mean_of_data_tue
print "Stand Dev of Tuesday", stand_dev_tue

mean_of_data_wed = numpy.mean(input_wed)
stand_dev_wed = numpy.std(input_wed)

a_wed = (test_data_wed - mean_of_data_wed)/stand_dev_wed
print "Wed z-score",a_wed
print "Mean of Wed",mean_of_data_wed
print "Stand Dev of Wed", stand_dev_wed


mean_of_data_thur = numpy.mean(input_thur)
stand_dev_thur = numpy.std(input_thur)

a_thur = (test_data_thur - mean_of_data_thur)/stand_dev_thur
print "Thur z-score",a_thur
print "Mean of Thur",mean_of_data_thur
print "Stand Dev of Thur", stand_dev_thur


mean_of_data_fri = numpy.mean(input_fri)
stand_dev_fri = numpy.std(input_fri)

a_fri = (test_data_fri - mean_of_data_fri)/stand_dev_fri
print "Fri z-score",a_fri
print "Mean of Fri",mean_of_data_fri
print "Stand Dev of Fri", stand_dev_fri

mean_of_data_sat = numpy.mean(input_sat)
stand_dev_sat = numpy.std(input_sat)

a_sat = (test_data_sat - mean_of_data_sat)/stand_dev_sat
print "Sat z-score",a_sat
print "Mean of Sat",mean_of_data_sat
print "Stand Dev of Sat", stand_dev_sat

mean_of_data_sun = numpy.mean(input_sun)
stand_dev_sun = numpy.std(input_sun)

a_sun = (test_data_sun - mean_of_data_sun)/stand_dev_sun
print "Sun z-score",a_sun
print "Mean of Sun",mean_of_data_sun
print "Stand Dev of Sun", stand_dev_sun









# z_array = []
#
# for test in y2018:
# 	print test
# 	a = (test - mean_of_data)/stand_dev
# 	z_array.append(round(a,3))

# print "Z-Value ---- "
# print(z_array)

