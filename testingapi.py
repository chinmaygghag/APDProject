from datetime import timedelta, date
import cPickle as pickle
import json
import csv
import requests

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def collectData(start_date,end_date):
    record = {}
    for single_date in daterange(start_date,end_date):
        date = single_date.strftime("%Y-%m-%d")
        # api = "http://apilayer.net/api/historical?access_key=52d3f38e1e605a96e2267a0f783cfc70&date="+date
        # contents = urllib2.urlopen(api).read()
        rec = {
            'date': date
        }

        record.update(rec)
        print record
        return record

def insertData(record,file):
    for rec in record:
        file.write(rec)



def setupAndIntial():
    start_date = date(2015, 8, 2)
    end_date = date(2017, 1, 31)
    source = "USD"
    currencies = "INR"
    f = open('data.csv', "a")
    fields = ['date','source','tocurrency','rate']
    writer = csv.DictWriter(f,fields)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        d = start_date + timedelta(i)
        date_str = d.strftime('%Y-%m-%d')
        api = "http://apilayer.net/api/historical?access_key=52d3f38e1e605a96e2267a0f783cfc70&date=" + date_str + "&source=" + source + "&currencies=" + currencies
        response = requests.get(api)
        data = response.json()
        print data
        rate = data['quotes'][source+currencies]
        writer.writerow({'date': d, 'source': source, 'tocurrency': currencies , 'rate':rate})

    f.close()

def importData():
    # f = open("records.pkl","r")
    # print f.read()
    # for a in f.readline():
    #     print a
    with open("records.pkl","rb") as f:
        data = pickle.load(f)

    print data


if __name__ == '__main__':
    setupAndIntial()
    # importData()


