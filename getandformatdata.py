from datetime import timedelta, date
import csv
import requests
import pandas
import datetime
import numpy

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)



def setupAndIntial():
    start_date = date(2007, 01, 01)
    end_date = date(2007, 01, 02)
    source = "USD"
    currencies = "INR"
    f = open('data.csv', "a")
    fields = ['date','source','tocurrency','rate']
    writer = csv.DictWriter(f,fields)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        d = start_date + timedelta(i)
        date_str = d.strftime('%Y-%m-%d')
        api = "http://apilayer.net/api/historical?access_key=3d1ce82772572a5fe161bd5e4bc6daeb&date=" + \
              date_str + "&source=" + source + "&currencies=" + currencies
        response = requests.get(api)
        data = response.json()
        print data
        rate = data['quotes'][source+currencies]
        writer.writerow({'date': d, 'source': source, 'tocurrency': currencies , 'rate':rate})

    f.close()


def appendDayofweek():
    reader = csv.reader(open('2008/2008.csv', 'rb'))
    writer = csv.writer(open('2008/2008_final.csv', 'w'))
    headers = reader.next()
    headers.append("Day Of Week")
    writer.writerow(headers)
    for row in reader:
        dt = row[0]
        year, month, day = (int(x) for x in dt.split('-'))
        answer = date(year, month, day).weekday()
        row.append(answer)
        writer.writerow(row)




def calculateMeanYearly(file,year):
    print file
    reader = csv.reader(open(file, 'rb'))
    jan_list = []
    feb_list = []
    mar_list = []
    aprl_list = []
    may_list = []
    june_list = []
    july_list = []
    aug_list = []
    sept_list = []
    oct_list = []
    nov_list = []
    dec_list = []
    for row in reader:
        date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        if date.month == 1:
            jan_list.append(float(row[3]))
        elif date.month == 2:
            feb_list.append(float(row[3]))
        elif date.month == 3:
            mar_list.append(float(row[3]))
        elif date.month == 4:
            aprl_list.append(float(row[3]))
        elif date.month == 5:
            may_list.append(float(row[3]))
        elif date.month == 6:
            june_list.append(float(row[3]))
        elif date.month == 7:
            july_list.append(float(row[3]))
        elif date.month == 8:
            aug_list.append(float(row[3]))
        elif date.month == 9:
            sept_list.append(float(row[3]))
        elif date.month == 10:
            oct_list.append(float(row[3]))
        elif date.month == 11:
            nov_list.append(float(row[3]))
        elif date.month == 12:
            dec_list.append(float(row[3]))
    writer = csv.writer(open('yearwise_monthlymean.csv', 'a'))
    mean_list = [numpy.mean(jan_list),
                 numpy.mean(feb_list),
                 numpy.mean(mar_list),
                 numpy.mean(aprl_list),
                 numpy.mean(may_list),
                 numpy.mean(june_list),
                 numpy.mean(july_list),
                 numpy.mean(aug_list),
                 numpy.mean(sept_list),
                 numpy.mean(oct_list),
                 numpy.mean(nov_list),
                 numpy.mean(dec_list)]
    writer.writerow([year,mean_list])



if __name__ == '__main__':
    # setupAndIntial()
    appendDayofweek()
    # calculateMeanYearly('2009/2009_final.csv',"2009")



