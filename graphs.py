import datetime
import numpy
import csv
import matplotlib.pyplot as plt



a = []
b = []
reader = csv.reader(open('2014/2014_final.csv', 'rb'))
for row in reader:
    date = datetime.datetime.strptime(row[0],'%Y-%m-%d')
    a.append(float(row[3]))
    b.append(row[0])

plt.ylabel('Dollar Rate in Rupees')
plt.xlabel('Days')
plt.plot(a)
plt.title("Year 2018")
plt.show()



x = ('Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov')
y2018 = (63.61552119354839, 64.44885832142856, 65.04169216129033, 65.68700323333333, 67.50892812903224, 67.75483848387097, 68.6614654516129, 69.57460880645161, 72.23412933333334, 73.73052035483872, 72.15457015999999)

# code for histogram
plt.bar(x,y2018,align='center') # A bar chart
plt.xlabel('Months')
plt.ylim(60,75)
plt.ylabel('Rates')
plt.title('Year 2018')
plt.xticks(range(len(y2018)),x)
plt.show()