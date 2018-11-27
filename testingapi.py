from datetime import timedelta, date
import json
import csv
import requests

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)



def setupAndIntial():
    start_date = date(2007, 01, 01)
    end_date = date(2009, 12, 31)
    source = "USD"
    currencies = "INR"
    f = open('data3.csv', "w")
    fields = ['date','source','tocurrency','rate']
    writer = csv.DictWriter(f,fields)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        d = start_date + timedelta(i)
        date_str = d.strftime('%Y-%m-%d')
        api = "http://apilayer.net/api/historical?access_key=3d1ce82772572a5fe161bd5e4bc6daeb&date=" + date_str + "&source=" + source + "&currencies=" + currencies
        response = requests.get(api)
        data = response.json()
        print data
        rate = data['quotes'][source+currencies]
        writer.writerow({'date': d, 'source': source, 'tocurrency': currencies , 'rate':rate})

    f.close()


if __name__ == '__main__':
    setupAndIntial()



